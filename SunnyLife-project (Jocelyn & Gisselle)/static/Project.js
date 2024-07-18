window.addEventListener("load", Initial);
window.addEventListener("load", addListener);

function Initial() {
    document.getElementById("DivCartPaint").style.display = "none";
    document.getElementById("DivCartYarn").style.display = "none";
    document.getElementById("DivCartCanvas").style.display = "none";
    document.getElementById("DivCartGelPens").style.display = "none";
    document.getElementById("DivCartSewNeedles").style.display = "none"; 
    document.getElementById("DivCartMarkers").style.display = "none";
    document.getElementById("DivCartTote").style.display = "none";
    document.getElementById("DivCartPaper").style.display = "none";
    document.getElementById("DivCartResin").style.display = "none";
    document.getElementById("DivCartGlue").style.display = "none";
}

function addListener() {
    document.getElementById("btnCartCanvas").addEventListener("click", AddtoCartCanvas);
    document.getElementById("btnCartGelPens").addEventListener("click", AddtoCartGelPens);
    document.getElementById("btnCartGlue").addEventListener("click", AddtoCartGlue);
    document.getElementById("btnCartMarkers").addEventListener("click", AddtoCartMarkers);
    document.getElementById("btnCartPaint").addEventListener("click", AddtoCartPaint);
    document.getElementById("btnCartResin").addEventListener("click", AddtoCartResin);
    document.getElementById("btnCartTote").addEventListener("click", AddtoCartTote);
    document.getElementById("btnCartSewNeedles").addEventListener("click", AddtoCartSewNeedles); 
    document.getElementById("btnCartPaper").addEventListener("click", AddtoCartPaper);
    document.getElementById("btnCartYarn").addEventListener("click", AddtoCartYarn);
}

function AddtoCartCanvas() {
    document.getElementById("DivCartCanvas").style.display = "block";
}

function AddtoCartGelPens() {
    document.getElementById("DivCartGelPens").style.display = "block";
}

function AddtoCartGlue() {
    document.getElementById("DivCartGlue").style.display = "block";
}

function AddtoCartMarkers() {
    document.getElementById("DivCartMarkers").style.display = "block";
}

function AddtoCartPaint() {
    document.getElementById("DivCartPaint").style.display = "block";
}

function AddtoCartResin() {
    document.getElementById("DivCartResin").style.display = "block";
}

function AddtoCartTote() {
    document.getElementById("DivCartTote").style.display = "block";
}

function AddtoCartYarn() {
    document.getElementById("DivCartYarn").style.display = "block";
}

function AddtoCartSewNeedles() {
    document.getElementById("DivCartSewNeedles").style.display = "block";
}

function AddtoCartPaper() {
    document.getElementById("DivCartPaper").style.display = "block";
}
