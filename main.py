from flask import Flask, request, render_template, jsonify
from pdf import get_codes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        return jsonify(get_codes(file.stream))
    

def main():
    app.run(debug=True)
    return 0

if __name__ == "__main__":
    exit(main())
