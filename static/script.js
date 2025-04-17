document.addEventListener("DOMContentLoaded", function () {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    
    function addToCart(productName, price) {
        cart.push({ name: productName, price: price });
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCartUI();
    }
    
    function updateCartUI() {
        const cartList = document.getElementById("cart-items");
        const totalAmount = document.getElementById("total-amount");
        cartList.innerHTML = "";
        let total = 0;

        cart.forEach((item, index) => {
            let listItem = document.createElement("li");
            listItem.textContent = `${item.name} - $${item.price}`;
            let removeBtn = document.createElement("button");
            removeBtn.textContent = "Remove";
            removeBtn.onclick = function () { removeFromCart(index); };
            listItem.appendChild(removeBtn);
            cartList.appendChild(listItem);
            total += parseFloat(item.price);
        });

        totalAmount.textContent = `Total: $${total.toFixed(2)}`;
    }

    function removeFromCart(index) {
        cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(cart));
        updateCartUI();
    }
    
    window.addToCart = addToCart;
    window.removeFromCart = removeFromCart;

    function fetchRecommendations() {
        const recommendationList = document.getElementById("recommendation-list");
        
        fetch("https://fakestoreapi.com/products?limit=3")
            .then(response => response.json())
            .then(data => {
                recommendationList.innerHTML = "";
                data.forEach(product => {
                    let item = document.createElement("div");
                    item.classList.add("product");
                    item.innerHTML = `
                        <img src="${product.image}" alt="${product.title}" width="100">
                        <h3>${product.title}</h3>
                        <p>$${product.price}</p>
                        <button onclick="addToCart('${product.title}', '${product.price}')">Add to Cart</button>
                    `;
                    recommendationList.appendChild(item);
                });
            })
            .catch(error => console.error("Error fetching recommendations:", error));
    }
    
    function handleUserAuth() {
        const user = JSON.parse(localStorage.getItem("user"));
        const authStatus = document.getElementById("auth-status");

        if (user) {
            authStatus.innerHTML = `Welcome, ${user.username} | <button onclick="logout()">Logout</button>`;
        } else {
            authStatus.innerHTML = `<a href="login.html">Login</a> | <a href="register.html">Register</a>`;
        }
    }
    
    function logout() {
        localStorage.removeItem("user");
        window.location.reload();
    }
    
    window.logout = logout;
    handleUserAuth();
    fetchRecommendations();
    updateCartUI();
});