let check_file_type=['jpg','gif','png','jpeg','bmp'];

$('form[name="writeform"]').submit(function(e) {
    let r=0;
    $('form').find('input').each(function(i,e) {
        if (e.value == "") {
            r = 1;
            return false;
        }
    });
    if (r) {
        alert("빈칸을 모두 채워주세요");
        return false;
    }
    imgType =  $('#post_pic').val().split('.').pop().toLowerCase();
    if(check_file_type.indexOf(imgType) == -1) {
        alert("이미지를 삽입하세요.");
        return false;
    }
});