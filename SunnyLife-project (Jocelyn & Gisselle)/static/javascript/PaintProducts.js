window.addEventListener("load", Initial);

function Initial() 
{
    checkPaintStock();
}

function checkPaintStock() {
    let Paintmsg = document.getElementById("Paintmsg").textContent;
    if (Paintmsg === "Out of stock") {
        document.getElementById("btnCartPaint").disabled = true;
    } else {
        document.getElementById("btnCartPaint").disabled = false;
    }
}


