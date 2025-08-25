# test_tool.py (Corrected)

from google_tools import create_calendar_event, search_drive

print("--- Testing the Calendar Tool ---")

# 1. Package all your arguments into a single dictionary.
#    The keys of the dictionary MUST match the argument names in your tool function.
tool_input = {
    "summary": "AI Agent Test Event",
    "start_datetime": "2025-08-22T15:00:00",  # 3:00 PM today in Kanpur
    "end_datetime": "2025-08-22T16:00:00",    # 4:00 PM today
    "description": "This was created successfully by the LangChain tool!"
}

# 2. Call the tool using the .invoke() method and pass the single dictionary.
# result = create_calendar_event.invoke(tool_input)


# --- The rest of the script is the same ---
# print(f"Result: {result}")
# print("--- Test Complete ---")
# print("Check your Google Calendar for an event at 3:00 PM today!")

print("\n--- Testing the Drive Search Tool ---")

# Let's search for a file. Replace 'Test Document' with a real filename
# or part of a filename that exists in your Google Drive.
drive_query = {
    "query": "Resume" 
}

drive_result = search_drive.invoke(drive_query)
print(f"Result: {drive_result}")
print("--- Test Complete ---")