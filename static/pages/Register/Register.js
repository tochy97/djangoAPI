self = document.forms.main;

async function sendRegister() {
    return new Promise ( async (resolve, reject) => {
        self.data.data = {
            username: self.uname.value,
            email: self.email.value,
            password: self.psw.value,
            repassword: self.rpsw.value
        };
        self.url.value = "user/register/"
        
        
        let response = await postData();
        resolve(true);
    })
}

self.send.addEventListener("click", function(event) {
    event.preventDefault()
    sendRegister();
});