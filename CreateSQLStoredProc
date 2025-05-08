from google import genai
from google.genai.types import HttpOptions, Part

def extract_StoredProc(paragraph):
    
    lines = paragraph.splitlines()
    start_index = -1
    end_index = -1

    for i, line in enumerate(lines):
      if line.strip().startswith("-- Stored Procedure Definition"):                        
        start_index = i + 1  # Start after the "BEGIN" line
      elif line.strip().startswith("END"):
        end_index = i
        break  # Stop searching after finding "GO"

    if start_index != -1 and end_index != -1 and start_index < end_index:
      extracted_lines = lines[start_index:end_index+1]
      return "\n".join(extracted_lines)
    else:
      return ""

def extract_CALLQuery(paragraph):
  
  lines = paragraph.splitlines()
  for line in lines:
    if line.strip().startswith("CALL"):
      return line
  return None

# client = genai.Client(http_options=HttpOptions(api_version="v1"))
client = genai.Client(api_key="AIzaSyB7D6jTD2tJKjt-YqjwyQBcam3MD_XRIUQ")

file = client.files.upload(file='/Users/kenyetzer/documents/dbschema.txt')
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    
    contents=['create a stored procedure for MySQL called testSP that returns Revenue,Units Sold given Product Name and Order Date and create a CALL query to test the new stored procedure where product name = abc and order_date = 2022-01-01', file]
)

try:
        # Open the file in write mode
        file = open('/Users/kenyetzer/storedproc.sql', 'w')

        storproc = extract_StoredProc(response.text);
        callstorproctest = extract_CALLQuery(response.text);

        print(storproc)
        print(callsstorproctest)

        # print(f"File '{filename}' created and written successfully.")

except Exception as e:
        print(f"An error occurred: {e}")

finally:
        # Close the file
        if 'file' in locals():  # Check if the file was successfully opened
            file.close()
