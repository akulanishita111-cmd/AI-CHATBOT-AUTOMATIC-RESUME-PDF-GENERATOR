 Features

* 🤖 AI Chatbot-based question flow (step-by-step interaction)
* 📝 Automatic resume data collection
* 📄 One-click resume PDF generation
* 🎨 Modern UI with dashboard and progress tracking
* ⚡ Fast and user-friendly experience
* 💾 Data storage during session
* 📥 Download resume as PDF

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Database (Optional):** MySQL
* **Libraries Used:**

  * Flask
  * reportlab / docx
  * nltk (for text processing)
  * zipfile, os

---

## 📁 Project Structure

```
AI-CHATBOT-AUTOMATIC-RESUME-PDF-GENERATOR/
│── app.py
│── templates/
│   ├── index.html
│   ├── dashboard.html
│── static/
│   ├── css/
│   ├── js/
│── resumes/
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup (Run in VS Code)

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 🔹 Step 2: Open in VS Code

* Open **VS Code**
* Click **File → Open Folder**
* Select your project folder

---

### 🔹 Step 3: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 🔹 Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install flask nltk python-docx reportlab
```

---

### 🔹 Step 5: Run the Application

```bash
python app.py
```

---

### 🔹 Step 6: Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

---

## 💡 How It Works

1. User interacts with chatbot
2. System asks resume-related questions
3. Data is collected step-by-step
4. Resume is generated automatically
5. User downloads PDF instantly

---

## 📸 Screenshots (Optional)

*Add screenshots here like:*

* Chatbot UI
* Dashboard
* Generated Resume

---

## 🔧 Future Enhancements

* AI-based resume suggestions
* Multiple resume templates
* Cloud storage integration
* User login system
* Resume preview before download

---

## 🐛 Troubleshooting

### Issue: PDF not generating

* Check if required libraries are installed
* Ensure `resumes/` folder exists

### Issue: Flask not running

* Check Python version (recommended: 3.8+)
* Verify virtual environment activation

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

**Nishita Nishi**

---


If you like this project, give it a ⭐ on GitHub!


### 🔥 Tip

Before uploading to GitHub:

* Replace `your-username/your-repo-name`
* Add screenshots
* Add `requirements.txt` (I can generate it for you if you want)

---

