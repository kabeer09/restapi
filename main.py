from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

# -------------------
# CREATE FILE
# -------------------
@app.route("/", methods=["POST"])
def create_file():
    data = request.get_json()
    filename = data.get("filename")
    content = data.get("content")

    if not filename or not content:
        return jsonify({"error": "filename and content required"}), 400

    encoded_content = base64.b64encode(content.encode()).decode()

    payload = {
        "message": "Creating file",
        "content": encoded_content
    }

    res = requests.put(f"{BASE_URL}/{filename}", headers=HEADERS, json=payload)
    return jsonify(res.json()), res.status_code


# -------------------
# READ FILE
# -------------------
@app.route("/<path:filename>", methods=["GET"])
def read_file(filename):
    res = requests.get(f"{BASE_URL}/{filename}", headers=HEADERS)

    if res.status_code != 200:
        return jsonify(res.json()), res.status_code

    data = res.json()
    content = base64.b64decode(data["content"]).decode()

    return jsonify({
        "filename": filename,
        "content": content
    })


# -------------------
# UPDATE FILE
# -------------------
@app.route("/<path:filename>", methods=["PUT"])
def update_file(filename):
    data = request.get_json()
    new_content = data.get("content")

    if not new_content:
        return jsonify({"error": "content required"}), 400

    # Get current file SHA
    get_res = requests.get(f"{BASE_URL}/{filename}", headers=HEADERS)
    if get_res.status_code != 200:
        return jsonify(get_res.json()), get_res.status_code

    sha = get_res.json()["sha"]

    encoded_content = base64.b64encode(new_content.encode()).decode()

    payload = {
        "message": "Updating file",
        "content": encoded_content,
        "sha": sha
    }

    res = requests.put(f"{BASE_URL}/{filename}", headers=HEADERS, json=payload)
    return jsonify(res.json()), res.status_code


# -------------------
# DELETE FILE
# -------------------
@app.route("/<path:filename>", methods=["DELETE"])
def delete_file(filename):
    # Get SHA first
    get_res = requests.get(f"{BASE_URL}/{filename}", headers=HEADERS)
    if get_res.status_code != 200:
        return jsonify(get_res.json()), get_res.status_code

    sha = get_res.json()["sha"]

    payload = {
        "message": "Deleting file",
        "sha": sha
    }

    res = requests.delete(f"{BASE_URL}/{filename}", headers=HEADERS, json=payload)
    return jsonify(res.json()), res.status_code


# -------------------
# RUN
# -------------------
if __name__ == "__main__":
    app.run(debug=True)