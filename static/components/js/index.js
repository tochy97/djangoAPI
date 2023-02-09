async function addHTML(route) {
    const resp = await fetch(route);
    const html = await resp.text();
    document.body.insertAdjacentHTML("beforeend", html);
}

function loadComponents(){
    
}