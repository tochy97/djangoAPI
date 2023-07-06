

async function StartApp()
{
    let self =  document.forms.main;

    // load in sidebar
    loadContent( "Sidebar", "nav", "StartSidebar()", "components" );
    // load in sidebar
    switch (window.location.pathname) {
        case "":
        case "/":
        case "/login":
        case "/Login":
            loadContent( "Login", "content", "StartLogin()", "pages" );
            break;
        case "/register":
        case "/Register":
            loadContent( "Register", "content", "StartRegister()", "pages" );
    }
}

async function loadContent (name, container, onload, dir)
{
    let url = "/static/" + dir + "/"
    let htmlSrc = url + name + "/" + name + ".html";
    let scriptSrc = url + name + "/" + name + ".js";

    let content = document.getElementById(container);

    // load html as text into content
    content.innerHTML = await (await fetch(htmlSrc)).text();
    loadScript(scriptSrc, function () {
        executeString(onload);
    });
}

function loadScript ( url, callback )
{
    // create script and set type
    var script = document.createElement("script")
    script.type = "text/javascript";
    if (script.readyState) {
        script.onreadystatechange = function() {
        if (script.readyState === "loaded" || script.readyState === "complete") {
            script.onreadystatechange = null;
            callback();
        }
        };
    } 
    else {
        script.onload = function() {
            callback();
        };
    }

    script.src = url;
    document.getElementsByTagName( "head" )[0].appendChild( script );
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