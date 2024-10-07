async function StartAppoitment () {
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
            }
            break;
        default:
            object.classList.add("sideButton");
            break;
    }
    return object;
}

async function openPage (event)
{
    var page = event.target.innerHTML;
    await loadContent("pages", page, "content")
}
