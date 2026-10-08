let cart = [];

let selectedRestaurant = null;

let orders = [];


/* =====================================================
   NAVIGATION
===================================================== */

function showSection(sectionId) {

    document
        .querySelectorAll(".section")
        .forEach(section => {

            section.classList.remove("active");

        });


    const section =
        document.getElementById(sectionId);


    if (section) {

        section.classList.add("active");

    }


    if (sectionId === "restaurants") {

        loadRestaurants();

    }


    if (sectionId === "orders") {

        loadOrders();

    }

}


/* =====================================================
   NOTIFICATION
===================================================== */

function showNotification(message) {

    const notification =
        document.getElementById(
            "notification"
        );


    notification.innerText =
        message;


    notification.style.display =
        "block";


    setTimeout(() => {

        notification.style.display =
            "none";

    }, 3000);

}


/* =====================================================
   RESTAURANTS
===================================================== */

async function loadRestaurants() {

    const container =
        document.getElementById(
            "restaurant-list"
        );


    container.innerHTML =
        '<div class="loading">Loading restaurants...</div>';


    try {

        const response =
            await fetch(
                "/restaurants"
            );


        const restaurants =
            await response.json();


        container.innerHTML = "";


        restaurants.forEach(
            restaurant => {

                const card =
                    document.createElement(
                        "div"
                    );


                card.className =
                    "restaurant-card";


                card.innerHTML = `

                    <div class="restaurant-image">
                        🍽️
                    </div>

                    <h3>
                        ${restaurant.name}
                    </h3>

                    <p>
                        📍 ${restaurant.location}
                    </p>

                    <p>
                        ⭐ ${restaurant.rating || "New"}
                    </p>

                    <button
                        onclick='openRestaurant(
                            ${restaurant.id},
                            ${JSON.stringify(
                                restaurant.name
                            )},
                            ${JSON.stringify(
                                restaurant.location
                            )}
                        )'
                    >
                        View Menu
                    </button>

                `;


                container.appendChild(
                    card
                );

            }
        );

    }

    catch (error) {

        console.error(error);

        container.innerHTML =
            '<div class="empty-state">Unable to load restaurants.</div>';

    }

}


/* =====================================================
   RESTAURANT MENU
===================================================== */

async function openRestaurant(
    restaurantId,
    restaurantName,
    restaurantLocation
) {

    selectedRestaurant =
        restaurantId;


    document.getElementById(
        "restaurant-name"
    ).innerText =
        restaurantName;


    document.getElementById(
        "restaurant-location"
    ).innerText =
        "📍 " + restaurantLocation;


    showSection("menu");


    const container =
        document.getElementById(
            "food-list"
        );


    container.innerHTML =
        '<div class="loading">Loading menu...</div>';


    try {

        const response =
            await fetch(
                `/restaurants/${restaurantId}/foods`
            );


        const foods =
            await response.json();


        container.innerHTML = "";


        foods.forEach(
            food => {

                const card =
                    document.createElement(
                        "div"
                    );


                card.className =
                    "food-card";


                card.innerHTML = `

                    <div class="food-icon">
                        🍛
                    </div>

                    <h3>
                        ${food.name}
                    </h3>

                    <p class="food-category">
                        ${food.category || "Food"}
                    </p>

                    <div class="food-price">
                        ₹${food.price}
                    </div>

                    <button
                        onclick='openCustomization(
                            ${JSON.stringify(food)}
                        )'
                    >
                        Customize & Add
                    </button>

                `;


                container.appendChild(
                    card
                );

            }
        );

    }

    catch (error) {

        console.error(error);

    }

}


/* =====================================================
   DISH-SPECIFIC CUSTOMIZATION
===================================================== */

async function openCustomization(food) {

    try {

        const response =
            await fetch(
                `/food/customize/options?name=${encodeURIComponent(
                    food.name
                )}&category=${encodeURIComponent(
                    food.category || ""
                )}`
            );


        const result =
            await response.json();


        createCustomizationModal(
            food,
            result.options
        );

    }

    catch (error) {

        console.error(error);

        showNotification(
            "Unable to load customization options"
        );

    }

}


