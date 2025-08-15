# career-nest-resume-screener

An AI-powered web tool that matches resumes against job descriptions using Natural Language Processing (NLP) and calculates the matching score.

🚀 Features

Resume Parsing – Extracts text from .pdf or .docx resumes.
NLP-based Matching – Uses spaCy to compare skills and content.
Match Percentage – Gives a similarity score in percentage.
Interactive UI – Clean & modern interface built with HTML/CSS.
File Upload Support – Upload resumes instead of copy-paste.

🛠 Tech Stack

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
NLP: spaCy (en_core_web_sm)
PDF Parser: PyPDF2
DOCX Parser: python-docx

📂 Project Structure
resume-screener/
│── app.py                # Main Flask app
│── templates/
│   └── index.html         # Frontend HTML
│── static/
│   └── style.css          # Stylesheet
│── venv/                  # Virtual environment (ignored in Git)
│── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/Abhinavsingh6557/career-nest-resume-screener.git
cd career-nest-resume-screener

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment
Windows PowerShell
venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Install spaCy Model
python -m spacy download en_core_web_sm

6️⃣ Run the App
python app.py

The app will be live at:
http://127.0.0.1:5000

📌 How It Works

Upload your resume file (.pdf or .docx).
Enter a job description in the text box.
Click Match Now.
The AI processes both texts using spaCy NLP and gives a similarity percentage.

Future Improvements:
• Support for multiple resume formats (DOCX, TXT)
• Advanced NLP model integration (BERT, GPT-based)
• Keyword extraction and highlighting
• Cloud deployment with Docker and Kubernetes
• Integration with job portals for automated screening

Conclusion:
The CareerNest Resume Screener project demonstrates the power of combining NLP with web
applications to solve real-world recruitment challenges. By automating the resume screening
process, recruiters can save significant time and effort. The project is highly customizable and can be extended with advanced AI models for better accuracy.



