window.addEventListener("load", Initial);

function Initial() 
{
    checkGlueStock();
}

function checkGlueStock() {
    let Gluemsg = document.getElementById("Gluemsg").textContent;
    if (Gluemsg === "Out of stock") {
        document.getElementById("btnCartGlue").disabled = true;
    } else {
        document.getElementById("btnCartGlue").disabled = false;
    }
}