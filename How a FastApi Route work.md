যখন একজন ইউজার ব্রাউজারে গিয়ে `www.shafiquebd.com/student` হিট করে, তখন FastAPI কীভাবে কাজ করে তার **পিছনের পুরো প্রসেস** (Backend Flow) নিচে বাংলায় ব্যাখ্যা করা হলো।

---

## 🔄 ১. ইউজার হিট করে: `www.shafiquebd.com/student`

* এই URL আসলে একটি **HTTP GET Request** পাঠায় `www.shafiquebd.com` সার্ভারে `/student` রুটে।
* ধরে নিচ্ছি আপনি FastAPI দিয়ে একটি API সার্ভার বানিয়েছেন যেটা `uvicorn` বা `gunicorn` দিয়ে রান হচ্ছে।

---

## 🧠 ২. FastAPI কীভাবে রিকোয়েস্ট হ্যান্ডেল করে

### Step-by-step Breakdown:

### ✅ ১. **UVicorn** → ASGI Server:

* Uvicorn হলো FastAPI-এর backend server (ASGI server).
* এটি সব incoming HTTP request নেয় এবং FastAPI অ্যাপকে দেয়।

```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

### ✅ ২. **FastAPI অ্যাপ শুরু হয়:**

```python
from fastapi import FastAPI
from app.routes import student  # ধরে নিচ্ছি student router আছে

app = FastAPI()

app.include_router(student.router, prefix="/student", tags=["Student"])
```

* এই `include_router()` ফাংশন FastAPI-কে বলে যে `/student` রুটে আসা সব request → `student.router` ফাইলে যাবে।

---

## ✅ ৩. `/student` URL কোথায় যায়?

```python
@router.get("/")
def get_all_students():
    return [{"id": 1, "name": "Rahim"}, {"id": 2, "name": "Karim"}]
```

* এখানে `/student` রুট মানে মূলত `prefix="/student"` + `@router.get("/")` → মিলে `/student`
* এই ফাংশন call হয় এবং JSON response রিটার্ন করে।

---

## 🔄 Behind-the-Scenes ডায়াগ্রাম (বাংলায়):

```text
[ইউজার ব্রাউজারে টাইপ করে] 
      ↓
https://www.shafiquebd.com/student
      ↓
[Domain পয়েন্ট করে server IP-তে]
      ↓
[Server চালু uvicorn দিয়ে → FastAPI অ্যাপ]
      ↓
[FastAPI দেখে prefix="/student"]
      ↓
[match করে @router.get("/") এর সাথে]
      ↓
[function execute → data fetch → JSON response পাঠায়]
      ↓
[User browser-এ JSON output দেখে]
```

---

## 🎯 এক কথায় সংক্ষেপে:

যখন ইউজার `/student` URL হিট করে, FastAPI ওই URL কে match করে সেই রাউটারের function এর সাথে, data ফেচ করে এবং JSON আকারে রেসপন্স পাঠায়।

---

আপনার যদি `@router.get("/get_all_name")` এর মতো সাবরাউট থাকে, তাহলে সেটা `/student/get_all_name` হয়ে যাবে।

