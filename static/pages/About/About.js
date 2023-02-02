async function addContact() {
        const resp = await fetch("../Contact/Contact.html");
        const html = await resp.text();
        document.body.insertAdjacentHTML("beforeend", html);
}