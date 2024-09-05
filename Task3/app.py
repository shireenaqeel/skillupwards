from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from the form
    user_input = request.form['user_input']
    return render_template('result.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
