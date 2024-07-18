window.addEventListener("load", Initial);

function Initial() 
{
    checkSewNeedlesStock();
}

function checkSewNeedlesStock() {
    let SewNeedlesmsg = document.getElementById("SewNeedlesmsg").textContent;
    if (SewNeedlesmsg === "Out of stock") {
        document.getElementById("btnCartSewNeedles").disabled = true;
    } else {
        document.getElementById("btnCartSewNeedles").disabled = false;
    }
}