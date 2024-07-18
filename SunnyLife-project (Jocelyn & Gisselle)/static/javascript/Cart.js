window.addEventListener("load", Initial);
window.addEventListener("load", EventListener);

var YorNCanvas = 0;
var YorNGelPens = 0;
var YorNGlue = 0;
var YorNMarkers = 0;
var YorNPaint = 0;
var YorNResin = 0;
var YorNTote = 0;
var YorNYarn = 0;
var YorNSewNeedles = 0;
var YorNPaper = 0;
var CartIconQty = document.getElementById("CartIconQty").value;

function Initial() 
{
    YnN();
}

function EventListener() 
{
    document.getElementById("btnCartCanvas").addEventListener("click", AddtoCartCanvas);
    document.getElementById("btnCartGelPens").addEventListener("click", AddtoCartGelPens);
    document.getElementById("btnCartGlue").addEventListener("click", AddtoCartGlue);
    document.getElementById("btnCartMarkers").addEventListener("click", AddtoCartMarkers);
    document.getElementById("btnCartPaint").addEventListener("click", AddtoCartPaint);
    document.getElementById("btnCartResin").addEventListener("click", AddtoCartResin);
    document.getElementById("btnCartSewNeedles").addEventListener("click", AddtoCartSewNeedles);
    document.getElementById("btnCartTote").addEventListener("click", AddtoCartTote);
    document.getElementById("btnCartYarn").addEventListener("click", AddtoCartYarn);
    
    
    document.getElementById("btnRemoveCanvas").addEventListener("click", RemoveCartCanvas);
    document.getElementById("btnRemoveGelPens").addEventListener("click", RemoveCartGelPens);
    document.getElementById("btnRemoveGlue").addEventListener("click", RemoveCartGlue);
    document.getElementById("btnRemoveMarkers").addEventListener("click", RemoveCartMarkers);
    document.getElementById("btnRemovePaint").addEventListener("click", RemoveCartPaint);
    document.getElementById("btnRemoveResin").addEventListener("click", RemoveCartResin);
    document.getElementById("btnRemoveSewNeedles").addEventListener("click", RemoveCartSewNeedles);
    document.getElementById("btnRemoveTote").addEventListener("click", RemoveCartTote);
    document.getElementById("btnRemoveYarn").addEventListener("click", RemoveCartYarn);
    
    
    document.getElementById("btnShowInfo").addEventListener("click", Exit);
}

function Exit() 
{
    document.getElementById("DivCartCanvas").style.display = "none";
    document.getElementById("DivCartGelPens").style.display = "none";
    document.getElementById("DivCartGlue").style.display = "none";
    document.getElementById("DivCartMarkers").style.display = "none";
    document.getElementById("DivCartPaint").style.display = "none";
    document.getElementById("DivCartResin").style.display = "none";
    document.getElementById("DivCartTote").style.display = "none";
    document.getElementById("DivCartYarn").style.display = "none";
    document.getElementById("DivCartSewNeedles").style.display = "none";
    document.getElementById("DivCartPaper").style.display = "none";
}

function YnN() 
{
    document.getElementById("DivCartCanvas").style.display = YorNCanvas ? "block" : "none";
    document.getElementById("DivCartGelPens").style.display = YorNGelPens ? "block" : "none";
    document.getElementById("DivCartGlue").style.display = YorNGlue ? "block" : "none";
    document.getElementById("DivCartMarkers").style.display = YorNMarkers ? "block" : "none";
    document.getElementById("DivCartPaint").style.display = YorNPaint ? "block" : "none";
    document.getElementById("DivCartResin").style.display = YorNResin ? "block" : "none";
    document.getElementById("DivCartTote").style.display = YorNTote ? "block" : "none";
    document.getElementById("DivCartYarn").style.display = YorNYarn ? "block" : "none";
    document.getElementById("DivCartSewNeedles").style.display = YorNSewNeedles ? "block" : "none";
    document.getElementById("DivCartPaper").style.display = YorNPaper ? "block" : "none";
}

function RemoveCartCanvas() 
{
    YorNCanvas = 0;
    YnN();
}
function RemoveCartGelPens() 
{
    YorNGelPens = 0;
    YnN();
}

function RemoveCartGlue() 
{
    YorNGlue = 0;
    YnN();
}

function RemoveCartMarkers() 
{
    YorNMarkers = 0;
    YnN();
}

function RemoveCartPaint() 
{
    YorNPaint = 0;
    YnN();
}
function RemoveCartResin() 
{
    YorNResin = 0;
    YnN();
}

function RemoveCartTote() 
{
    YorNTote = 0;
    YnN();
}

function RemoveCartYarn() 
{
    YorNYarn = 0;
    YnN();
}
function RemoveCartSewNeedles() 
{
    YorNSewNeedles = 0;
    YnN();
}

function RemoveCartPaper() 
{
    YorNPaper = 0;
    YnN();
}

function AddtoCartCanvas() 
{
    YorNCanvas = 1;
    CartIconQty++;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartCanvas() 
{
	var YorNCanvas
	YorNCanvas = 1 
	CartIconQty += 1 
	document.getElementById("CartIconQty").innerHTML = CartIconQty
	YnN();
}

function AddtoCartGelPens() 
{
    YorNGelPens = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartGlue() 
{
    YorNGlue = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartMarkers() {
    YorNMarkers = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartPaint() {
    YorNPaint = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartResin() {
    YorNResin = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartTote() {
    YorNTote = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartYarn() {
    YorNYarn = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartSewNeedles() {
    YorNSewNeedles = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

function AddtoCartPaper() {
    YorNPaper = 1;
    CartIconQty += 1;
    document.getElementById("CartIconQty").innerHTML = CartIconQty;
    YnN();
}

