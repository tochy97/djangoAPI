function StartQuick() {
    let form = document.forms.main;
    let quick = form.elements.quick;
    let chat = quick.querySelector(".chat");
    let notification = quick.querySelector(".notification");

    openOptions("N");
    return;
}

function loadNotification () {
    let form = document.forms.main;
    let widget = form.elements.widget;
    let quickOptions = form.elements.quickOptions;

    let notificationButton = widget.querySelector(".notificationButton");
    let quickOptionsHeader = quickOptions.querySelector(".quickOptionsHeader");

    quickOptionsHeader.innerHTML = "Notification";
    notificationButton.style.display = "none";
    return;
}

function loadChat () {
    let form = document.forms.main;
    let widget = form.elements.widget;
    let quickOptions = form.elements.quickOptions;

    let chatButton = widget.querySelector(".chatButton");
    let quickOptionsHeader = quickOptions.querySelector(".quickOptionsHeader");

    quickOptionsHeader.innerHTML = "Chat";
    chatButton.style.display = "none";
    return;
}

function openOptions (type)
{
    let form = document.forms.main;
    let widget = form.elements.widget;
    let quickOptions = form.elements.quickOptions;

    let chatButton = widget.querySelector(".chatButton");
    let notificationButton = widget.querySelector(".notificationButton");
    let quickOptionsHeader = quickOptions.querySelector(".quickOptionsHeader");
    let options = quickOptions.querySelectorAll('a, hr');

    if (quickOptions.isOpen === true) {
        closeOptions(type);
    }

    widget.style.marginRight = "100px";
    quickOptions.style.visibility = "visible";

    if (type === "N") {
        loadNotification();
    }
    else {
        loadChat();
    }

    quickOptions.style.height = "100%";

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "visible";
    }

    quickOptionsHeader.style.visibility = "visible";
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
    let quickOptionsHeader = quickOptions.querySelector(".quickOptionsHeader");
    let options = quickOptions.querySelectorAll('a, hr');

    chatButton.style.visibility = "visible";
    notificationButton.style.visibility = "visible";
    quickOptions.style.visibility = "hidden";
    widget.style.marginRight = "0px";

    quickOptions.style.height = "0%";

    chatButton.style.display = "";
    notificationButton.style.display = "";

    for (var i = 0; i < options.length; i++) {
        options[i].style.visibility = "hidden";
    }

    quickOptionsHeader.style.visibility = "hidden";
    quickOptions.isOpen = false;
    return;
}