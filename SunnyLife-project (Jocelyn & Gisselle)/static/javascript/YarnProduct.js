window.addEventListener("load", Initial);

function Initial() 
{
    checkYarnStock();
}

function checkYarnStock() {
    let Yarnmsg = document.getElementById("Yarnmsg").textContent;
    if (Yarnmsg === "Out of stock") {
        document.getElementById("btnCartYarn").disabled = true;
    } else {
        document.getElementById("btnCartYarn").disabled = false;
    }
}