function createCustomizationModal(
    food,
    options
) {

    closeCustomization();


    const modal =
        document.createElement(
            "div"
        );


    modal.id =
        "customization-modal";


    modal.style.position =
        "fixed";

    modal.style.top =
        "0";

    modal.style.left =
        "0";

    modal.style.width =
        "100%";

    modal.style.height =
        "100%";

    modal.style.background =
        "rgba(0,0,0,0.55)";

    modal.style.display =
        "flex";

    modal.style.alignItems =
        "center";

    modal.style.justifyContent =
        "center";

    modal.style.zIndex =
        "500";


    let optionsHTML = "";


    options.forEach(
        option => {

            optionsHTML += `

                <label style="
                    display:block;
                    padding:14px 0;
                    cursor:pointer;
                ">

                    <input
                        type="checkbox"
                        class="extra-option"
                        value="${option.id}"
                    >

                    ${option.name}

                    <strong>
                        +₹${option.price}
                    </strong>

                </label>

            `;

        }
    );


    modal.innerHTML = `

        <div style="
            background:white;
            width:90%;
            max-width:500px;
            border-radius:18px;
            padding:30px;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
            ">

                <h2>
                    Customize ${food.name}
                </h2>

                <button
                    onclick="closeCustomization()"
                    style="
                        border:none;
                        background:none;
                        font-size:24px;
                        cursor:pointer;
                    "
                >
                    ×
                </button>

            </div>


            <p style="
                color:#777;
                margin:15px 0;
            ">

                Base Price:
                <strong>
                    ₹${food.price}
                </strong>

            </p>


            <h3>
                Available Extras
            </h3>


            ${optionsHTML}


            <div style="
                margin-top:15px;
                padding:15px;
                background:#f5f5f5;
                border-radius:10px;
            ">

                <strong>
                    Final Price:
                </strong>

                <span
                    id="custom-price"
                    style="float:right"
                >
                    ₹${food.price}
                </span>

            </div>


            <button
                id="custom-add-button"
                style="
                    width:100%;
                    margin-top:20px;
                    padding:14px;
                    border:none;
                    background:#111;
                    color:white;
                    border-radius:9px;
                    cursor:pointer;
                    font-size:16px;
                    font-weight:bold;
                "
            >
                Add to Cart
            </button>

        </div>

    `;


    document.body.appendChild(
        modal
    );


    document
        .querySelectorAll(
            ".extra-option"
        )
        .forEach(option => {

            option.addEventListener(
                "change",
                () => {

                    let total =
                        Number(
                            food.price
                        );


                    document
                        .querySelectorAll(
                            ".extra-option:checked"
                        )
                        .forEach(
                            selected => {

                                const selectedOption =
                                    options.find(
                                        item =>
                                            item.id ===
                                            selected.value
                                    );


                                if (
                                    selectedOption
                                ) {

                                    total +=
                                        Number(
                                            selectedOption.price
                                        );

                                }

                            }
                        );


                    document.getElementById(
                        "custom-price"
                    ).innerText =
                        "₹" + total;

                }
            );

        });


    document.getElementById(
        "custom-add-button"
    ).onclick = () => {

        addCustomizedFood(
            food,
            options
        );

    };

}


async function addCustomizedFood(
    food,
    options
) {

    const selectedExtras =
        Array.from(
            document.querySelectorAll(
                ".extra-option:checked"
            )
        ).map(
            option =>
                option.value
        );


    try {

        const response =
            await fetch(
                "/food/customize",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            name:
                                food.name,

                            price:
                                food.price,

                            category:
                                food.category,

                            extras:
                                selectedExtras

                        })

                }
            );


        const result =
            await response.json();


        if (!response.ok) {

            showNotification(
                result.error
            );

            return;

        }


        const existing =
            cart.find(
                item =>
                    item.id === food.id &&
                    JSON.stringify(
                        item.extras
                    ) ===
                    JSON.stringify(
                        selectedExtras
                    )
            );


        if (existing) {

            existing.quantity++;

        }

        else {

            cart.push({

                id:
                    food.id,

                name:
                    result.food_name,

                price:
                    result.final_price,

                quantity:
                    1,

                extras:
                    selectedExtras

            });

        }


        updateCartCount();

        closeCustomization();


        showNotification(
            `${result.food_name} added to cart`
        );

    }

    catch (error) {

        console.error(error);

        showNotification(
            "Unable to customize food"
        );

    }

}


