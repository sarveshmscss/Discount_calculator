from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            discount = float(request.form['discount'])
            total = price * quantity
            discount_amount = total * (discount / 100)
            final_amount = total - discount_amount
            result = {
                "total": total,
                "discount_amount": discount_amount,
                "final_amount": final_amount
            }
        except ValueError:
            result = {"error": "Invalid input. Please enter valid numbers."}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
