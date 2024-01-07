async function StartSidebar () {
    let form = document.forms.main;

    let sidebar = form.elements.sidebar;
    document.addEventListener("click", (event) => {
        let toggle = form.elements.toggle;
        let closeSidebarButton = document.getElementsByName("closeSidebarButton");
        let eventTarget = event.target; // clicked element    
    
        do {
          if(eventTarget == sidebar) {
            // This is a click inside, does nothing, just return.
            return;
          }
          if(eventTarget == toggle) {
            openSidebar();
            return;
          }
          if(eventTarget == closeSidebarButton) {
            openSidcloseSidebarebar();
            return;
          }
          // Go up the DOM
            eventTarget = eventTarget.parentNode;
        } while (eventTarget);
            // This is a click outside.      
            closeSidebar();
    })
    sidebar.appendChild(createOption("Home"));
    if (await verify()) {
        sidebar.appendChild(createOption("Logout"));
    }
    else {
        sidebar.appendChild(createOption("Login"));
        sidebar.appendChild(createOption("Register"));
    }
    sidebar.appendChild(createOption("Settings"));
    
    let options = sidebar.querySelectorAll('a, hr');
    for (var i = 0; i < options.length; i++) 
    {
        if (i > 0 && options[i].name !== "Logout") 
        {
            options[i].addEventListener('click', openPage);
        }
    }
    closeSidebar();
    return;
}

function createOption (name) {
    var object = document.createElement("a");
    object.href = "javascript:void(0)";
    object.innerHTML = name;
    object.id ="sideButton";
    switch (name) {
        case "Logout" :
            object.onclick = () => {
                eraseCookie("data");
                location.reload();
            };
            break;
        default:
            break;
    }
    return object;
}

async function openPage (event)
{
    var page = event.target.innerHTML;
    await loadContent("pages", page, "content")
}

function openSidebar ()
{
    let form = document.forms.main;

    let sidebar = form.elements.sidebar;
    let toggle = form.elements.toggle;

    sidebar.style.pointerEvent = "auto";
    toggle.style.visibility = "hidden";

    let options = sidebar.querySelectorAll('a, hr');

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "visible";
    }
    sidebar.style.width = "auto";
}

function closeSidebar ()
{
    let form = document.forms.main;

    let sidebar = form.elements.sidebar;
    let toggle = form.elements.toggle;

    sidebar.style.pointerEvent = "none";
    toggle.style.visibility = "visible";

    let options = sidebar.querySelectorAll('a, hr');

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "hidden";
    }
    sidebar.style.width = "0px";
}