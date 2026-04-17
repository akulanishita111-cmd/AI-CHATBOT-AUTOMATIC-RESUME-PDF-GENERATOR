"""
AI Resume Builder - Flask Application
Run: python app.py
Then open: http://localhost:5000
"""

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ── Config ──────────────────────────────────────────────────
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'webp'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024   # 16 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.secret_key = 'resume-builder-secret-2025'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ──────────────────────────────────────────────────

@app.route('/')
def index():
    """Serve the main resume builder page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle profile photo / signature / certificate uploads.
    Returns JSON with the public URL of the saved file.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Prefix with a timestamp to avoid collisions
        import time
        filename = f"{int(time.time())}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({
            'success': True,
            'filename': filename,
            'url': f'/uploads/{filename}'
        })

    return jsonify({'error': 'File type not allowed'}), 400


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files (photos, signatures, certs)."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/health')
def health():
    """Simple health-check endpoint."""
    return jsonify({'status': 'ok', 'app': 'AI Resume Builder'})


# ── Entry point ──────────────────────────────────────────────

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    print(f"\n{'='*50}")
    print(f"  AI Resume Builder")
    print(f"  Running on http://localhost:{port}")
    print(f"{'='*50}\n")
    app.run(host='0.0.0.0', port=port, debug=debug)
