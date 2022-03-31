// Code for Stripe implementation
var publicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(publicKey);
var elements = stripe.elements();
var card = elements.create('card');
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

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);

    var django_token = $('input[name="csrfmiddlewaretoken"]').val();
    var imageCheckData = {
        'csrfmiddlewaretoken': django_token,
        'client_secret': clientSecret,
    };

    var url = '/checkout/image_checkout_data/'

    $.post(url, imageCheckData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.first_name.value + ' ' + form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email_address.value)
                }
            }
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                $(errorDiv).html(
                    `<div class="stripe-error" role="alert">
                    <p>
                        <i class="fas fa-times"></i> ${result.error.message}
                    </p>
                </div>`
                );
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                   form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    })
});