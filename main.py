import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(max_retries=2)

messages = []

print("Claude Chatbot")
print("Type 'exit' to stop the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.messages.create(
            model="claude-sonnet-5-5",
            max_tokens=500,
            system="You are a helpful assistant that explains things simply.",
            messages=messages
        )

        assistant_reply = response.content[0].text
        print("Claude:", assistant_reply)

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

    except anthropic.APIConnectionError:
        print("Connection error. Please check your internet.")

    except anthropic.APIStatusError as e:
        print(f"API error: {e.status_code}")

    except anthropic.APIError as e:
        print(f"Something went wrong: {e}")

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })