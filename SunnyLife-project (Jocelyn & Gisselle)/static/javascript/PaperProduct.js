window.addEventListener("load", Initial);

function Initial() 
{
	checkPaperStock();
}

function checkPaperStock() {
    let Papermsg = document.getElementById("Papermsg").textContent;
    if (Papermsg === "Out of stock") {
        document.getElementById("btnPaperCart").disabled = true;
    } else {
        document.getElementById("btnPaperCart").disabled = false;
    }
}