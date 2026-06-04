import google.generativeai as genai
import time
import os

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Explain quicksort in Python."

start = time.time()

response = model.generate_content(prompt)

end = time.time()

latency = end - start

print("\n===== RESPONSE =====\n")

print(response.text)

print("\n===== METRICS =====\n")

print(f"Latency: {latency:.2f} seconds")
print(f"Response Size: {len(response.text)} characters")
