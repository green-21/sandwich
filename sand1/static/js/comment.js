$('form[name="sand-comment-form"]').submit( function(e) {
    if(!$('#comment-msg').val()) {
        alert("댓글을 입력하세요");
        return false;
    }
});