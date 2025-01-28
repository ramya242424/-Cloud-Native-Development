import os
from flask import Flask, redirect, request, send_file, render_template, session
import time
import re

from storage import download_file, getImages, uploadImage

os.makedirs('files', exist_ok=True)

app = Flask(__name__)
app.secret_key = 'jO=5RWaU|nZN9S:P' 

@app.route('/', methods=["GET", "POST"])
def index():
    email = session.get('email')

    if request.method == "POST":
        if 'email' in request.form:
            email = request.form['email']
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
            if not re.match(email_pattern, email):
                return "Invalid email format. Please enter a valid email.", 400
            
            session['email'] = email
        elif 'form_file' in request.files:
            file = request.files['form_file']
            
            if not email:
                return redirect('/')
    
            time_stamp = int(time.time())
            filename = f"{time_stamp}_{file.filename}"
            file.save(os.path.join("./files", filename))
            uploadImage(filename, email, time_stamp)
    
            return redirect("/")

    files = list_files(email) if email else []
    return render_template('index.html', files=files, email=email)

@app.route('/files/<filename>')
def get_file(filename):
    return send_file('./files/' + filename)

def list_files(email):
    if not email:
        return []
    
    images = getImages(email)
    files = os.listdir("./files")
    jpegs = []

    for image in images:
        if image in files:
            jpegs.append(image)
        else:
            download_file("cnd_images", "files/" + image)
            jpegs.append(image)
    
    return jpegs

@app.route('/logout', methods=["POST"])
def logout():
    session.pop('email', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
