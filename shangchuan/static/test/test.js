$(function () {
    // getjson();
    window.setInterval(function ()
    {
         /*getjson();*/
    },1000);
})

// function getjson() {
//     $.ajax({
//         type: "get",
//         url: "test.json",
//         //async: false,       //修改成为同步
//         error: erryFunction,  //错误执行方法
//         success: succFunction //成功执行方法
//     });
// }

function erryFunction() {
    console.log("ajax error!")
}
function succFunction(tt) {
    var json = eval(tt); //数组
    var tt = "";
    $.each(json, function (index) {
        var length = json.length;
        //循环获取数据
        var time = json[index].time;
        var message = json[index].message;
        var imgsrc1 = json[index].imgsrc1;
        var imgsrc2 = json[index].imgsrc2;
        var imgsrc3 = json[index].imgsrc3;
        var imgsrc4 = json[index].imgsrc4;
        //tt += Id + "___" + Name + "___" + Age + "___" + Score + "<br>";
        if(index==0){
            //alert(imgsrc1);
            tt+="<div class=\"time\" id=\"newtime\">"+time+"</div>\n" +
                "<li>\n" +
                "    <article class=\"message\">"+message+"</article>\n" +
                "    <div class=\"border\">\n" +
                "        <figure class=\"picture\">";
            if(imgsrc1!=undefined)
                tt+="<a class='imgbox' href=\""+ imgsrc1+"\">\n" +
                    "                <img src=\""+imgsrc1+"\"+>\n" +
                    "            </a>";
            if(imgsrc2!=undefined)
                tt+="<a class='imgbox' href=\""+ imgsrc2+"\">\n" +
                    "                <img src=\""+imgsrc2+"\"+>\n" +
                    "            </a>";
            if(imgsrc3!=undefined)
                tt+="<a class='imgbox' href=\""+ imgsrc3+"\">\n" +
                    "                <img src=\""+imgsrc3+"\"+>\n" +
                    "            </a>";
            if(imgsrc4!=undefined)
                tt+="<a class='imgbox' href=\""+ imgsrc4+"\">\n" +
                    "                <img src=\""+imgsrc4+"\"+>\n" +
                    "            </a>";

            //alert(tt);
            tt+="</figure>\n" +
                "    </div>\n" +
                "</li>";
        }else if(index==length-1){/*   class="border"id="newtime"*/
            tt+="<div class=\"time\" >"+time+"</div>\n" +
                "<li>\n" +
                "    <article class=\"message\">"+message+"</article>\n" +
                "    <div  id='lastborder'>\n" +
                "        <figure class=\"picture\">";
            if(imgsrc1!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc1+"\">\n" +
                    "                <img src=\""+imgsrc1+"\"+>\n" +
                    "            </a>";
            if(imgsrc2!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc2+"\">\n" +
                    "                <img src=\""+imgsrc2+"\"+>\n" +
                    "            </a>";
            if(imgsrc3!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc3+"\">\n" +
                    "                <img src=\""+imgsrc3+"\"+>\n" +
                    "            </a>";
            if(imgsrc4!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc4+"\">\n" +
                    "                <img src=\""+imgsrc4+"\"+>\n" +
                    "            </a>";

            //alert(tt);
            tt+="</figure>\n" +
                "    </div>\n" +
                "</li>";
        }
        else {
            tt+="<div class=\"time\">"+time+"</div>\n" +
                "<li>\n" +
                "    <article class=\"message\">"+message+"</article>\n" +
                "    <div class=\"border\">\n" +
                "        <figure class=\"picture\">";
            if(imgsrc1!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc1+"\">\n" +
                    "                <img src=\""+imgsrc1+"\"+>\n" +
                    "            </a>";
            if(imgsrc2!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc2+"\">\n" +
                    "                <img src=\""+imgsrc2+"\"+>\n" +
                    "            </a>";
            if(imgsrc3!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc3+"\">\n" +
                    "                <img src=\""+imgsrc3+"\"+>\n" +
                    "            </a>";
            if(imgsrc4!=undefined)
                tt+="<a class='imgbox' href=\""+imgsrc4+"\">\n" +
                    "                <img src=\""+imgsrc4+"\"+>\n" +
                    "            </a>";


            tt+="</figure>\n" +
                "    </div>\n" +
                "</li>";
        }
    });
    $("#begin" ).html(tt);

    $(".imgbox").imgbox({
        'speedIn'		: 0,
        'speedOut'		: 0,
        'alignment'	: 'center',
        'overlayShow'	: true,
        'allowMultiple'	: false
    });
}