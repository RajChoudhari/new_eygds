import google.generativeai as genai
genai.configure(api_key="AIzaSyC9OT_L0M6qE7JJ0Y9ebj3xKYAjpzYVk5k")
for m in genai.list_models():
    print(m.name)