# At the top of your main.py file
import os
from dotenv import load_dotenv

# This line loads the environment variables from the .env file
load_dotenv()

# The rest of your main.py file stays the same...

# When you instantiate the model, it will automatically find the GOOGLE_API_KEY
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

