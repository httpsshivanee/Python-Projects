from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)

# Store prices as integers
menu = {
    'PIZZA': 100,
    'BURGER(VEG)': 150,
    'BURGER(NON-VEG)': 180,
    'MOMOS': 80,
    'COLDCOFFEE': 90,
    'TEA': 20
}

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        selected_items = request.form.getlist('items')
        total_price = 0
        valid_items = []

        if selected_items:
            for item in selected_items:
                item_upper = item.upper()
                if item_upper in menu:
                    total_price += menu[item_upper]
                    valid_items.append(item_upper)

            return render_template('order.html', item=valid_items, price=total_price, menu=menu)
        else:
            return render_template('order.html', item=[], price=0, menu=menu)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

@app.route('/some_route')
def some_function():
    menu = ...  # Fetch your menu
    logging.debug(f"Menu: {menu}")  # Log the menu value
    return render_template('your_template.html', menu=menu)
