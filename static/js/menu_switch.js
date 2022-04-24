document.addEventListener("DOMContentLoaded", function () {
    //hides javascript error if javascript is running
    document.getElementById("support").style.display = "none";
    init();
});


function init(){

    switchDisplay('overviewDisplay','overview');

    let btnOverview = document.getElementById("overview")
    let btnRequestList = document.getElementById("requestList")
    let btnPurchaseHistory = document.getElementById("purchaseHistory")
    let btnContactInquiries = document.getElementById("contactInquiries")
    let btnProducts = document.getElementById("products")

    btnOverview.addEventListener("click", function(){
        switchDisplay('overviewDisplay','overview');
    });
    btnRequestList.addEventListener("click", function(){
        switchDisplay('requestListDisplay','requestList');
    });

    btnPurchaseHistory.addEventListener("click", function(){
        switchDisplay('purchaseHistoryDisplay','purchaseHistory');
    });

    btnContactInquiries.addEventListener("click", function(){
        switchDisplay('ContactInquiriesDisplay','contactInquiries');
    });

    btnProducts.addEventListener("click", function(){
        switchDisplay('productsDisplay','products');
    });

}
/**
 * Changes which style.display and block should be shown from the input
 * 
 * @param {string} displayBlock id
 * @param {string} button id
 */
 function switchDisplay(displayBlock, button) {
    document.getElementById("overviewDisplay").style.display = "none";
    document.getElementById("requestListDisplay").style.display = "none";
    document.getElementById("purchaseHistoryDisplay").style.display = "none";
    document.getElementById("ContactInquiriesDisplay").style.display = "none";
    document.getElementById("productsDisplay").style.display = "none";
    document.getElementById(displayBlock).style.display = "flex";

    document.getElementById('overview').classList.remove('ap-menu-sel');
    document.getElementById('requestList').classList.remove('ap-menu-sel');
    document.getElementById('purchaseHistory').classList.remove('ap-menu-sel');
    document.getElementById('contactInquiries').classList.remove('ap-menu-sel');
    document.getElementById('products').classList.remove('ap-menu-sel');
    document.getElementById(button).classList.add('ap-menu-sel');
}