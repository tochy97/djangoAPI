async function sendLogin() {
    let self = document.forms.main;
    if (self.uname.value === "") {
        self.uname.focus()
        return alert("Username is required!")
    }
    if (self.psw.value === "") {
        self.psw.focus()
        return alert("Password is required!")
    }
    self.data.data = loginRequest(self.uname.value, self.psw.value);

    postData().then( response => {
        setCookie("data", response?.data.tokenAuth.token, 1);
    }).catch((err) =>{
        console.log(err)
        alert("Invalid username or password!");
    }).finally(() =>{
        location.reload()
    });
}

let self = document.forms.main;
self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendLogin();
});