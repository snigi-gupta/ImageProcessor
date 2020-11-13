from flask import Flask, render_template, request, abort, send_file
from werkzeug.utils import secure_filename
from cachetools import cached, TTLCache
from PIL import Image, ImageDraw
import os
import io
import uuid
import cv2
import numpy as np

# file paths
absolute_path = os.path.dirname(__file__)  # D:\UB CSE\ImageProcessor\
template_dir = os.path.join(absolute_path, 'assets')  # D:\UB CSE\ImageProcessor\assets

# app configurations
app = Flask(__name__, template_folder=template_dir)
cache = TTLCache(maxsize=1000, ttl=60)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'png', 'gif', 'jpeg']
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['IMAGE_DIR'] = IMAGE_FOLDER  # static\images


# route to render upload.html template
@app.route('/')
def upload():
    return render_template("upload.html")


# route to display submitted image
@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    # saving file with unique uuid
    if request.method == 'POST':
        f = request.files['file']
        temp_file_name = f.filename
        f = Image.open(f).convert("RGB")
        if temp_file_name != '':
            unique_filename = str(uuid.uuid4())
            file_extension = temp_file_name.split('.')[1]
            if file_extension not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            file_extension = 'webp'
            file_name = '.'.join(
                [secure_filename(unique_filename), file_extension])  # 5d8fe035-d9b0-4066-9334-53ec85f798df.jpeg
            file_path = os.path.join(app.config['IMAGE_DIR'], file_name)
            f.save(os.path.join(absolute_path, file_path), 'webp')
            url = "http://127.0.0.1:5000/edit/" + file_name
            return render_template("edit.html", images_dir=file_path, image_url=url, file_name=file_name)


# caching function to display edited image
@cached(cache)
def edit_file(file_name, img_height, img_width, img_rotate, img_ellipse=False):
    file_path = os.path.join(app.config['IMAGE_DIR'], file_name)
    file_extension = file_name.split('.')[1]
    url = "http://127.0.0.1:5000/edit/" + file_name

    # get original image
    org_img = Image.open(file_path).convert("RGB")

    # get original image dimensions if no URL parameters
    org_height, org_width = org_img.size

    # resizing the image
    dsize = (int(img_width or org_width), int(img_height or org_height))
    new_img = org_img.resize(dsize)

    

    new_filename = '.'.join([secure_filename(str(uuid.uuid4())), file_extension])
    new_file_path = os.path.join(app.config['IMAGE_DIR'], new_filename)
    new_img.save(new_file_path, 'webp')
    return new_file_path, url, file_name


# route to display edited image
@app.route('/edit/<file_name>', methods=['GET', 'POST'])
def edit(file_name):
    img_height = request.args.get('height')
    img_width = request.args.get('width')
    img_ellipse = request.args.get('ellipse')
    img_rotate = request.args.get('rotate')

    new_file_path, url, new_file_name = edit_file(file_name, img_height, img_width, img_rotate, img_ellipse)
    return render_template("edit.html", images_dir=new_file_path, image_url=url, file_name=new_file_name)


if __name__ == "__main__":
    app.run(debug=True)
