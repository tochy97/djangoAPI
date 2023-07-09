const url = (dir, name) => "/static/" + dir + "/" + name + "/" + name;

async function StartApp()
{
    let self =  document.forms.main;

    // load in sidebar
    let sidebar = await loadContent( url("components", "Sidebar"), "nav", "StartSidebar()" );

    // load in content
    let content;
    switch (window.location.pathname) {
        case "":
        case "/":
        case "/login":
        case "/Login":
            content = await loadContent( url("pages", "Login"), "content" );
            break;
        case "/register":
        case "/Register":
            content = await loadContent( url("pages", "Register"), "content" );
    }
}

async function loadContent ( url, container, callback )
{
    let htmlSrc = url + ".html";

    let content = document.getElementById(container);

    // load html as text into content
    content.innerHTML = await (await fetch(htmlSrc)).text();
    // load script
    content.scriptSrc = loadScript( url, callback );

    return content;
}

function loadScript ( url, callback )
{
    let scriptSrc = url + ".js";
    // create script and set type
    var script = document.createElement("script")
    script.type = "text/javascript";
    
    // set src
    script.setAttribute("src", scriptSrc);
    document.body.appendChild(script);

    // if it loads execute callback and return the element
    script.addEventListener("load", () => {
        executeString(callback);
        return script;
    });
    
    script.addEventListener("error", () => {
        return null;
    });
}

function executeString (exec)
{
    // function we want to run
    var fnstring = exec;

    // find object
    var fn = window[fnstring];

    // run if object is a function
    if (typeof fn === "function") fn();
}