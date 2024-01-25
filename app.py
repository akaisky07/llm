# import gemini_client
# api_key = "AIzaSyAiB2nQe1lfdip_h0Ap2wphPGzM-_bRJBY"
# client = gemini_client.Client(api_key=api_key)

# def generate_summary_with_gemini(function_code, function_name, metadata=None):
#     prompt = f"Summarize the following function in a concise and informative way:\n\n{function_code}\n\nFunction name: {function_name}\n\n{metadata}"
#     response = client.generate_text(prompt=prompt)
#     return response.text

import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAiB2nQe1lfdip_h0Ap2wphPGzM-_bRJBY"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from IPython.display import Markdown

input="def add_numbers(*args):sum = 0for number in args:sum += numberreturn sum"

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Summarize the following function in a concise and informative way"+input)

Markdown(response.text)

print(response.text)
