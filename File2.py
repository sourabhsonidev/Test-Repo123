
import re

def sanitize_name(name, max_length=100):
    """
    Sanitize a name by removing any characters that are not alphanumeric,
    spaces, hyphens, apostrophes, or periods. Also truncates the name if it
    exceeds the specified maximum length.
    """
    # Use a regular expression to keep only allowed characters
    sanitized = re.sub(r'[^a-zA-Z0-9\s\-\'\.]', '', name)
    # Truncate the name if it exceeds the maximum length
    return sanitized[:max_length]
