import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the permissions your app will request from the user.
# For our multi-agent chatbot, we need to read/write to all three services.
SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly", # View files in Drive
    "https://www.googleapis.com/auth/calendar",         # View and edit events on all your calendars
    "https://www.googleapis.com/auth/gmail.modify"      # Read, compose, send, and permanently delete all your email from Gmail
]

# The name of your application's master key file from Part A.
CLIENT_SECRETS_FILE = "credentials.json"
# The name of the file that will store the user's specific permission token.
TOKEN_FILE = "token.json"

def perform_authentication():
    """
    Executes the user consent flow to generate or refresh user credentials.
    This is the core of the authentication system.
    """
    creds = None
    
    # The TOKEN_FILE stores the user's access and refresh tokens.
    # It's created automatically after the first successful authorization.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no (valid) credentials, trigger the user consent flow.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # If the token is just expired, refresh it without user interaction.
            print("Refreshing access token...")
            creds.refresh(Request())
        else:
            # This is the main flow for the first-time user.
            print("No valid credentials found. Starting authentication flow...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            # This line starts a local web server and opens a browser window.
            creds = flow.run_local_server(port=0)
        
        # Save the new/refreshed credentials to the token file for future use.
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
        print(f"Credentials saved to {TOKEN_FILE}")
        
    print("Authentication successful and credentials are valid.")
    return creds

if __name__ == "__main__":
    print("--- Running Authentication Setup ---")
    perform_authentication()
    print("--- Setup Complete ---")
    print(f"You should now have a '{TOKEN_FILE}' in your project directory.")
    print("You can now proceed to create and use your API tools.")