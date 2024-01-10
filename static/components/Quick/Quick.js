function StartQuick() {
    let form = document.forms.main;
    let quick = form.elements.quick;
    let chat = quick.querySelector(".chat");
    let notification = quick.querySelector(".notification");

    closeOptions();
    return;
}

function openOptions (type)
{
    let form = document.forms.main;
    let widget = form.elements.widget;
    let quickOptions = form.elements.quickOptions;

    let chatButton = widget.querySelector(".chatButton");
    let notificationButton = widget.querySelector(".notificationButton");
    let options = quickOptions.querySelectorAll('a, hr');

    if (quickOptions.isOpen === true) {
        closeOptions(type);
    }

    quickOptions.style.visibility = "visible";
    widget.style.marginRight = "100px";

    if (type === "N") {
        quickOptions.style.borderColor = "rgb(255,0,0)";
        notificationButton.style.visibility = "hidden";
    }
    else {
        quickOptions.style.borderColor = "rgb(255,255,0)";
        chatButton.style.visibility = "hidden";
    }

    quickOptions.style.height = "100%";

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "visible";
    }

    quickOptions.isOpen = true;
    return;
}

function closeOptions (type)
{
    let form = document.forms.main;
    let widget = form.elements.widget;
    let quickOptions = form.elements.quickOptions;


    let chatButton = widget.querySelector(".chatButton");
    let notificationButton = widget.querySelector(".notificationButton");
    let options = quickOptions.querySelectorAll('a, hr');

    chatButton.style.visibility = "visible";
    notificationButton.style.visibility = "visible";
    quickOptions.style.visibility = "hidden";
    widget.style.marginRight = "0px";

    quickOptions.style.height = "0%";

    if (type === "N") {
        chatButton.style.visibility = "visible";
    }
    else {
        notificationButton.style.visibility = "visible";
    }

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "hidden";
    }

    quickOptions.isOpen = false;
    return;
}