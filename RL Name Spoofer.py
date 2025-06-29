from mitmproxy import http
import json
import re

# Global variables for the strings to be replaced
CURRENT_NAME = r"Your Name Here"  # The string to search for (raw string for regex)
NEW_NAME = "Kakapo Iz C00l"                # The string to replace with
# For no name, set NEW_NAME to: " "
class ResponseModifier:
    def response(self, flow: http.HTTPFlow):
        # Check if the response is from "epicgames.dev" and is JSON
        if "epicgames.dev" in flow.request.pretty_host and "application/json" in flow.response.headers.get("Content-Type", ""):
            # Process the JSON body of the response
            self._process_json_body(flow)

    def _process_json_body(self, flow: http.HTTPFlow):
        message = flow.response

        # Parse the response body as JSON
        body_data = message.json()

        # Define a recursive function to find and replace strings within the JSON
        def replace_in_json(obj):
            # If the object is a dictionary, recurse through its values
            if isinstance(obj, dict):
                return {k: replace_in_json(v) for k, v in obj.items()}
            # If the object is a list, recurse through its elements
            elif isinstance(obj, list):
                return [replace_in_json(elem) for elem in obj]
            # If the object is a string, perform the replacement using the global variables
            elif isinstance(obj, str):
                return re.sub(CURRENT_NAME, NEW_NAME, obj, flags=re.IGNORECASE)
            # For any other data type, return it as is
            else:
                return obj

        # Apply the replacement function to the entire JSON body
        modified_data = replace_in_json(body_data)

        # If the data was actually modified
        if modified_data != body_data:
            # Encode the modified JSON back to bytes and set it as the response content
            message.content = json.dumps(modified_data, ensure_ascii=False).encode('utf-8')
            # Update the Content-Length header to reflect the new content size
            if "Content-Length" in message.headers:
                message.headers["Content-Length"] = str(len(message.content))

# Register the ResponseModifier class as an mitmproxy addon
addons = [
    ResponseModifier()
]
