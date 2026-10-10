# Basic Streaming Implementation
#To enable streaming, add stream=True to your messages.create call:

messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model = model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)



#Simplified Text Streaming=======================================
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")


#Getting the Complete Message==================================== 
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass
    
    # Get the complete message for database storage
    final_message = stream.get_final_message()