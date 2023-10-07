function bindEmailCaptchaClick() {
    $("#captcha-btn").click(function (event) {
        const that = $(this)
        event.preventDefault()
        const email = $("input[name='email']").val();
        let countdown = 5
        that.off("click")
        const timer = setInterval(function (){
            that.text(countdown)
            countdown--
            if(countdown <= 0) {
                clearInterval(timer)
                that.text("Get V-code")
                bindEmailCaptchaClick()
            }
        }, 1000);
        $.ajax({
            url: "/auth/captcha/email?email=" + email,
            method: "POST",
            success: function (result) {
                const code = result.code
                if(code === 200) {
                    alert("send success")
                } else {
                    alert(result.message)
                }
            },
            fail: function (error) {
                console.log(error)
            }
        })
    })
}

$(function () {
    bindEmailCaptchaClick()
})