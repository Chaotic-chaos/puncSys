# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     inference
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''
import argparse

import torch
from sanic import Blueprint, text, json
from transformers import BertTokenizer

from app.utils.punctuateWithBERT_CN.model import BERTForPunctuator
from app.utils.punctuateWithBERT_CN.nums2word.zh_tools.cn_tn_api import NSWNormalizer

inf = Blueprint("inference")

# init model
parser = argparse.ArgumentParser()

parser.add_argument("--ckp", default="app/utils/punctuateWithBERT_CN/checkpoint/epoch16.pt", help="where the model saved")
parser.add_argument("--label-vocab", default="app/utils/punctuateWithBERT_CN/dataset/label.dict.tsv")
parser.add_argument("--bert-path", default="app/utils/punctuateWithBERT_CN/pretrained_bert", help="where the pretrained bert model saved")
parser.add_argument("--device", default="cpu", help="whether use cpu or gpu")

args = parser.parse_args()

device = torch.device(args.device)

tokenizer = BertTokenizer.from_pretrained(args.bert_path)

checkpoint = torch.load(args.ckp, map_location=device)
# print(checkpoint)
model = BERTForPunctuator(5, device)
model.load_state_dict(checkpoint['model'])
model = model.to(device)
model.eval()

# load vocab
with open(args.label_vocab, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]
label_vocab = {int(e.split("\t")[1]): e.split("\t")[0][0] for e in lines}


@inf.post("/inference")
async def inference(request):
    sentence = request.json["sentence"]
    sentence = NSWNormalizer(sentence).normalize()
    sentence = list(sentence)

    ids = tokenizer.convert_tokens_to_ids(sentence)
    input = torch.tensor(ids, dtype=torch.long, device=device)

    with torch.no_grad():
        pred = model(input.unsqueeze(0))
    pred = pred.cpu()
    pred_ids = torch.argmax(pred.squeeze(0), 1).numpy().tolist()

    pred_label = [label_vocab.get(id) for id in pred_ids]

    res = []
    for word, label in zip(sentence, pred_label):
        res.append(f"{word}{label if label != '_' else ''}")

    return json({
        "res": "".join(res),
    })
