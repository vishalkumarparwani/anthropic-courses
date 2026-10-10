#The Solution: Assistant Message Prefilling + Stop Sequences

#You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:


messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_messages(messages, "```json")

text = chat(messages, stop_squence=["```"])



#You might notice some extra newline characters in the response. These are easy to handle:
import json

# Clean up and parse the JSON
clean_json = json.loads(text.strip())



"""

"""