from flask import Flask, render_template, request

app = Flask(__name__)

# Route to render the form
@app.route('/create_profile', methods=['GET'])
def show_form():
    return render_template('form.html')

# Route to handle form submission and generate output
@app.route('/generate_output', methods=['POST'])
def generate_output():
    # Get form data
    first_name = request.form.get('first_name', 'Not provided')
    last_name = request.form.get('last_name', 'Not provided')
    sex = request.form.get('sex', 'Not provided')
    status = request.form.get('status', 'Not provided')
    location = request.form.get('location', 'Not provided')

    # Render the output template with the data
    return render_template(
        'output.html',
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        status=status,
        location=location
    )

if __name__ == '__main__':
    app.run(debug=True)
