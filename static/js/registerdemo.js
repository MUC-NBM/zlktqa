//整个网页部加载完毕后再执行的
$(function (){
    $("#captcha-btn").click(function (event){
        // 阻止默认的事件
        event.preventDefault();

        var email = $("input[name='email']").val();
        $.ajax({
             // http://127.0.0.1:500
            // /auth/captcha/email?email=xx@qq.com
            url: "/auth/captcha/email?email="+email,
            method:"GET",
            success: function (result){
                var code = result['code'];
                if(code == 200){
                var countdown = 60;
                //开始倒计时之前就取消掉off事件
                this.off("click")
                var timer = setInterval(function (){
                $this.text(countdown);
                countdown -= 1;
                //倒计时结束时执行
                if(countdown <= 0 ){
                // 清掉定时器
                clearInterval(timer);
                //将按钮的文字重新修改回来
                $this.text("获取验证码");
                //重新绑定点击事件
                }
            },
            error: function (error){ // 应该是 error 而不是 fail
                console.log(error);
            }
        });
    });
});
