let check_file_type=['jpg','gif','png','jpeg','bmp'];
$('form[name="profileform"]').submit(function(e) {
    $(this).find("input:radio[name=search_type]:checked").val()

    let t = $(this).find('input[name="formtype"]').val();
    if (t == "set1") { 
        let pic = $('#user_pic');
        if (!pic.attr("disabled")) {
            imgType =  pic.val().split('.').pop().toLowerCase();
            console.log(imgType);
            if(check_file_type.indexOf(imgType)==-1) {
                alert("이미지를 삽입하세요.");
                return false;
            }
        }
    } else if (t == "set2") {
        if ($('#user_name').val() == "") {
            alert("이름이 있어야 합니다.");
            return false;
        }
    } else {
        return false;
    }
});
$('input[type="radio"]').change(function(e) {
    let pic = $('#user_pic');
    if (this.value == "0") {
        pic.val("");
        pic.attr("disabled", "disabled");
    } else {
        pic.removeAttr("disabled");
    }
})
