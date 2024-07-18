window.addEventListener("load", Initial);

function Initial() 
{
	checkGelPensStock();
}

function checkGelPensStock() {
    let GelPensmsg = document.getElementById("GelPensmsg").textContent;
    if (GelPensmsg === "Out of stock") {
        document.getElementById("btnCartGelPens").disabled = true;
    } else {
        document.getElementById("btnCartGelPens").disabled = false;
    }
}