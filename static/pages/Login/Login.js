self = document.forms.main;

async function sendLogin() {
    return new Promise ( async (resolve, reject) => {
        self.data.data = {
            user: self.uname.value,
            password: self.psw.value
        };
        self.url.value = "user/auth/"
        
        
        let response = await postData();
        resolve(true);
    })
}

self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendLogin();
});