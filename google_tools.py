# google_tools.py
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from langchain_core.tools import tool

TOKEN_FILE = "token.json"

def get_credentials():
    """Helper function to load user credentials from token.json."""
    if not os.path.exists(TOKEN_FILE):
        raise FileNotFoundError(f"{TOKEN_FILE} not found. Authentication is required.")
    return Credentials.from_authorized_user_file(TOKEN_FILE)

@tool
def create_calendar_event(
    summary: str, 
    start_datetime: str, 
    end_datetime: str, 
    description: str = "Created by AI Agent"
) -> str:
    """
    Creates a new event on the user's primary Google Calendar.

    Args:
        summary (str): The title or summary of the event.
        start_datetime (str): The start time in ISO 8601 format (e.g., '2025-08-22T15:00:00').
        end_datetime (str): The end time in ISO 8601 format (e.g., '2025-08-22T16:00:00').
        description (str, optional): A description for the event.
    """
    try:
        creds = get_credentials()
        service = build("calendar", "v3", credentials=creds)
        
        event_body = {
            "summary": summary,
            "description": description,
            "start": {"dateTime": start_datetime, "timeZone": "Asia/Kolkata"},
            "end": {"dateTime": end_datetime, "timeZone": "Asia/Kolkata"},
        }

        created_event = service.events().insert(calendarId="primary", body=event_body).execute()
        return f"Event created successfully! Link: {created_event.get('htmlLink')}"

    except Exception as e:
        return f"An error occurred: {e}"
    
# Add this to your google_tools.py file, below the create_calendar_event tool

@tool
def search_drive(query: str) -> str:
    """
    Searches for files in the user's Google Drive based on a query.
    
    The AI agent will use this to find files before reading them or sending them.
    The query can be a simple filename or part of a filename.

    Args:
        query (str): The search term to look for in the filenames.
    """
    try:
        creds = get_credentials()
        service = build("drive", "v3", credentials=creds)
        
        # Call the Drive v3 API
        results = (
            service.files()
            .list(q=f"name contains '{query}'", pageSize=5, fields="files(id, name)")
            .execute()
        )
        items = results.get("files", [])

        if not items:
            return f"No files found in Google Drive matching the query: '{query}'"
        
        # Format the results into a clean string for the agent to read
        file_list = "\n".join([f"- {item['name']} (ID: {item['id']})" for item in items])
        return f"Found the following files matching '{query}':\n{file_list}"

    except Exception as e:
        return f"An error occurred while searching Google Drive: {e}"    