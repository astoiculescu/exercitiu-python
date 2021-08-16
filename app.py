from flask import Flask, render_template, url_for, request

#app = Flask(__name__, template_folder='templates/')
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('/index.html')

@app.route('/<string:page_name>')
def html_name(page_name):
    if('.html' not in page_name):
        return render_template(page_name + '.html')
    else:
        return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted succesfully!'
