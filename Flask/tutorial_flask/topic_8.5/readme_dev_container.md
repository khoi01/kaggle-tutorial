Absolutely! Here's your new, clean, beginner-friendly `README.md` tailored to your setup:

---

```markdown
# 🐳 Flask API – Dev Container Setup Guide

This project runs a Flask API inside a **VS Code Dev Container** using Docker. It ensures a consistent development environment and removes the need for local Python setup.

---

## 📁 Project Structure

```
project-root/
├── .devcontainer/
│   └── devcontainer.json
├── app.py
├── Dockerfile
├── requirements.txt
├── .env
└── docker-compose.yml   # optional
```

---

## ⚙️ Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

## 🚀 How to Setup the Dev Container

### 1️⃣ Open project in VS Code

```bash
code .
```

---

### 2️⃣ Reopen in Dev Container

1. Open Command Palette:  
   `Ctrl+Shift+P` or `Cmd+Shift+P`
2. Select:  
   `Dev-Containers: Open Folder in Container`

VS Code will:
- Build the container from the `Dockerfile`
- Mount your project into the container
- Install dependencies inside Docker

---

### 3️⃣ Folder Mounting (Sync Files Between Host & Dev Container)

Ensure the `.devcontainer/devcontainer.json` contains:

```json
{
  "name": "Flask Dev",
  "build": {
    "dockerfile": "../Dockerfile"
  },
  "workspaceFolder": "/workspace",
  "workspaceMount": "source=${localWorkspaceFolder},target=/workspace,type=bind",
  "settings": {
    "python.pythonPath": "/usr/local/bin/python"
  },
  "extensions": [
    "ms-python.python"
  ],
  "forwardPorts": [5000],
  "postCreateCommand": "pip install -r requirements.txt"
}
```

This ensures:
✅ Any changes or new files inside the container are also saved on your host PC.

---

## ▶️ How to Run the App (Inside Dev Container)

Once the container is open:

```bash
python app.py
```

Then visit:  
👉 `http://localhost:5000`

---

## 📦 How to Use `.env`

Create a `.env` file in the root folder:

```
FLASK_ENV=development
SECRET_KEY=mysecret
UPLOAD_DIR=uploads
```

In `app.py`, load it using:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 🔁 Auto-Reload Flask (Optional for Dev)

Inside `app.py`, run Flask like this:

```python
app.run(debug=True, host="0.0.0.0", use_reloader=True)
```

This allows automatic restarts when `.py` files are modified.

---

## ✅ Summary

| Task | How |
|------|-----|
| Rebuild dev container | `Remote-Containers: Rebuild and Reopen in Container` |
| Sync files with host | Use `workspaceMount` |
| Run the app | `python app.py` |
| Install packages | `pip install packagename` inside container |

---

Happy coding! 🐍💻🐳
```

Let me know if you'd like me to generate this as an actual file for download or push it to your repo structure!