from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        return render_template('profile.html', name=name, email=email, phone=phone)
    
    # If request method is GET, render the registration form
    return render_template('register.html')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
