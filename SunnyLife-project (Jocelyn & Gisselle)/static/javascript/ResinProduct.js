window.addEventListener("load", Initial);

function Initial() 
{
    checkResinStock();
}

function checkResinStock() {
    let Resinmsg = document.getElementById("Resinmsg").textContent;
    if (Resinmsg === "Out of stock") {
        document.getElementById("btnCartResin").disabled = true;
    } else {
        document.getElementById("btnCartResin").disabled = false;
    }
}