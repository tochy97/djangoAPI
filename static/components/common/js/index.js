const url = (dir, name) => "/static/" + dir + "/" + name + "/" + name;

async function StartApp()
{
    let self =  document.forms.main;

    // load in sidebar
    let sidebar = await loadContent( "components", "Sidebar", "nav");
    let settings = await loadContent( "pages", "Login", "content");

    // load in content
    let content;
    
}

async function loadContent ( dir, name, container )
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

function loadScript ( url, container )
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