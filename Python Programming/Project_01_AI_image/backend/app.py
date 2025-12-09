from flask import Flask, request, send_from_directory, session, redirect, url_for
#Flask: Creates web app
#request: Reads uploaded files/form data
#send_from_directory: Serves images/CSS/JS
#session: Remembers user login
#redirect/url_for: Navigates between pages

import cv2
import os
import numpy as np
from werkzeug.utils import secure_filename
#cv2: OpenCV for AI filters
#os: Creates folders
#np: Math for image processing
#secure_filename: Prevents hacker file names

app = Flask(__name__, static_folder='../frontend')
app.secret_key = 'your-secret-key-change-this-in-production'
#static_folder='../frontend': Serves HTML/CSS/JS from frontend folder
#secret_key: Encrypts login sessions (like password)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
SKETCH_FOLDER = os.path.join(BASE_DIR, 'sketches')
CARTOON_FOLDER = os.path.join(BASE_DIR, 'cartoons')
OILPAINT_FOLDER = os.path.join(BASE_DIR, 'oilpaints')
#uploads/     ← User photos
#sketches/    ← Sketch results
#cartoons/    ← Cartoon results  
#oilpaints/   ← Oil painting results


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SKETCH_FOLDER, exist_ok=True)
os.makedirs(CARTOON_FOLDER, exist_ok=True)
os.makedirs(OILPAINT_FOLDER, exist_ok=True)
# if not exist it creats new file

VALID_USER = 'admin'
VALID_PASS = '1234'


def image_to_cartoon(image_path):# Convert into cartoon style
    
    # STEP 1: Load color photo from file
    image = cv2.imread(image_path)

    #  STEP 2: SMOOTH COLORS (FLAT CARTOON STYLE)
    # bilateralFilter = MAGIC: Smooths colors BUT keeps edges sharp
    color_smooth = cv2.bilateralFilter(image, 10, 250, 250)

    #  STEP 3: Create BLACK & WHITE version (for edge detection)
    # RGB [255,128,0] → GRAY [128] (average brightness)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #  STEP 4: Remove noise/tiny speckles (clean edges)
    # medianBlur = Takes 5x5 pixels → picks MIDDLE value (not average)
    gray_blur = cv2.medianBlur(gray, 5)

     
    #  STEP 5: DETECT EDGES → Create BLACK OUTLINES
    # adaptiveThreshold = Smart edge finder (local brightness)
    # 255 = WHITE pixels    | 9=9x9 neighborhood    | 9=threshold offset
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    
    # STEP 6: COMBINE! Smooth colors INSIDE black outlines
    # bitwise_and = MASKING: 
    cartoon = cv2.bitwise_and(color_smooth, color_smooth, mask=edges)

    #Return cartoon image → Flask saves as "cartoon_photo.jpg"
    return cartoon

# convert into oil paint style
def image_to_oil_paint(image_path):
    image = cv2.imread(image_path)# read file
    try:
        oil_paint = cv2.xphoto.oilPainting(image, size=7, dynRatio=1)# dynRatio=1 → How thick paint blobs are , size=7 means 7*7 pixel
    except:
        oil_paint = cv2.stylization(image, sigma_s=60, sigma_r=0.07)
        #sigma_s=60 → How far paint spreads (60 pixels)
        #sigma_r=0.07 → How much color changes allowed
    return oil_paint

def image_to_sketch(image_path):# convert into sketchy style
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return sketch

