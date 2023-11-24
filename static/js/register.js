function bindEmailCaptchaClick() {
  $("#captcha-btn").click(function (event) {
      // this: 代表当前按钮的 jQuery 对象
      var $this = $(this);
      // 阻止默认的事件
      event.preventDefault();

      var email = $("input[name='email']").val();
      $.ajax({
          url: "/auth/captcha/email?email=" + email,
          method: "GET",
          success: function (result) {
              var code = result['code'];
              if (code == 200) {
                  var countdown = 60;
                  // 开始倒计时之前，取消按钮的点击事件
                  $this.off("click");
                  var timer = setInterval(function () {
                      $this.text(countdown);
                      countdown -= 1;
                      // 倒计时结束时执行
                      if (countdown <= 0) {
                          // 清除定时器
                          clearInterval(timer);
                          // 按钮文本恢复原样
                          $this.text("获取验证码");
                          // 重新绑定点击事件
                          bindEmailCaptchaClick();
                      }
                  }, 1000);
                   $("#success-message").text("邮箱验证码发送成功!").show();
                    setTimeout(function () {
                        $("#success-message").hide(); // 3秒后隐藏消息
                    }, 3000);
              } else {
                  alert(result['message']);
              }
          },
          error: function (error) {
              console.log(error);
          }
      });
  });
}

// 整个网页加载完成后再执行
$(function () {
  bindEmailCaptchaClick();
});
