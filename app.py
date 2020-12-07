from flask import Flask, render_template, request, abort, send_file
from werkzeug.utils import secure_filename
from cachetools import cached, TTLCache, Cache
from apscheduler.schedulers.background import BackgroundScheduler
from PIL import Image, ImageDraw
import os
import uuid
import time
import atexit
import numpy as np

# file paths
absolute_path = os.path.dirname(__file__)  # D:\UB CSE\ImageProcessor\
template_dir = os.path.join(absolute_path, 'assets')  # D:\UB CSE\ImageProcessor\assets

# app configurations
app = Flask(__name__, template_folder=template_dir)
cache = TTLCache(maxsize=1000, ttl=300)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'jpeg', 'png', 'gif', 'webp']
# IMAGE_FOLDER = os.path.join('static', 'images')
app.config['IMAGE_DIR'] = os.path.join('static', 'images')  # static\images
app.config['CACHE_DIR'] = os.path.join('static', 'cache')  # static\cache

# extension mapping
extension_map = {
    "0": 'jpg',
    "1": 'jpeg',
    "2": 'png',
    "3": 'gif',
    "4": 'webp'
}

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
            file_extension = temp_file_name.split('.')[1]

            if file_extension not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            unique_filename = str(uuid.uuid4()) + str(app.config['UPLOAD_EXTENSIONS'].index(file_extension))

            file_name = secure_filename(unique_filename)  # 5d8fe035-d9b0-4066-9334-53ec85f798df0 with mapping
            file_path = os.path.join(app.config['IMAGE_DIR'], file_name + "." + file_extension)
            f.save(os.path.join(absolute_path, file_path))
            url = "http://127.0.0.1:5000/edit/" + file_name
            return render_template("edit.html", images_dir=file_path, image_url=url, file_name=file_name)


# caching function to display edited image
@cached(cache)
def edit_file(file_name, img_height, img_width, img_rotate, img_type, img_ellipse=False):

    # get extension
    file_extension = extension_map[file_name[-1]]
    file_path = os.path.join(app.config['IMAGE_DIR'], file_name + "." + file_extension)
    # file_extension = file_name.split('.')[1]
    url = "http://127.0.0.1:5000/edit/" + file_name
    # get original image
    org_img = Image.open(file_path).convert("RGB")

    # get original image dimensions if no URL parameters
    org_height, org_width = org_img.size

    #calculate the aspect ratio
    aspect_ratio = org_height/org_width
    if not img_width and not img_height:
        img_width, img_height = org_width, org_height
    elif not img_width:
        img_width = int(img_height)/aspect_ratio
    elif not img_height:
        img_height = int(img_width) * aspect_ratio

    # resizing the image
    dsize = (int(img_width), int(img_height))
    new_img = org_img.resize(dsize)

    # rotate image
    if img_rotate:
        new_img = new_img.rotate(-int(img_rotate))

    # crop circular
    if img_ellipse:
        h, w = new_img.size
        npImage = np.array(new_img)

        # create same size alpha layer with circle
        alpha = Image.new('L', new_img.size, 0)
        draw_alpha = ImageDraw.Draw(alpha)
        draw_alpha.pieslice([0, 0, h, w], 0, 360, fill=255)

        # convert alpha image to numpy array again
        npAlpha = np.array(alpha)

        # add alpha layer to RGB
        npImage = np.dstack((npImage, npAlpha))

        new_img = Image.fromarray(npImage)

    # convert to webp
    if img_type:
        file_extension = 'webp'
        new_filename = secure_filename(str(uuid.uuid4()) + str(app.config['UPLOAD_EXTENSIONS'].index(file_extension)))
    else:
        new_filename = secure_filename(str(uuid.uuid4()) + file_name[-1])
    new_file_path = os.path.join(app.config['CACHE_DIR'], new_filename + "." + file_extension)
    new_img.save(new_file_path)

    return new_file_path, url, new_filename


# route to display edited image
@app.route('/edit/<file_name>', methods=['GET', 'POST'])
def edit(file_name):
    img_height = request.args.get('height')
    img_width = request.args.get('width')
    img_ellipse = request.args.get('ellipse')
    img_rotate = request.args.get('rotate')
    img_type = request.args.get('imgtype')

    new_file_path, url, new_file_name = edit_file(file_name, img_height, img_width, img_rotate, img_type, img_ellipse)
    # file_name = file_name + "." + extension_map[file_name[-1]]
    return render_template("edit.html", images_dir=new_file_path, image_url=url, file_name=file_name)


def delete_file():
    images = os.listdir(app.config['CACHE_DIR'])
    current_time = time.time()
    for image in images:
        img_path = os.path.join(app.config['CACHE_DIR'], image)
        img_time = os.path.getmtime(img_path)
        # print(current_time, img_path, img_time)
        if current_time-img_time > 60:
            os.remove(img_path)


if __name__ == "__main__":

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=delete_file, trigger="interval", seconds=60)
    scheduler.start()
    app.run(debug=True, threaded=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
