from flask import Flask, render_template, request
import spacy
import os
import docx
import PyPDF2

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")  # make sure this is installed

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Match calculation
def calculate_match(resume_text, jd_text):
    resume_doc = nlp(resume_text)
    jd_doc = nlp(jd_text)
    return resume_doc.similarity(jd_doc) * 100  # percentage

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        jd = request.form.get('jd', '').strip()
        resume_text_input = request.form.get('resume_text', '').strip()
        file = request.files.get('resume_file')

        resume_text = ""

        # Priority: uploaded file first
        if file and file.filename:
            file_ext = file.filename.lower().split('.')[-1]
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            if file_ext == "pdf":
                resume_text = extract_text_from_pdf(file_path)
            elif file_ext == "docx":
                resume_text = extract_text_from_docx(file_path)
            else:
                error = "Unsupported file type. Please upload a PDF or DOCX."
        elif resume_text_input:
            resume_text = resume_text_input
        else:
            error = "Please paste resume text or upload a file."

        # If resume and JD provided, calculate match
        if resume_text and jd:
            match = calculate_match(resume_text, jd)
            result = f"Match Score: {match:.2f}%"
        elif not jd:
            error = "Please enter the job description."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