function closeCustomization() {

    const modal =
        document.getElementById(
            "customization-modal"
        );


    if (modal) {

        modal.remove();

    }

}


/* =====================================================
   CART
===================================================== */

function updateCartCount() {

    const count =
        cart.reduce(
            (total, item) =>
                total +
                item.quantity,
            0
        );


    document.getElementById(
        "cart-count"
    ).innerText =
        count;

}


function showCart() {

    showSection("cart");

    renderCart();

}


function renderCart() {

    const container =
        document.getElementById(
            "cart-items"
        );


    const summary =
        document.getElementById(
            "cart-summary"
        );


    if (cart.length === 0) {

        container.innerHTML = `

            <div class="empty-state">

                <div>🛒</div>

                <p>
                    Your cart is empty.
                </p>

            </div>

        `;

        summary.innerHTML = "";

        return;

    }


    container.innerHTML = "";


    let total = 0;


    cart.forEach(
        (item, index) => {

            const itemTotal =
                item.price *
                item.quantity;


            total += itemTotal;


            let extras =
                "No extras";


            if (
                item.extras &&
                item.extras.length
            ) {

                extras =
                    item.extras.join(
                        ", "
                    );

            }


            const div =
                document.createElement(
                    "div"
                );


            div.className =
                "cart-item";


            div.innerHTML = `

                <div>

                    <h3>
                        ${item.name}
                    </h3>

                    <p>
                        ₹${item.price}
                        × ${item.quantity}
                    </p>

                    <small>
                        ${extras}
                    </small>

                </div>


                <div class="quantity-controls">

                    <button
                        onclick="changeQuantity(
                            ${index},
                            -1
                        )"
                    >
                        -
                    </button>

                    <span>
                        ${item.quantity}
                    </span>

                    <button
                        onclick="changeQuantity(
                            ${index},
                            1
                        )"
                    >
                        +
                    </button>

                </div>


                <strong>
                    ₹${itemTotal}
                </strong>

            `;


            container.appendChild(
                div
            );

        }
    );


    summary.innerHTML = `

        <div class="cart-summary-row">

            <span>
                Food Total
            </span>

            <strong>
                ₹${total}
            </strong>

        </div>


        <button
            class="checkout-btn"
            onclick="openCheckout()"
        >
            Proceed to Checkout
        </button>

    `;

}


function changeQuantity(
    index,
    change
) {

    cart[index].quantity +=
        change;


    if (
        cart[index].quantity <= 0
    ) {

        cart.splice(
            index,
            1
        );

    }


    updateCartCount();

    renderCart();

}


/* =====================================================
   CHECKOUT
===================================================== */

function getDeliveryCharge(
    deliveryType
) {

    const distance = 5;


    if (
        deliveryType ===
        "normal"
    ) {

        return 50;

    }


    if (
        deliveryType ===
        "express"
    ) {

        return 90;

    }


    if (
        deliveryType ===
        "premium"
    ) {

        return 140;

    }


    return 0;

}


function openCheckout() {

    if (cart.length === 0) {

        showNotification(
            "Your cart is empty"
        );

        return;

    }


    showSection(
        "checkout"
    );


    const container =
        document.getElementById(
            "checkout-items"
        );


    let total = 0;


    container.innerHTML = "";


    cart.forEach(
        item => {

            const itemTotal =
                item.price *
                item.quantity;


            total +=
                itemTotal;


            container.innerHTML += `

                <div class="cart-summary-row">

                    <span>
                        ${item.name}
                        × ${item.quantity}
                    </span>

                    <span>
                        ₹${itemTotal}
                    </span>

                </div>

            `;

        }
    );


    document.getElementById(
        "checkout-food-total"
    ).innerText =
        "₹" + total;


    updateDeliverySummary();


    document
        .querySelectorAll(
            'input[name="delivery"]'
        )
        .forEach(
            radio => {

                radio.onchange =
                    updateDeliverySummary;

            }
        );

}


