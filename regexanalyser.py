import re

log_data = """
14.12.2002 13:05:06 App. 2435 Ziel 0221/2323458 245s
14.12.2002 13:05:06 App. 2435 Ziel xxxx/xxxx 245s
"""

# This function will process each line of the log file
def process_log_entry(entry: str):
    # Regular expression pattern to find phone numbers
    phone_pattern = re.compile(r'(\d{4})/(\d{7})')
    # Replace the phone number with 'xxxx/xxxx' while keeping the duration part unchanged
    modified_entry = phone_pattern.sub(r'xxxx/xxxx', entry)
    return modified_entry

# Splitting the log data into individual lines for processing
log_entries = log_data.strip().split('\n')

# Process each entry and collect the modified entries
modified_entries = [process_log_entry(entry) for entry in log_entries]

# Join the modified entries back into a single string to simulate writing to a file
modified_log_data = '\n'.join(modified_entries)
print(modified_log_data)
