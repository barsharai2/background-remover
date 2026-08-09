# 🖼️ BG Remover

A simple and user-friendly **image background removal web application** built with Django and Python.

This project was developed as a **hands-on learning project** to strengthen my skills in Django, Python, frontend development, file handling, and image processing.

---

## 🚀 About The Project

BG Remover allows users to upload an image and automatically remove its background.

After processing, users can:

- Upload an image
- Remove the image background
- Preview the processed image
- Download the background-removed image

The project focuses on creating a simple and clean user experience while learning how different technologies work together in a Django application.

---

## ✨ Features

- 📤 Image Upload
- 🤖 Automatic Background Removal
- 🖼️ Processed Image Preview
- 📥 Download Background-Removed Image
- 📱 Responsive Design
- 🎨 Bootstrap UI
- 🏠 Home Page
- 🖼️ Gallery Page
- ℹ️ About Page
- 📞 Contact Page

---

## 🛠️ Technologies Used

### Backend

- Python
- Django
- rembg
- Pillow

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Font Awesome

### Database

- SQLite

---

## 📂 Project Structure

```text
BG-Remover/
│
├── manage.py
│
├── my_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── my_app/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── my_app/
│       ├── home.html
│       ├── bgremove.html
│       ├── gallery.html
│       ├── about.html
│       └── contact.html
│
├── static/
│   ├── css/
│   └── images/
│
├── media/
│
├── .gitignore
├── requirements.txt
└── README.md
