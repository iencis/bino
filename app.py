from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main_page():
    return render_template('index.html')



@app.route('/makers', methods=["GET", "POST"])
def makers_page():
    return render_template('makers.html')

@app.route('/meat', methods=["GET", "POST"])
def et_page():
    return render_template('et.html')



@app.route('/milk', methods=["GET", "POST"])
def milk_page():
    return render_template('syt.html')


@app.route('/crafts', methods=["GET", "POST"])
def crafts_page():
    return render_template('crafts.html')

@app.route('/astik', methods=["GET", "POST"])
def astyk_page():
    return render_template('astik.html')



@app.route('/meat1', methods=["GET", "POST"])
def et_page1():
    return render_template('et1.html')

@app.route('/meat2', methods=["GET", "POST"])
def et_page2():
    return render_template('et2.html')

@app.route('/meat3', methods=["GET", "POST"])
def et_page3():
    return render_template('et3.html')

@app.route('/meat4', methods=["GET", "POST"])
def et_page4():
    return render_template('et4.html')


@app.route('/i1', methods=["GET", "POST"])
def makers_page1():
    return render_template('ondu.html')
@app.route('/i2', methods=["GET", "POST"])
def makers_page2():
    return render_template('ondu1.html')
@app.route('/i3', methods=["GET", "POST"])
def makers_page3():
    return render_template('ondu2.html')
@app.route('/i4', methods=["GET", "POST"])
def makers_page4():
    return render_template('ondu3.html')
@app.route('/i5', methods=["GET", "POST"])
def makers_page5():
    return render_template('ondu4.html')
@app.route('/i6', methods=["GET", "POST"])
def makers_page6():
    return render_template('ondu5.html')

if __name__ == '__main__':
    app.run(debug=True)


# Python script for website functionality
def main():
    print("This is a Python script for the website.")

if __name__ == "__main__":
    main()



