// // static/js/cart.js

// document.addEventListener('DOMContentLoaded', function () {
//     // Select all elements with the 'update-cart' class
//     var updateBtns = document.getElementsByClassName('update-cart');

//     for (var i = 0; i < updateBtns.length; i++) {
//         updateBtns[i].addEventListener('click', function (e) {
//             // Prevent default behavior if attached to an anchor or form submit
//             e.preventDefault();

//             // Using this.dataset grabs attributes from the button element
//             var productId = this.dataset.product;
//             var action = this.dataset.action;

//             console.log('Product ID:', productId, '| Action:', action);
//             console.log('Current User:', user);

//             // Redirect unauthenticated users to the login page
//             if (user === 'AnonymousUser') {
//                 window.location.href = "/auth/login/";
//             } else {
//                 updateUserOrder(productId, action);
//             }
//         });
//     }
// });

// /**
//  * Sends an AJAX request to update the user's cart in Django backend.
//  * 
//  * @param {string|number} productId - The ID of the product being updated.
//  * @param {string} action - Action type: 'add', 'remove', or 'delete'.
//  */
// function updateUserOrder(productId, action) {
//     console.log('User authenticated. Sending cart payload...');

//     // Change endpoint URL if your urls.py uses a different path name
//     var url = '/update_item/'; 

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken, // Global variable defined in base.html
//         },
//         body: JSON.stringify({
//             'productId': productId,
//             'action': action
//         })
//     })
//     .then((response) => {
//         if (!response.ok) {
//             return response.json().then((err) => { throw err; });
//         }
//         return response.json();
//     })
//     .then((data) => {
//         console.log('Cart response:', data);
//         // Refresh page to sync cart count badge and totals
//         location.reload();
//     })
//     .catch((error) => {
//         console.error('Failed to update cart:', error);
//     });
// }