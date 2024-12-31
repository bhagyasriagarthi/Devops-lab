from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong key for security

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        phone_number = request.form.get('phone-number')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        gender = request.form.get('gender')

        # Validation example: Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        # Placeholder for saving user data to a database
        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('Registrationform.html')

if __name__ == "__main__":
    app.run(debug=True)
