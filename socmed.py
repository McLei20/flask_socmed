from flask import *

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('create.html')

@app.route('/output', methods=['POST', 'GET'])
def output():
    data = request.form
    return render_template('output.html', output=data)



if __name__ == '__main__':
    app.run(debug=True)
