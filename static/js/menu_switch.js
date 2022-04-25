document.addEventListener("DOMContentLoaded", function () {
    init();
});


function init(){
    let switchKeepMe = document.getElementById('keepMeOnRightPage').innerText;
    switchDisplay(switchKeepMe);
    switchKeepMe = document.getElementById('keepMeOnRightPage').remove();
}
/**
 * Changes which button should be highlighted
 * 
 * @param {string} button id
 */
 function switchDisplay(button) {
    document.getElementById('overview').classList.remove('ap-menu-sel');
    document.getElementById('requestList').classList.remove('ap-menu-sel');
    document.getElementById('purchaseHistory').classList.remove('ap-menu-sel');
    document.getElementById('contactInquiries').classList.remove('ap-menu-sel');
    document.getElementById('products').classList.remove('ap-menu-sel');
    document.getElementById(button).classList.add('ap-menu-sel');
}