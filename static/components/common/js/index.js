const url = (dir = "", name = "") => "/static/" + dir + "/" + name + "/" + name;

async function StartApp()
{
    let self =  document.forms.main;

    return new Promise( async (resolve, reject) => {
        // load in sidebar
        let sidebar = await loadContent( "components", "Sidebar", "nav");
        // load in content
        let content = await loadContent( "pages", "Login", "content");
        resolve(true);
    })
}   

async function loadContent ( dir = "", name = "", container = "" )
{
    let htmlSrc = url(dir, name) + ".html";

    let content = document.getElementById(container);

    // load html as text into content
    content.innerHTML = await (await fetch(htmlSrc)).text();
    // load script
    let oldScript = document.getElementById("contentScript")
    if (oldScript) 
    {
        oldScript.remove();
    }
    content.scriptSrc = loadScript( url(dir, name), container );

    return content;
}

function loadScript ( url = "", container = "" )
{
    let scriptSrc = url + ".js";
    // create script and set type
    var script = document.createElement("script")
    script.type = "text/javascript";
    script.id = container + "Script"
    
    // set src
    script.setAttribute("src", scriptSrc);
    document.body.prepend(script);

    // if it loads and return the element
    script.addEventListener("load", () => {
        script.onreadystatechange = function () {
            return script;
        }
    });

    script.addEventListener("error", () => {
        return null;
    });
}

async function postData () 
{
    let url = self.url.value;
    // Default options are marked with *
    const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
        "Content-Type": "application/json",
        // "Header" : access
        },
        redirect: "follow", // manual, *follow, error
        referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(self.data.data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
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
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
