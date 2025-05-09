## 🚀 FastAPI Project Generator – User Manual

This CLI tool helps you **generate a scalable FastAPI project structure** with prebuilt modules like `punch` and a scaffolded `user` feature.

---

### 📦 Features

* 🧱 Feature-first folder structure
* 🛠️ Preconfigured SQLite database using SQLAlchemy
* ✅ Built-in dependency injection
* 📁 Modular design ready for CRUD, services, and auth
* 🚀 Auto-initialized Git repository with first commit

---

### 🔧 Requirements

* Python 3.7+
* Git installed
* Virtual environment recommended (optional)

---

### 📁 Generated Project Structure

```
<project_name>/
├── app/
│   ├── main.py
│   ├── __init__.py
│   ├── database.py
│   ├── core/
│   ├── shared/
│   ├── modules/
│       ├── punch/
│       └── user/
```

---

### 🛠️ How to Use

1. **Save the script** to a file, e.g. `generate.py`.

2. **Run the script** from the terminal with your desired project name:

```bash
python generate.py your_project_name
```

This will:

* Create the full directory structure
* Add `main.py`, `database.py`, prebuilt `punch` feature, and a scaffold for `user`
* Initialize a Git repository and make the first commit

---

### 🧪 Test Your App

After generating your project:

```bash
cd your_project_name
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore your auto-generated Swagger UI.

---

### 📝 Notes

* `punch` module includes working POST API to store punch-in/out info.
* `user` module contains placeholder files for modular development.
* `.env` file support is set up in `app/core/config.py` (you must create it manually if needed).
* SQLite is used for simplicity but can be replaced easily.

---

### 📌 Tips

* Extend the `user` module with models, schemas, routers, and services.
* Create new modules under `app/modules/<your_module>/`.
* Use `app/shared/` for shared utilities and dependencies.

---
