from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    try:
        # Run the Python script and capture its output
        result = subprocess.check_output(['python', 'https://drive.google.com/file/d/1i523pd4YRI2X0fsTzYE1pXDifb2BoQs3/view?usp=sharing'], universal_newlines=True, stderr=subprocess.STDOUT)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
