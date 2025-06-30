from flask import Flask, render_template, request, redirect, url_for
import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        return "✅ Login berhasil dengan email: " + email
    return render_template('login.html')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
