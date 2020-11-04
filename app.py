from flask import Flask, render_template, request, abort, send_file
from werkzeug.utils import secure_filename
import os
import uuid

# file paths
absolute_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(absolute_path, "ImageProcessor\\assets\\")
images_dir = os.path.join(absolute_path, "ImageProcessor\\images\\")

# app configurations
app = Flask(__name__, template_folder=template_dir)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['jpg', 'png', 'gif', 'jpeg']

# route to render upload.html template
@app.route('/')
def upload():
    return render_template("upload.html")

# route to display submitted image
@app.route('/image', methods=['GET','POST'])
def upload_file():

    # saving file with unique uuid
    if request.method == 'POST':
        f = request.files['file']
        temp_file_name = f.filename
        if temp_file_name != '':
            unique_filename = str(uuid.uuid4())
            file_extension = temp_file_name.split('.')[1]
            if file_extension not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            file_name = '.'.join([secure_filename(unique_filename), file_extension])
            f.save(os.path.join(images_dir, file_name))
            # return 'file uploaded successfully'
            return send_file(os.path.join(images_dir, file_name), mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)
