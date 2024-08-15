from flask import Flask, jsonify, request, send_file
from fdds.core.engine import FDDSEngine
from fdds.storage.backup import BackupManager
from werkzeug.utils import safe_join
import os

app = Flask(__name__)
engine = FDDSEngine()

# Set up the upload folder for file uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "FDDS API is running!"

@app.route('/api/query', methods=['POST'])
def execute_query():
    data = request.get_json()
    query = data.get('query')
    
    try:
        result = engine.execute_fdql(query)
        return jsonify({'status': 'success', 'result': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/backup', methods=['POST'])
def create_backup():
    data = request.get_json()
    db_name = data.get('db_name')
    
    try:
        backup_manager = BackupManager(engine.get_storage_path())
        result = backup_manager.create_backup(db_name)
        return jsonify({'status': 'success', 'message': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# File upload endpoint
@app.route('/api/upload_file', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400

    # Save the file to the upload directory
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # Explicitly save the file as binary
    with open(file_path, 'wb') as f:
        f.write(file.read())
    
    return jsonify({'status': 'success', 'message': f'File {file.filename} uploaded successfully', 'path': file_path}), 200

# File download endpoint with enhanced error handling and debugging
@app.route('/api/download_file/<filename>', methods=['GET'])
def download_file(filename):
    try:
        # Construct the full file path safely
        file_path = safe_join(app.config['UPLOAD_FOLDER'], filename)
        print(f"Attempting to download file from path: {file_path}")  # Debugging

        if os.path.exists(file_path):
            # Send the file as a binary stream
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'status': 'error', 'message': 'File not found'}), 404

    except Exception as e:
        print(f"Error during file download: {str(e)}")  # Debugging
        return jsonify({'status': 'error', 'message': 'An error occurred while trying to download the file.'}), 500

# File delete endpoint
@app.route('/api/delete_file/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        # Construct the full file path safely
        file_path = safe_join(app.config['UPLOAD_FOLDER'], filename)
        print(f"Attempting to delete file from path: {file_path}")  # Debugging

        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify({'status': 'success', 'message': f'File {filename} deleted successfully'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'File not found'}), 404

    except Exception as e:
        print(f"Error during file deletion: {str(e)}")  # Debugging
        return jsonify({'status': 'error', 'message': 'An error occurred while trying to delete the file.'}), 500

if __name__ == "__main__":
    app.run(debug=True)
