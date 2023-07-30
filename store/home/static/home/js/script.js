document.addEventListener('DOMContentLoaded', function () {
    const addToCartForm = document.querySelector('#form_add_to_cart');

    addToCartForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const cartInfo = addToCartForm.querySelector('.cart-info');
        addToCartForm.classList.add('submitted');
        cartInfo.style.display = 'block';

        setTimeout(function () {
            addToCartForm.submit();
        }, 1000);
    });
});