function updateDeliverySummary() {

    const selected =
        document.querySelector(
            'input[name="delivery"]:checked'
        );


    if (!selected) {

        return;

    }


    const delivery =
        selected.value;


    const deliveryCharge =
        getDeliveryCharge(
            delivery
        );


    const foodTotal =
        cart.reduce(
            (total, item) =>
                total +
                item.price *
                item.quantity,
            0
        );


    const finalTotal =
        foodTotal +
        deliveryCharge;


    const checkoutCards =
        document.querySelectorAll(
            ".checkout-card"
        );


    if (
        checkoutCards.length <
        2
    ) {

        return;

    }


    let summary =
        document.getElementById(
            "delivery-summary"
        );


    if (!summary) {

        summary =
            document.createElement(
                "div"
            );


        summary.id =
            "delivery-summary";


        summary.style.marginTop =
            "20px";


        summary.style.padding =
            "15px";


        summary.style.background =
            "#f5f5f5";


        summary.style.borderRadius =
            "10px";


        checkoutCards[1]
            .appendChild(
                summary
            );

    }


    summary.innerHTML = `

        <div style="
            display:flex;
            justify-content:space-between;
        ">

            <span>
                Delivery Charge
            </span>

            <strong>
                ₹${deliveryCharge}
            </strong>

        </div>


        <div style="
            display:flex;
            justify-content:space-between;
            margin-top:10px;
            font-size:18px;
        ">

            <strong>
                Final Total
            </strong>

            <strong>
                ₹${finalTotal}
            </strong>

        </div>

    `;

}


/* =====================================================
   PLACE ORDER
===================================================== */

async function placeOrder() {

    const delivery =
        document.querySelector(
            'input[name="delivery"]:checked'
        ).value;


    const payment =
        document.querySelector(
            'input[name="payment"]:checked'
        ).value;


    const items =
        cart.map(
            item => ({

                food_id:
                    item.id,

                quantity:
                    item.quantity,

                price:
                    item.price

            })
        );


    try {

        const response =
            await fetch(
                "/orders/place",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            customer_id:
                                1,

                            restaurant_id:
                                selectedRestaurant,

                            order_type:
                                "normal",

                            items:
                                items,

                            delivery_type:
                                delivery,

                            distance:
                                5,

                            payment_method:
                                payment

                        })

                }
            );


        const result =
            await response.json();


        if (!response.ok) {

            showNotification(
                result.error ||
                "Order failed"
            );

            return;

        }


        orders.push(
            result
        );


        cart = [];


        updateCartCount();


        showNotification(
            "✅ Order placed successfully!"
        );


        setTimeout(
            () => {

                showSection(
                    "orders"
                );

                loadOrders();

            },
            800
        );

    }

    catch (error) {

        console.error(error);

        showNotification(
            "Unable to place order"
        );

    }

}


/* =====================================================
   CUSTOMER ORDERS
===================================================== */

function loadOrders() {

    const container =
        document.getElementById(
            "order-list"
        );


    if (orders.length === 0) {

        container.innerHTML = `

            <div class="empty-state">

                <div>
                    📦
                </div>

                <p>
                    No orders yet.
                </p>

            </div>

        `;

        return;

    }


    container.innerHTML = "";


    orders.forEach(
        order => {

            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "order-card";


            card.innerHTML = `

                <div class="order-header">

                    <strong>
                        Order #${order.order_id}
                    </strong>

                    <span
                        class="status"
                        id="status-${order.order_id}"
                    >
                        ${order.status}
                    </span>

                </div>


                <p>
                    Food Amount:
                    ₹${order.food_amount}
                </p>


                <p>
                    Delivery:
                    ₹${order.delivery_charge}
                </p>


                <p>
                    Total:
                    <strong>
                        ₹${order.total_amount}
                    </strong>
                </p>


                <button
                    class="track-btn"
                    onclick="trackOrder(
                        ${order.order_id}
                    )"
                >
                    Track Order
                </button>

            `;


            container.appendChild(
                card
            );

        }
    );

}


/* =====================================================
   CUSTOMER TRACKING
   READ ONLY
===================================================== */

