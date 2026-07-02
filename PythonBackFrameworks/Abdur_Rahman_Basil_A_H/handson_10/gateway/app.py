from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# The internal addresses of our microservices
COURSE_SERVICE_URL = "http://127.0.0.1:5001"
STUDENT_SERVICE_URL = "http://127.0.0.1:5002"

def forward_request(base_url, path):
    """Helper function to forward requests to the correct service"""
    url = f"{base_url}/{path}"
    
    # We grab the method, body, and query parameters from the incoming request
    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True), # Forward the JSON body if it exists
        params=request.args                 # Forward query parameters
    )
    
    # Return the exact response we got from the microservice
    try:
        return jsonify(response.json()), response.status_code
    except:
        return response.content, response.status_code


@app.route('/api/courses', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/courses/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_courses(path):
    full_path = f"api/courses/{path}" if path else "api/courses"
    return forward_request(COURSE_SERVICE_URL, full_path)


@app.route('/api/students', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/students/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_students(path):
    full_path = f"api/students/{path}" if path else "api/students"
    return forward_request(STUDENT_SERVICE_URL, full_path)


if __name__ == '__main__':
    # The Gateway runs on port 5000!
    app.run(port=5000, debug=True)