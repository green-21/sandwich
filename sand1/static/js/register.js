let isID = false;
let isPW = false;
function offIdMsg() {
    if ($('#imp_id_msg').css("display") != "none")
        $('#imp_id_msg').css("display", "none");
    if ($('#p_id_msg').css("display") != "none")
        $('#p_id_msg').css("display", "none");
}

function onIdMsg(flag) {
    offIdMsg();
    isID = false;
    switch(flag) {
        case 0:
            $('#imp_id_msg').css("display", "block");
            break;
        case 1:
            $('#p_id_msg').css("display", "block");
            isID = true;
            break;
    }
}
function idMsgCheck(event) {
    if ($('#user_id').val() == "") {
        onIdMsg(3);
        return;
    }
    let idRule = /^[0-9a-zA-Z_]{5,15}$/
    let idVal = $('#user_id').val();
    if (idRule.test(idVal)) {
        $.ajax({
            url: "register_id_check",
            data: { user_id : idVal },
            method: "GET",
            dataType: "json"
        })
        .done(function(result) {
            if(result == "1"){
                onIdMsg(1);
                return;
            }
        });
    }
    onIdMsg(0);
}

$('#user_id').keyup(idMsgCheck);

function checkPW(event) {
    isPW = false;
    let a = $('#user_pw').val();
    let b = $('#user_pw2').val();
    
    if (a != "" && b != "") {
        if (a == b) {

            isPW = true;
            if ($('#pw_check_msg').css("display") != "none")
                $('#pw_check_msg').css("display", "none");
        } else {
            if ($('#pw_check_msg').css("display") == "none")
                $('#pw_check_msg').css("display", "block");
        }
    }
}
$('#user_pw').keyup(checkPW);
$('#user_pw').keydown(checkPW);
$('#user_pw2').keyup(checkPW);
$('#user_pw2').keydown(checkPW);


$('form[name="registerform"]').submit(function(event) {
    if (!isID || !isPW || $('#user_name').val() == "") {
        alert("양식을 제대로 완성해주세요.");
        return false;
    }
    let pwd = $('#user_pw').val();
    $('#user_pw').val(md5(pwd));
});