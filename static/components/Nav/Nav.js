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

function loadOkech(){
    const csrftoken = getCookie('csrftoken')
    fetch("http://127.0.0.1:8000/okechAPI/", {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        redirect: 'follow',
    })
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        console.log(error)
    })
    alert("done")
}

function loadCJ(){

}