# GitHub File CRUD API (Flask)

A simple Flask-based REST API that performs **CRUD operations on GitHub repository files** using the GitHub REST API.

---

## Features

* Create a file in a GitHub repository
* Read file contents
* Update existing files
* Delete files
* Secure access using GitHub Personal Access Token
*  Built with Flask + Requests

---

##  Tech Stack

* Python
* Flask
* Requests
* GitHub REST API

---

##  Project Structure

```
.
├── app.py
├── README.md
```

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Install Dependencies

```bash
pip install flask requests
```

---

### 3. Configure GitHub Token

Generate a Personal Access Token from GitHub and update your code:

```python
GITHUB_TOKEN = "your_token_here"
OWNER = "your_github_username"
REPO = "your_repository_name"
```

---

### 4. Run the Application

```bash
python main.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

##  API Endpoints

### Create File

**POST** `/`

```json
{
  "filename": "test.txt",
  "content": "Hello World"
}
```

---

### Read File

**GET** `/<filename>`

Example:

```
/test.txt
```

---

### Update File

**PUT** `/<filename>`

```json
{
  "content": "Updated content"
}
```

---

###  Delete File

**DELETE** `/<filename>`

---

##  Important Notes

* File content must be encoded in Base64 (handled automatically in code)
* GitHub requires a **SHA value** for updating/deleting files
* Repository must already exist
* API uses GitHub commits internally

---

## Testing

You can test APIs using:

* Postman
* cURL
* Thunder Client (VS Code)

---

##  Common Errors

| Error            | Cause                              |
| ---------------- | ---------------------------------- |
| 401 Unauthorized | Invalid GitHub token               |
| 404 Not Found    | Wrong repo or file                 |
| 409 Conflict     | File already exists / SHA mismatch |

---


##  Contributing

Pull requests are welcome! Feel free to fork and improve the project.

---

## License

This project is open-source and available under the MIT License.

---

##  Acknowledgment

Powered by the GitHub REST API.

---

If you want, I can also:

* Add **badges (build, stars, license)**
* Customize it for your **GitHub profile repo**
* Or make a **fancy README with screenshots + GIF demo**
