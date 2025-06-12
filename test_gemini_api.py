import sys
import os
import site
print("Python Version:", sys.version)
print("Python Path:", sys.executable)
print("Site Packages:", site.getsitepackages())
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("API Key:", "Set" if api_key else "Not set")
print("Key Start:", api_key[:5] if api_key else "No key")