function StartSidebar ()
{
    let self = document.forms.sidebar;

    let loggedIn = false;
console.log("test")
    self.isVisible = false;
    self.initialized = false;

    let toggle = self.elements.toggle;
    let sidebar = self.elements.sidebar;

    self.initialized = true;
}

function addOption (option, link)
{
    let self = document.forms.sidebar;

    let sidebar = self.elements.sidebar;
}

function openSidebar ()
{
    let self = document.forms.main;

    let sidebar = self.elements.sidebar;
    let toggle = self.elements.toggle;

    sidebar.style.width = "20%";
    toggle.style.visibility = "hidden";
}

function closeSidebar ()
{
    let self = document.forms.main;

    let sidebar = self.elements.sidebar;
    let toggle = self.elements.toggle;

    sidebar.style.width = "0px";
    toggle.style.visibility = "visible";
}