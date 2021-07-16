/*
   Project:       puncSysDemo
   File Name:     index
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
*/
$(document).ready(function (){
    $("#punctuate").click(function () {
        sentence = $("#origin-sentence").val();

        // 未输入句子
        if(sentence == "") {
            layer.msg("请输入句子...", {
                icon: 2,
                time: 1500,
            })
        }
        else {
            $("#punctuate").html(
            "<i class=\"layui-icon layui-icon-loading\"></i>\n" +
            "                请求中..."
            )

            // post the request
            $.ajax({
                url: "/bert/inference",
                type: "POST",
                data: JSON.stringify({
                    "sentence": sentence,
                }),
                error: function(error){
                    $("#punctuate").html(
                        "<i class=\"layui-icon layui-icon-upload-drag\"></i>\n" +
                        "                去恢复"
                    );
                    layer.msg("请求失败，请重试...", {
                        icon: 2,
                        time: 1500,
                    });
                },
                success: function (response){
                    $("#punctuated-sentence").val(response.res);
                    $("#punctuate").html(
                        "<i class=\"layui-icon layui-icon-upload-drag\"></i>\n" +
                        "                去恢复"
                    );
                }
            })
        }
    })
})