window.addEventListener("load", Initial);

function Initial()
{
	checkCanvasStock();
}

function checkCanvasStock() {
    let Canvasmsg = document.getElementById("Canvasmsg").textContent;
    if (Canvasmsg === "Out of stock") {
        document.getElementById("btnCartCanvas").disabled = true;
    } else {
        document.getElementById("btnCartCanvas").disabled = false;
    }
}