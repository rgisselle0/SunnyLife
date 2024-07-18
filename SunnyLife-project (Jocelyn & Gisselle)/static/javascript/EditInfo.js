window.addEventListener("load", Initial);
window.addEventListener("load", addListener);

function Initial() 
{
    document.getElementById("divEditName").style.display = "none";
    document.getElementById("divEditShipping").style.display = "none";
    document.getElementById("divEditBilling").style.display = "none";
    document.getElementById("divEditCard").style.display = "none";
}

function addListener() 
{
    document.getElementById("btnEditName").addEventListener("click", EditName);
    document.getElementById("btnEditShipping").addEventListener("click", EditShipping);
    document.getElementById("btnEditBilling").addEventListener("click", EditBilling);
    document.getElementById("btnEditCard").addEventListener("click", EditCard);
	
}

function EditName() 
{
    document.getElementById("divEditName").style.display = "block";
}

function EditShipping() 
{
    document.getElementById("divEditShipping").style.display = "block";
}

function EditBilling() 
{
    document.getElementById("divEditBilling").style.display = "block";
}

function EditCard() 
{
    document.getElementById("divEditCard").style.display = "block";
}