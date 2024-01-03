const url = (dir = "", name = "") => "/static/" + dir + "/" + name + "/" + name;
const requestUrl = (dir = "", name = "") => "/static/" + dir + "/" + name + "/requests";
async function StartApp()
{
    if (await verify()) {
        let content = await loadContent( "pages", "Settings", "content");
    }
    else {
        let content = await loadContent( "pages", "Login", "content");
    }
    // load in sidebar
    let sidebar = await loadContent( "components", "Sidebar", "nav", "StartSidebar()");
    // load in content
}

async function verify ()
{
    let self = document.forms.main;
    let data = getCookie("data")
    self.data.data = verifyRequest(data);
    self.url.value = "graphql";
    let response = await postData();
    return loadUser(response.data);
}

async function postData () 
{
    return new Promise ( async (resolve, reject) => {
        let self = document.forms.main;
        let url = self.url.value;
        const csrftoken = getCookie('csrftoken');
        // Default options are marked with *
        const response = await fetch(url, {
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "same-origin", // no-cors, *cors, same-origin
            cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
            credentials: "same-origin", // include, *same-origin, omit
            headers: {
            "Content-Type": "application/json",
            "X-CSRFToken" : csrftoken,
            },
            redirect: "follow", // manual, *follow, error
            referrerPolicy: "same-origin", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            body: JSON.stringify(self.data.data), // body data type must match "Content-Type" header
        });
        
        resolve(response.json());
    })
}

function parseResponse (response) {
    try {

    }
    catch {

    }
    finally {

    }
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {
    let self = document.forms.main;
    let input = getCookie("data");
    self.data.data = logout(input);
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
