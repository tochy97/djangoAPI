class RequestManager {
    constructor (element) {
        this.element = element;
        this.output = {};
    }
    self = this.element;
    
    async postData() 
    {
        return new Promise ( async (resolve, reject) => {
            let url = self.url.value;
            const csrftoken = getCookie('csrftoken');
            // Default options are marked with *
            const response = await fetch(url, {
                method: "POST", // *GET, POST, PUT, DELETE, etc.
                mode: "same-origin", // no-cors, *cors, same-origin
                cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
                credentials: "include", // include, *same-origin, omit
                headers: {
                "Content-Type": "application/json",
                "X-CSRFToken" : csrftoken,
                },
                redirect: "follow", // manual, *follow, error
                referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(self.data.data), // body data type must match "Content-Type" header
            });
            let output = await parseResponse(response)
            resolve(output);
        })
    }

    async #parseResponse(response) {
        return new Promise ( async (resolve, reject) => {
            response.json().then((res) => {
                this.output = res;
                resolve();
            }).catch(() =>{
                reject(null);
            })
        })
    }

}