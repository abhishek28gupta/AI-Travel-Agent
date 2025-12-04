import google.generativeai as genai

genai.configure(api_key="AIzaSyAPi4FC2jcABV5Csg_EOgbAM0liFrh9ZPU")
for m in genai.list_models():
    print(m.name)
