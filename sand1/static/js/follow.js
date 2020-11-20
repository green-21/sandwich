$('body').on('click','a.sand-follow-btn', function(e) {
    a = this;
    let str = this.attributes.value.value;
    $.ajax({
        url: "follow_request",
        data: {  to_id : str,
                action : "f" },
        method: "GET",
        dataType: "json"
    })
    .done((r) => {
        if(r == "-1") {
            location.reload();
            return;
        }
        this.classList.remove("ui-shadow-inset");
        this.classList.add("ui-btn-active");
        this.classList.replace("sand-follow-btn", "sand-unfollow-btn");
        this.classList.replace("ui-icon-plus","ui-icon-minus");
        // 함수 체인지
    });
});

$('body').on('click','a.sand-unfollow-btn', function(e) {
    let str = this.attributes.value.value;
    $.ajax({
        url: "follow_request",
        data: {  to_id : str,
                action : "u" },
        method: "GET",
        dataType: "json"
    })
    .done((r) => {
        if(r == "-1") {
            location.reload();
            return;
        }
        this.classList.remove("ui-shadow-inset");
        this.classList.remove("ui-btn-active");
        this.classList.replace("sand-unfollow-btn","sand-follow-btn");
        this.classList.replace("ui-icon-minus","ui-icon-plus");
        // 함수 체인지
    });
});