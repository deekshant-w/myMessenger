const inputElement = document.querySelector('input[type="file"]');
const pond = FilePond.create(inputElement);
FilePond.setOptions({
    instantUpload: false,
    allowMultiple: true,
    dropOnPage: true,
    credits: false

});

pond.setOptions({
    dropOnPage: true,
    credits: false
})

// csrf cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// form submit
document.querySelector("#saveMsg").addEventListener("click", () => {
    let msgForm = document.querySelector("#newMsg");
    let formdata = new FormData(msgForm);
    formdata.delete("filepond");
    for(var i=0;i<pond.getFiles().length;i++){
        formdata.append("file",pond.getFiles()[i].file)
    }
    for (var [key, value] of formdata.entries()) {
        console.log(key, value);
    }
    
    $.ajax({
        url: '/',
        type: 'POST',
        data: formdata,
        cache : false,
        processData: false,
        contentType: false,
        success: function(a){
            location.reload();
        },
        failure: function(a){
            console.log(a)
            alert("Failed")
        }
    });
})

// target = "_blank"
document.querySelectorAll('a[rel=nofollow]').forEach((ele)=>{ele.target = "_blank"})

// refresh page
document.querySelector("#refBut").addEventListener("click",()=>{
    try{
        caches.keys().then(function(names) {
            for (let name of names)
                caches.delete(name);
        });
    }catch(err){};
    
    window.location.href = window.location.href
})