@app.route('/', methods=['GET', 'POST'])# GET is used to request data from the server , POST is used to send data to the server.
def login():
    if request.method == 'POST':
        username = request.form.get('username')# User clicked "Enter Dashboard"
        password = request.form.get('password')
        if username == VALID_USER and password == VALID_PASS:
            session['logged_in'] = True
            return redirect(url_for('home'))# navigate to home page
        else: # if user and password are wrong
            return '''
            <!DOCTYPE html>
            <html><head><title>Login Failed</title>
            <link rel="stylesheet" href="/style.css"></head>
            <body><div class="container">
                <h1>❌ Login Failed</h1>
                <p style="color: #dc3545; font-size: 18px;">Invalid credentials</p>
                <a href="/" class="btn" style="background: linear-gradient(45deg, #dc3545, #c82333);">🔄 Try Again</a>
            </div></body></html>
            '''
    # if user and password are right [ click on retry button navigate to same page again]
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔐 AI Image Filters</title>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <div class="container">
            <h1>🎨 AI Image Filters</h1>
            <p class="subtitle">Login to access 3 professional AI filters</p>
            
            <form action="/" method="POST" class="login-form">
                <input type="text" name="username" class="login-username" placeholder="👤 Username" required>
                <input type="password" name="password" class="login-password" placeholder="🔒 Password" required>
                <button type="submit">🚀 Enter Dashboard</button>
            </form>
            
            <div class="demo-credentials">
                <p><strong>Demo Credentials:</strong></p>
                <p>👤 Username: <code>admin</code></p>
                <p>🔑 Password: <code>1234</code></p>
            </div>
        </div>
    </body>
    </html>
    '''

# [REST OF ROUTES SAME AS BEFORE - home, logout, convert, serve_file]
@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return send_from_directory('../frontend', 'index.html')

@app.route('/logout')
def logout():
    session.clear()# "Wash off VIP sticker"
    return redirect(url_for('login')) # "Back to login line"

@app.route('/style.css')# apply css 
def css():
    return send_from_directory('../frontend', 'style.css')

@app.route('/script.js') # apply js and link functions
def js():
    return send_from_directory('../frontend', 'script.js')

@app.route('/convert', methods=['POST'])# when user click apply selected filter over image
def convert():
    if not session.get('logged_in'):# if user is not having login session it redirect to login page
        return redirect(url_for('login'))
    
    # default setting
    filter_type = request.form.get('filter', 'sketch')
    file = request.files.get('file')
    
    if not file: return "No file uploaded"  # No photo? Reject!
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Wrong type?
      return "Invalid file type"  # Only photos allowed!

    
    filename = secure_filename(file.filename)
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(upload_path)
    

    # creats folder for generated image 
    if filter_type == 'sketch':
        result_img = image_to_sketch(upload_path)# give image path
        result_folder = 'sketches'# save generated image in folfer
        result_prefix = "sketch_"# image name starts with...
        folder_obj = SKETCH_FOLDER# folder name
    elif filter_type == 'cartoon':
        result_img = image_to_cartoon(upload_path)
        result_folder = 'cartoons'
        result_prefix = "cartoon_"
        folder_obj = CARTOON_FOLDER
    elif filter_type == 'oilpaint':
        result_img = image_to_oil_paint(upload_path)
        result_folder = 'oilpaints'
        result_prefix = "oilpaint_"
        folder_obj = OILPAINT_FOLDER
    else:
        result_img = image_to_sketch(upload_path)
        result_folder = 'sketches'
        result_prefix = "sketch_"
        folder_obj = SKETCH_FOLDER
    
    result_filename = f"{result_prefix}{filename}"# resulted name = new +old
    result_path = os.path.join(folder_obj, result_filename)# path
    cv2.imwrite(result_path, result_img)# save image
    

    # after image is generated page with new image and download button
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>AI Filter Result</title><link rel="stylesheet" href="/style.css"></head>
    <body>
        <div class="container">
        <div style="text-align: right; margin-bottom: 20px;">
            <a href="/logout" class="btn" style="background: linear-gradient(45deg, #dc3545, #c82333);">🚪 Logout</a>
        </div>
        <h1>✅ AI {filter_type.replace("oilpaint", "Oil Painting").title()} Filter Applied!</h1>
        <div class="filter-info">
            <strong>🎨 Filter:</strong> {filter_type.replace("oilpaint", "Oil Painting").title()} Effect
        </div>
        <div class="image-pair">
            <div><h3>📷 Original Image</h3><img src="/uploads/{filename}" alt="Original"></div>
            <div><h3>✨ {filter_type.replace("oilpaint", "Oil Painting").title()}</h3>
                <img src="/{result_folder}/{result_filename}" alt="Result">
                <br><a href="/{result_folder}/{result_filename}" class="btn" download>💾 Download Result</a>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/home" class="btn">🔄 Convert New Image</a>
        </div>
    </div></body></html>
    '''

# routing
@app.route('/uploads/<path:filename>')
@app.route('/sketches/<path:filename>')
@app.route('/cartoons/<path:filename>')
@app.route('/oilpaints/<path:filename>')

def serve_file(filename):
    # if session not present then created new session rediracting to login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # Maps URL parts to actual backend folder paths.
    folder_map = {
        'uploads': UPLOAD_FOLDER, 'sketches': SKETCH_FOLDER,
        'cartoons': CARTOON_FOLDER, 'oilpaints': OILPAINT_FOLDER
    }
    folder = request.path.split('/')[1]
    return send_from_directory(folder_map[folder], filename)

if __name__ == '__main__':
    app.run(debug=True)
