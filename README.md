<<<<<<< HEAD
# Kinjal Sharma — Portfolio Website

A personal portfolio website built using Flask (Python), HTML, CSS, and JavaScript.  
It showcases my projects, skills, and certificates, and includes a working contact form with database integration.

---

## 🚀 Features

- Responsive portfolio design  
- Projects section  
- Certificates section with image preview (click to enlarge)  
- Contact form (Flask + MySQL backend)  

---

## 🛠️ Tech Stack

- Python (Flask)  
- HTML, CSS, JavaScript  
- MySQL  

---

## 📁 Project Structure

```
portfolio-flask/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── images/certificates/
```

## ⚙️ Running Locally

1. Create virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Setup MySQL database
CREATE DATABASE portfolio_db;

4. Create .env file
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=portfolio_db
PORT=5000

5. Run the app
python app.py

6. Open in browser
http://localhost:5000

---

## 📤 Push to GitHub

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/portfolio-flask.git
git push -u origin main

---

## ☁️ Deployment (Render)

1. Push project to GitHub  
2. Go to Render → New Web Service  
3. Connect your repo  

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app

Add Environment Variables:
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=portfolio_db

---

## 📬 Contact

You can reach me through the contact form on the website.

---

## 🚀 Future Improvements

- Add authentication system  
- Add more projects  
- Improve UI/UX  
=======
# portfolio-flask
>>>>>>> 4d60b93db430f197d7352e24cb9a134179316f0e
