a=0;
$('body').on('click','a.sand-like-btn', function(e) {
    let info = this.attributes.value.value.split("/");
    $.ajax({
        url: "/like_request",
        data: { doc_no : info[0], 
                doc_type : info[1],
                action : "l" },
        method: "GET",
        dataType: "json"
    })
    .done((r) => {
        if(r == "-1") {
            location.reload();
            return;
        }
        $(this).parent().find('span')[0].innerText = r;
        this.classList.add("ui-btn-active");
        this.classList.replace("sand-like-btn", "sand-unlike-btn");
        this.classList.remove("ui-shadow-inset");
    });
});

$('body').on('click','a.sand-unlike-btn', function(e) {
    let info = this.attributes.value.value.split("/");
    $.ajax({
        url: "/like_request",
        data: { doc_no : info[0], 
                doc_type : info[1],
                action : "u" },
        method: "GET",
        dataType: "json"
    })
    .done((r) => {
        if(r == "-1") {
            location.reload();
            return;
        }
        $(this).parent().find('span')[0].innerText = r;
        this.classList.remove("ui-btn-active");
        this.classList.replace("sand-unlike-btn", "sand-like-btn");
        this.classList.remove("ui-shadow-inset");
    });
});