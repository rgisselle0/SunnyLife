window.addEventListener("load", Initial);

function Initial() 
{
    checkToteStock();
}

function checkToteStock() {
    let Totemsg = document.getElementById("Totemsg").textContent;
    if (Totemsg === "Out of stock") {
        document.getElementById("btnCartTote").disabled = true;
    } else {
        document.getElementById("btnCartTote").disabled = false;
    }
}