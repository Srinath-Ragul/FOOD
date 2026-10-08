from flask import Flask, render_template

from database import create_tables


from controllers.customer_controller import (
    customer_controller
)

from controllers.restaurant_controller import (
    restaurant_controller
)

from controllers.food_controller import (
    food_controller
)

from controllers.order_controller import (
    order_controller
)

from controllers.order_state_controller import (
    order_state_controller
)

from controllers.payment_controller import (
    payment_controller
)

from controllers.food_customization_controller import (
    food_customization_controller
)

from controllers.order_facade_controller import (
    order_facade_controller
)

from controllers.order_proxy_controller import (
    order_proxy_controller
)

from controllers.admin_controller import (
    admin_controller
)


app = Flask(__name__)


app.register_blueprint(
    customer_controller
)

app.register_blueprint(
    restaurant_controller
)

app.register_blueprint(
    food_controller
)

app.register_blueprint(
    order_controller
)

app.register_blueprint(
    order_state_controller
)

app.register_blueprint(
    payment_controller
)

app.register_blueprint(
    food_customization_controller
)

app.register_blueprint(
    order_facade_controller
)

app.register_blueprint(
    order_proxy_controller
)

app.register_blueprint(
    admin_controller
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


if __name__ == "__main__":

    create_tables()

    app.run(
        debug=True
    )