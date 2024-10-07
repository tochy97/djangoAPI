const url = (dir = "", name = "") => "/static/" + dir + "/" + name + "/" + name;
const requestUrl = (dir = "", name = "") => "/static/" + dir + "/" + name + "/requests";
async function StartApp()
{
    // let RequestManager = new RequestManager(this);
    // let CookiesManager = new CookiesManager();
    // load in content
    // if (await verify()) {
    //     await loadContent( "pages", "Settings", "content");
    //     await loadContent( "components", "Quick", "quick", "StartQuick()");
    // }
    // else {
        await loadContent( "pages", "Login", "content");
    // }
    // load in components
    await loadContent( "components", "Sidebar", "nav", "StartSidebar()");
}

async function verify()
{
    let self = document.forms.main;
    // let data = getCookie("data")
    // self.data.data = verifyRequest(data);
    self.url.value = "graphql";
    // let response = await postData();
    // return loadUser(response?.data);
}

function universal_log(component, status) {
    switch (status) {
        case 0:
            console.log(component + " has failed. - " +  status);
            break;
        case 100:
            console.log(component + " finished loading. - " + status);
            break;
        case 200:
            console.log(component + " decision - " + status)
            break;
        default:
            console.log(component + " exited with unknown status.");
            break;
    }
}