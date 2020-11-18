$('form[name=loginform]').submit(function(event) {
    let a = $('#user_id');
    let b = $('#user_pw');
    if(a.val()=="" || b.val()=="") {
        alert("빈칸을 모두 채워주세요");
        return false;
    }
    let pwd = md5(b.val());
    b.val(pwd);
});
