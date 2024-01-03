async function loadContent ( dir = "", name = "", container = "", fnCallback = "" )
{
    return new Promise ( async (resolve, reject) => {
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
        content.scriptSrc = await loadScript( url(dir, name), container );
        // if it loads and return the element
        content.scriptSrc.addEventListener("load", () => {
            console.log(name + ": Fully loaded.")
            try {
                eval(fnCallback)
                console.log(name + ": Initialized.")
            }
            catch {
                console.log(name + " has no valid initializer.")
            }
        });
    
        content.scriptSrc.addEventListener("error", (err) => {
            console.log(name + " :Error on loading file", err);
        });
        // load request
        oldScript = document.getElementById("contentRequestScript")
        if (oldScript) 
        {
            oldScript.remove();
        }
        content.requestSrc = await loadScript( requestUrl(dir, name), container, "Request");
        // if it loads and return the element
        content.requestSrc.addEventListener("load", () => {
            console.log(name + ": Requests fully loaded.");
        });
    
        content.requestSrc.addEventListener("error", (err) => {
            console.log(name + " :Error on loading file", err);
        });
        resolve(content);
    })
}

async function loadScript ( url = "", container = "", name = "" )
{
    let scriptSrc = url + ".js";
    // create script and set type
    var script = document.createElement("script")
    script.type = "text/javascript";
    script.id = container + name + "Script"
    
    // set src
    script.setAttribute("src", scriptSrc);
    document.body.prepend(script);
    return script

}

function loadUser ( data = {} )
{
    let self = document.forms.main;
    try {
        self.user.value = data.verifyToken.payload.username;
    }
    catch {
        return false;
    }
    return true;
}