

---

## File Structure: What Each File Does

-   `main.py`: The main chatbot application. **Empty.**
-   `google_tools.py`: The library of tool functions that connect to Google APIs (e.g., `Calendar`). **This is where you will add new capabilities.**
-   `authenticate.py`: A one-time script that you run to grant the application permission to access your Google account. It creates the `token.json` file.
-   `test_tool.py`: A script for testing individual tools in isolation before integrating them into the main agent.

---

## Setup Instructions


### Step 1: Clone & Install
1.  **Clone the repository** to your local machine.
2.  **Create and activate a Python virtual environment.**
    ```bash
    # Create the environment
    python -m venv venv
    # Activate it (on macOS/Linux)
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```
3.  **Install all required packages.**
    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Get Credentials
1.  **Get `credentials.json`:** 
2.  **Create `.env` file:** Create a new file in the root directory named `.env`. Open it and add your Google API Key for the Gemini model:
    ```
    GOOGLE_API_KEY="your_personal_google_api_key_here"
    ```


### Step 4: Run Authentication
Run the authentication script from your terminal:
```bash
python authenticate.py
```
This will open your browser. Log in with the Google account , and grant all the requested permissions. When it's finished, a `token.json` file will appear in your project folder.

### Step 5: Run the Chatbot!
You are now fully set up. Start the main application:
```bash
python main.py
```
You can now chat with the agent from your terminal.

---

## How to Add New Tools
1.  **Build:** Add your new tool function to `google_tools.py`. Remember the `@tool` decorator and a detailed docstring explaining what it does.
2.  **Test:** Open `test_tool.py`, import your new tool, and add a simple test case to call it with `.invoke()` to ensure it works on its own.
3.  **Integrate:** Open `main.py` and add your new function to the `tools` list to make the agent aware of its new capability.(Still empty)