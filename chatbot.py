import requests

api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual OpenAI API key


def chat_with_bot():
    messages = [
        {'role': 'system', 'content': 'You are a helpful chatbot.'}
    ]
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        messages.append({'role': 'user', 'content': user_input})
        response_json = get_openai_response(messages)
        if response_json is None:
            print("Chatbot: Sorry, something went wrong. Please try again.")
            continue

        assistant_message = response_json['choices'][0]['message']['content'].strip()
        print("Chatbot:", assistant_message)
        messages.append({'role': 'assistant', 'content': assistant_message})


def get_openai_response(messages):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': messages
    }
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
    except requests.RequestException as exc:
        print(f"Chatbot error: {exc}")
        return None
    except ValueError:
        print("Chatbot error: Invalid JSON response from API.")
        return None

    if 'choices' not in response_json or not response_json['choices']:
        print("Chatbot error: Unexpected response format from API.")
        return None

    return response_json


if __name__ == "__main__":
    chat_with_bot()
