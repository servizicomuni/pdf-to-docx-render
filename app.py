
from flask import Flask, request, send_file
import fitz  # PyMuPDF
from docx import Document
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf():
    pdf_file = request.files['file']
    pdf_path = 'temp.pdf'
    docx_path = 'converted.docx'

    pdf_file.save(pdf_path)

    doc = Document()
    pdf = fitz.open(pdf_path)
    for page in pdf:
        text = page.get_text()
        doc.add_paragraph(text)
    pdf.close()
    doc.save(docx_path)

    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
