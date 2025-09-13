
# 📂 MCP Demo Project

This is a simple **Model Context Protocol (MCP)** demo project.
It exposes a lightweight API to interact with local files using **FastAPI**.

---

## ⚡ Features

* List files inside the `docs/` folder
* Read contents of a file via API
* Built with **FastAPI** + **Uvicorn**
* Simple entry point to extend MCP for RAG, LLMs, or custom tools

---

## 📂 Project Structure

```
github_mcp/
│── docs/                # Text files for testing
│   ├── sample_1.txt
│   ├── sample_2.txt
│
│── server.py            # MCP FastAPI server
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .env                 # (optional) environment variables
```

---

## 🚀 Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/github_mcp.git
cd github_mcp
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run MCP server

```bash
python server.py
```

The server will start at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 API Endpoints

### ✅ List files

```
GET /list_files
```

Example Response:

```json
{"files": ["sample_1.txt", "sample_2.txt"]}
```

### 📖 Read file

```
GET /read_file/{filename}
```

Example:

```bash
curl http://127.0.0.1:8000/read_file/sample_1.txt
```

Response:

```json
{"filename": "sample_1.txt", "content": "This is a test file."}
```

---

## 🛠️ Next Steps

* Add **LLM-powered embeddings** (RAG pipeline)
* Extend with **chat endpoints**
* Integrate with **LangChain / MCP client**

---

## 📜 License

MIT License. Free to use & modify.

---

Do you want me to also include a **`requirements.txt` snippet** in the README so GitHub users can just copy-paste without opening the file?
