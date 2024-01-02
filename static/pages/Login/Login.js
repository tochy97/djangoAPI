self = document.forms.main;

async function sendLogin() {
    return new Promise ( async (resolve, reject) => {
        self.data.data = loginRequest(self.uname.value, self.psw.value);debugger
        self.url.value = "user/graphql";
        
        let response = await postData();
        resolve(true);
    })
}

self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendLogin();
});