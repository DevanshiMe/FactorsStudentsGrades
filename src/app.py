from flask import Flask, request, render_template, jsonify, send_from_directory
import pandas as pd
import os
from subprocess import run
import nbformat

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
PLOTS_FOLDER = 'static/plots'
images = {
    "totalfeature": [],
    "scfeature": [],
    "psyfeature": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)

    if filename.endswith('.csv'):
        data = pd.read_csv(filename)
    elif filename.endswith('.xlsx'):
        data = pd.read_excel(filename)
    else:
        return "Unsupported file format."
    
    execute_notebook(filename)
    return jsonify(images)

def execute_notebook(uploaded_file_path):
    notebook_filename = 'bonus.ipynb'
    
    with open(notebook_filename, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            if 'uploadBonus.csv' in cell.source:
                cell.source = cell.source.replace('uploadBonus.csv', uploaded_file_path)
    
    modified_notebook_filename = 'bonus_UI.ipynb'
    with open(modified_notebook_filename, 'w', encoding='utf-8') as f:
        nbformat.write(notebook_content, f)
    
    command = [
        'jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--ExecutePreprocessor.kernel_name', 'python3', modified_notebook_filename
    ]
    run(command, check=True)

    global images
    for filename in os.listdir(PLOTS_FOLDER):
        if filename.endswith('.png'):
            if 'total' in filename:
                images['totalfeature'].append(filename)
            elif 'sc' in filename:
                images['scfeature'].append(filename)
            elif 'psy' in filename:
                images['psyfeature'].append(filename)
        elif filename.endswith('.html'):
            if 'total' in filename:
                images['totalfeature'].append(filename)
            elif 'sc' in filename:
                images['scfeature'].append(filename)
            elif 'psy' in filename:
                images['psyfeature'].append(filename)

    return jsonify(images)

@app.route('/static/plots/<filename>')
def serve_image(filename):
    return send_from_directory(PLOTS_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
