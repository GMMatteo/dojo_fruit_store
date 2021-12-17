from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    # # fruit request form data
    session['strawberry_qty'] = request.form['strawberry']
    session['raspberry_qty'] = request.form['raspberry']
    session['apple_qty'] = request.form['apple']
    session['blackberry_qty'] = request.form['blackberry']

    # # information request form data
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    count = int(session['strawberry_qty']) + int(session['raspberry_qty']) + int(session['apple_qty']) + int(session['blackberry_qty'])
    session['total'] = count
    print(f"Charging { session['first_name'] } { session['last_name'] } for { count } fruit")
    return render_template("checkout.html", first_name=session['first_name'], last_name=session['last_name'], studentid=session['student_id'], straw=session['strawberry_qty'], rasp=session['raspberry_qty'], apple=session['apple_qty'], bb=session['blackberry_qty'] )

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)