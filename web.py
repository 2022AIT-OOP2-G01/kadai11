import os
import glob
from flask import Flask, render_template, send_from_directory, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './original'
app.config['OUTPUT_FOLDER'] = './after'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', message = '画像のアップロードが完了しました')
    return render_template('index.html', message = '画像のアップロードができていません')

# Topページ
@app.route('/')
def index():
    return render_template("index.html", message='')


# アップロードファイル一覧
@app.route('/uploaded_list/')
def uploaded_list():
    files = glob.glob("./original/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/uploaded/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="アップロードファイル", target_files=urls)


# 画像処理後のファイル一覧(モザイク)
@app.route('/mosaic_list/')
def processed_mosaic_list():
    files = glob.glob("./after/mosaic/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/mosaic/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="モザイク", target_files=urls)

# 画像処理後のファイル一覧(顔検出)
@app.route('/face_list/')
def processed_face_list():
    files = glob.glob("./after/face/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/face/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="顔検出", target_files=urls)

# 画像処理後のファイル一覧(輪郭抽出)
@app.route('/contour_list/')
def processed_contour_list():
    files = glob.glob("./after/contour/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/contour/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="輪郭抽出", target_files=urls)

# 画像処理後のファイル一覧(グレイスケール)
@app.route('/gs_list/')
def processed_gs_list():
    files = glob.glob("./after/gs/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/gs/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="グレースケール", target_files=urls)

# 画像処理後のファイル一覧(2値化)
@app.route('/binary_list/')
def processed_binary_list():
    files = glob.glob("./after/binary/*")
    urls = []
    for file in files:
        urls.append({
            "filename": os.path.basename(file),
            "url": "/processed/binary/" + os.path.basename(file)
        })
    return render_template("index.html", page_title="2値化", target_files=urls)


@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/processed/mosaic/<path:filename>')
def processed_mosaic_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'] + '/mosaic', filename)

@app.route('/processed/face/<path:filename>')
def processed_face_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'] + '/face', filename)

@app.route('/processed/contour/<path:filename>')
def processed_contour_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'] + '/contour', filename)

@app.route('/processed/gs/<path:filename>')
def processed_gs_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'] + '/gs', filename)

@app.route('/processed/binary/<path:filename>')
def processed_binary_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'] + '/binary', filename)

if __name__ == "__main__":
    app.run(debug=True)