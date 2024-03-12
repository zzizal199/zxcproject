from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button1')
def button1_clicked():
    return 'Button 1 Clicked!'

@app.route('/button2')
def button2_clicked():
    return 'Button 2 Clicked!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