async function trackOrder(
    orderId
) {

    try {

        const response =
            await fetch(
                `/orders/${orderId}/status`
            );


        const result =
            await response.json();


        if (!response.ok) {

            showNotification(
                "Unable to get order status"
            );

            return;

        }


        const secureResponse =
            await fetch(
                `/orders/${orderId}/secure?customer_id=1`
            );


        const secureOrder =
            await secureResponse.json();


        showTrackingModal(
            secureOrder,
            result.status
        );

    }

    catch (error) {

        console.error(error);

        showNotification(
            "Unable to track order"
        );

    }

}


/* =====================================================
   READ-ONLY TRACKING MODAL
===================================================== */

function showTrackingModal(
    order,
    status
) {

    closeTrackingModal();


    const states = [

        "PLACED",

        "ACCEPTED",

        "PREPARING",

        "READY",

        "OUT_FOR_DELIVERY",

        "DELIVERED"

    ];


    const currentIndex =
        states.indexOf(
            status
        );


    let stateHTML = "";


    states.forEach(
        (state, index) => {

            let symbol = "○";


            if (
                index <
                currentIndex
            ) {

                symbol = "✓";

            }


            if (
                index ===
                currentIndex
            ) {

                symbol = "●";

            }


            stateHTML += `

                <div style="
                    display:flex;
                    gap:12px;
                    align-items:center;
                    margin:14px 0;
                    font-weight:${
                        index === currentIndex
                        ? "bold"
                        : "normal"
                    };
                ">

                    <span>
                        ${symbol}
                    </span>

                    <span>
                        ${formatStatus(
                            state
                        )}
                    </span>

                </div>

            `;

        }
    );


    const modal =
        document.createElement(
            "div"
        );


    modal.id =
        "tracking-modal";


    modal.style.position =
        "fixed";

    modal.style.top =
        "0";

    modal.style.left =
        "0";

    modal.style.width =
        "100%";

    modal.style.height =
        "100%";

    modal.style.background =
        "rgba(0,0,0,0.55)";

    modal.style.display =
        "flex";

    modal.style.alignItems =
        "center";

    modal.style.justifyContent =
        "center";

    modal.style.zIndex =
        "500";


    modal.innerHTML = `

        <div style="
            background:white;
            width:90%;
            max-width:600px;
            border-radius:18px;
            padding:30px;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
            ">

                <h2>
                    📦 Order #${order.order_id}
                </h2>

                <button
                    onclick="closeTrackingModal()"
                    style="
                        border:none;
                        background:none;
                        font-size:24px;
                        cursor:pointer;
                    "
                >
                    ×
                </button>

            </div>


            <p style="
                color:#777;
                margin:10px 0 20px;
            ">

                Current Status:

                <strong>
                    ${formatStatus(
                        status
                    )}
                </strong>

            </p>


            <div style="
                background:#f5f5f5;
                padding:20px;
                border-radius:12px;
            ">

                <h3>
                    Order Progress
                </h3>

                ${stateHTML}

            </div>


            <div style="
                display:flex;
                justify-content:space-between;
                margin-top:25px;
                font-size:18px;
            ">

                <span>
                    Total Amount
                </span>

                <strong>
                    ₹${order.total_amount}
                </strong>

            </div>


            <div style="
                margin-top:20px;
                padding:12px;
                background:#f5f5f5;
                border-radius:8px;
                text-align:center;
                color:#666;
            ">

                🔔 Order status is updated
                by the restaurant.

            </div>


            <button
                onclick="refreshTracking(
                    ${order.order_id}
                )"
                style="
                    width:100%;
                    margin-top:15px;
                    padding:13px;
                    border:none;
                    background:#111;
                    color:white;
                    border-radius:8px;
                    cursor:pointer;
                    font-weight:bold;
                "
            >
                Refresh Status
            </button>

        </div>

    `;


    document.body.appendChild(
        modal
    );

}


async function refreshTracking(
    orderId
) {

    closeTrackingModal();

    await trackOrder(
        orderId
    );

}


function formatStatus(
    status
) {

    return status
        .replaceAll(
            "_",
            " "
        )
        .toLowerCase()
        .replace(
            /\b\w/g,
            char =>
                char.toUpperCase()
        );

}


function closeTrackingModal() {

    const modal =
        document.getElementById(
            "tracking-modal"
        );


    if (modal) {

        modal.remove();

    }

}


/* =====================================================
   START
===================================================== */

showSection(
    "home"
);

updateCartCount();