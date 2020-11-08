from flask import Flask, render_template, request, abort, send_file
from werkzeug.utils import secure_filename
import os
import io
import uuid
import cv2

# file paths
absolute_path = os.path.dirname(__file__) #D:\UB CSE\ImageProcessor\
template_dir = os.path.join(absolute_path, 'assets') #D:\UB CSE\ImageProcessor\assets

# app configurations
app = Flask(__name__, template_folder=template_dir)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'png', 'gif', 'jpeg']
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['IMAGE_DIR'] = IMAGE_FOLDER #static\images

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
        if temp_file_name != '':
            unique_filename = str(uuid.uuid4())
            file_extension = temp_file_name.split('.')[1]
            # file_extension = f.content_type
            if file_extension not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            file_name = '.'.join([secure_filename(unique_filename), file_extension]) #5d8fe035-d9b0-4066-9334-53ec85f798df.jpeg
            file_path = os.path.join(app.config['IMAGE_DIR'], file_name)
            f.save(os.path.join(absolute_path, file_path))
            # convert to webp format
            # import pdb
            # pdb.set_trace();
            # _img = cv2.imread(file_path)
            # print(_img)
            # retval, buf = cv2.imencode(".webp", _img,[cv2.IMWRITE_WEBP_QUALITY, 100])
            # print(retval)
            # print("webp--->", os.path.join(app.config['IMAGE_DIR'], '.'.join([secure_filename(unique_filename), 'webp'])))
            # buf.tofile()
            # flag = cv2.imwrite('test.webp', buf.tofile('Extens'))
            # print(flag)
            # return 'file uploaded successfully'
            url = "http://127.0.0.1:5000/edit/" + file_name
            return render_template("imageurl.html", images_dir=file_path, image_url=url, file_name=file_name)
            # return send_file(os.path.join(images_dir, file_name), mimetype='image/jpeg')

# route to display submitted image
@app.route('/edit/<file_name>', methods=['GET', 'POST'])
def edit(file_name):
    img_height = request.args.get('height')
    img_width = request.args.get('width')
    file_path = os.path.join(app.config['IMAGE_DIR'], file_name)
    file_extension = file_name.split('.')[1]
    url = "http://127.0.0.1:5000/edit/" + file_name
    org_img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    dsize = (int(img_width),int(img_height))
    new_img = cv2.resize(org_img,dsize)
    new_filename = '.'.join([secure_filename(str(uuid.uuid4())), file_extension])
    new_file_path = os.path.join(app.config['IMAGE_DIR'], new_filename)
    cv2.imwrite(new_file_path, new_img)
    return render_template("imageurl.html", images_dir=new_file_path, image_url=url, file_name=file_name)


if __name__ == "__main__":
    app.run(debug=True)
