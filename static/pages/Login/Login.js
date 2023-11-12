self = document.forms.main;

async function sendLogin(){
    return new Promise ( async (resolve, reject) => {
        self.data = {
            username: self.uname.value,
            password: self.psw.value
        };
        self.url.value += "auth/"
        debugger
        
        let request = addRequestHandler(true);
        let res = self.dispatchEvent(request);
        setCookie("access", res.access, 1);
        setCookie("refresh", res.refresh, 1);
        resolve(true);
    })
}

self.send.onclick = sendLogin;