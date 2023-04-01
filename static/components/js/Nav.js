
function toContact(){
    var content = document.getElementById("Content");
    var contact = content.contentWindow.document.getElementById("Contact");
    var email = content.contentWindow.document.getElementById("email");
    var form = content.contentWindow.document.getElementById("contactForm");
    contact.scrollIntoView();
    email.focus();
}

function createCalender(){
    var getPast = require("../CalenderApp/getPast");
    var calender = getPast();
    console.log(calender)
}

function loadPage(name) {
  var content = document.getElementById("Content");
  switch (name) {
    case "Register":
        content.src = "/static/pages/Register/Register.html";
        break;
    case "Login":
        content.src = "/static/pages/Login/Login.html";
        break;
    case "Contact":
        content.src = "/static/pages/Contact/Contact.html";
        break;
    default:
        content.src = "/static/pages/About/About.html";
        break;
  }
  console.log("here", content.data);
}