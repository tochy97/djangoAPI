document.addEventListener("click", (event) => {
    let form = document.forms.main
    let sidebar = form.elements.sidebar;
    let toggle = form.elements.toggle;

    let eventTarget = event.target; // clicked element    

    do {
      if(eventTarget == sidebar || eventTarget == toggle) {
        // This is a click inside, does nothing, just return.
        return;
      }
      // Go up the DOM
        eventTarget = eventTarget.parentNode;
    } while (eventTarget);
        // This is a click outside.      
        closeSidebar();
})
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

    sidebar.style.width = "20%";
    sidebar.style.pointerEvent = "auto";
    toggle.style.visibility = "hidden";

    let options = document.querySelectorAll('a');

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "visible";
        if (i > 0)
        {
            options[i].addEventListener('click', openPage);
        }
    }
}

function closeSidebar ()
{
    let form = document.forms.main;

    let sidebar = form.elements.sidebar;
    let toggle = form.elements.toggle;

    sidebar.style.width = "0px";
    sidebar.style.pointerEvent = "none";
    toggle.style.visibility = "visible";

    let options = document.querySelectorAll('a');

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "hidden";
    }
}