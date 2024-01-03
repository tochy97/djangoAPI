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
        
    let response = await postData();
    try {
        setCookie("data", response.data.tokenAuth.token, 1);
    }
    catch {
        alert("Invalid username or password!")
    }
    finally {
        location.reload();
    }
}

let self = document.forms.main;
self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendLogin();
});