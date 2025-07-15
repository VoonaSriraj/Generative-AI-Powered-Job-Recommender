import fitz  # PyMuPDF
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(prompt, max_tokens=500):
    """
    Sends a prompt to the OpenAI API and returns the response.
    
    Args:
        prompt (str): The prompt to send to the OpenAI API.
        model (str): The model to use for the request.
        temperature (float): The temperature for the response.
        
    Returns:
        str: The response from the OpenAI API.
    """
    

    response = client.chat.completions.create(
        model= "llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content

def extract_text_from_pdf(uploaded_pdf):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    
    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        str: The extracted text from the PDF.
    """
    text=""
    doc=fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    for page in doc:
        text +=page.get_text()
    return text