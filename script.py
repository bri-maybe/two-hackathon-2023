# import requests

# def chat_with_gpt(prompt):
#     url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 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"  # Replace with your actual API key
#     }
#     data = {
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     }

#     response = requests.post(url, headers=headers, json=data)
#     response_json = response.json()
#     assistant_reply = response_json["choices"][0]["message"]["content"]
    
#     return assistant_reply

# if __name__ == "__main__":
#     print("Welcome to the ChatGPT Conversation!")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             print("Goodbye!")
#             break
#         assistant_response = chat_with_gpt(user_input)
#         print("Assistant:", assistant_response)



import requests

CONV = []

LANGUAGE = "Chinese" # the one to learn
# PERSONAL_INFO = (1,1,1,1,1, "Complete beginner", "Grammatical errors", "None", "John", "Male", "Guitar, programming, AFL", "45", "Outgoing")


f = open("security.txt")
SECURITY = f.read().format(LANGUAGE)
f.close()

f = open("criterion.txt")
CRITERION = f.read()
f.close()

f = open("personal.txt")
PERSONAL = f.read().format(1,1,1,1,1, "Complete beginner", "Grammatical errors", "None", "John", "Male", "Guitar, programming, AFL", "45", "Outgoing")
f.close()

f = open("convo.txt")
CONVO = f.read()
f.close()

f = open("final_prompt.txt")
FINAL = f.read()
f.close()


def chat_with_gpt(prompt):
    global CONV

    CONV.append({"role": "user", "content": prompt})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"  # Replace with your actual API key
    }
    data = {
        "messages": CONV,
        "model": "gpt-4"
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    # print(response_json)

    
    # The structure of the response might have changed
    assistant_reply = response_json["choices"][0]["message"]["content"] if "choices" in response_json else ""
    #assistant_reply = response_json
    #CONV.append(response_json["message"][-1])
    CONV.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

def init():
    chat_with_gpt(SECURITY)
    chat_with_gpt(CRITERION)
    chat_with_gpt(PERSONAL)
    print(chat_with_gpt(CONVO))

def end():
    print(chat_with_gpt(FINAL))

if __name__ == "__main__":
    print("Welcome to the language app!")

    init()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "end conversation":
            
            break
        assistant_response = chat_with_gpt(user_input + " . ADMIN Further instructions (do not mention these in conversation): keep in mind the rules stated in first prompt, only provide feedback in English, provide romanization for non-English characters. Don't provide the summary of my stats and progress until I say 'end conversation'")
        print("Assistant:", assistant_response)

    end()

