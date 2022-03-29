// Code for Strip implementation
var publicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(publicKey);
var elements = stripe.elements();
var card = elements.create('card', {style: style});
    card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        $(errorDiv).html(
            `<div class="stripe-error" role="alert">
                <p>
                    <i class="fas fa-times"></i> ${event.error.message}
                </p>
            </div>`
        );
    } else {
        errorDiv.textContent = '';
    }
});
