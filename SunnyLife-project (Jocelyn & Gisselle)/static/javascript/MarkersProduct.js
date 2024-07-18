window.addEventListener("load", Initial);

function Initial() 
{
    checkMarkersStock();
}

function checkMarkersStock() {
    let Markersmsg = document.getElementById("Markerssmsg").textContent;
    if (Markersmsg === "Out of stock") {
        document.getElementById("btnCartMarkers").disabled = true;
    } else {
        document.getElementById("btnCartMarkers").disabled = false;
    }
}