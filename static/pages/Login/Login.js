async function sendLogin() {
    let self = document.forms.main;
    self.data.data = loginRequest(self.uname.value, self.psw.value);
    self.url.value = "user/graphql";
        
    let response = await postData();
    setCookie("data", response.data.tokenAuth.token, 1);
    location.reload();
}

let self = document.forms.main;
self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendLogin();
});