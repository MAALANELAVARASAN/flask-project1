from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    hobbies=["Football","Badminton","Cricket","Gaming","Movies"]
    return render_template("index.html",hobbies=hobbies)

@app.route('/')
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/')
@app.route('/contact')
def contact():
    return render_template("contact.html")



@app.route('/')
@app.route('/others')
def others():
    return render_template("others.html")


if __name__=='__main__':
    app.run(debug=True)   