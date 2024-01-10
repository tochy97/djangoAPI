function StartQuick() {
    let form = document.forms.main;
    let quick = form.elements.quick;
    let chat = quick.querySelector(".chat");
    let notification = quick.querySelector(".notification");

    closeOptions();
}

function openOptions ()
{
    let form = document.forms.main;
    let widget = form.elements.widget;debugger
    let quickOptions = form.elements.quickOptions;

    let chatButton = widget.querySelector(".chatButton");
    let options = quickOptions.querySelectorAll('a, hr');

    chatButton.style.visibility = "hidden";
    quickOptions.style.visibility = "visible";
    widget.style.marginRight = "100px";

    quickOptions.style.height = "100%";

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "visible";
    }

    console.log("open")
}

function closeOptions ()
{
    let form = document.forms.main;
    let widget = form.elements.widget;debugger
    let quickOptions = form.elements.quickOptions;


    let chatButton = widget.querySelector(".chatButton");
    let options = quickOptions.querySelectorAll('a, hr');

    chatButton.style.visibility = "visible";
    quickOptions.style.visibility = "hidden";
    widget.style.marginRight = "0px";

    quickOptions.style.height = "0%";


    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "hidden";
    }

    console.log("close")
}