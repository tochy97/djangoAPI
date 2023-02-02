function loadPage(name){
    content = document.getElementById('Content');
    switch(name){
        case 'Register':
            content.data="/static/pages/Register/Register.html"
            break;
        case 'Login':
            content.data="/static/pages/Login/Login.html"
            break;
        case 'Contact':
            content.data="/static/pages/Contact/Contact.html"
            break;
        default:
            location.reload();
            break;
    }
}