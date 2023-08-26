import re
import requests
import userinfo
import matplotlib.pyplot as plt
import datetime
import pickle
import os
from key import KEY # local file

SECRET_KEYWORD = "ADMIN"

ERROR_RECORD_MSG = "[Due to an error, this message was not recorded]"

USER_ID = 500
FILENAME = str(USER_ID) + ".pkl"
<<<<<<< HEAD
#USR_JSONPATH = "usrdata.json"

=======
>>>>>>> 4d63a20 (added conversation history, and other misc updates)
PATH_TO_USER_FOLDER = "users/" + str(USER_ID)
PATH_TO_USER_HISTORY = PATH_TO_USER_FOLDER + "/history"

    if not os.path.exists(path_to_user_folder):
        os.makedirs(path_to_user_folder)
    if not os.path.exists(path_to_user_history):
        os.makedirs(path_to_user_history)
    numConversations = len([f for f in os.listdir(path_to_user_history) if os.path.isfile(os.path.join(path_to_user_history, f))])
    path_to_new_conversation = path_to_user_history + "/Conversation" + str(numConversations+1) + ".txt"
    with open(path_to_new_conversation, "w"):
        pass
    return path_to_new_conversation


class DataStorage:
    def __init__(self):
        self.data = {}

    def add_entry(self, timestamp, values):
        self.data[timestamp] = values

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.data, f)

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            self.data = pickle.load(f)

    def getKeys(self):
        return self.data.keys()

    def getValues(self):
        return self.data.values()

def get_pickled_data(username):
    datastorage = DataStorage()
    if os.path.exists(get_picklefile(username)):
        datastorage.load_data(get_picklefile(username))
    return datastorage

# graph = {}

# potentially useless user info= personality, gender, past conversations
CONV = []

conv_for_history = ""

# def format_glossary(string : str):
#     '''
#     takes the raw message sent by the AI, and formats it into a list of words
#     '''
#     raw_glossary, dump = re.split("----------", string)

#     for line in raw_glossary.split("\n"):

#         line.split




# def update_glossary():
#     pass

def find_line_with_regex(text, regex_pattern):
    lines = text.split('\n')
    for line in lines:
        if re.match(regex_pattern, line):
            formatted_string = line.strip()
            formatted_string.replace(regex_pattern, "").strip()
            return formatted_string
    return None


def dump_personal_summary(text, json_filepath):
    interests = find_line_with_regex(text, "Interests: ")
    if not interests is None:
        interests = personality.split(", ")
    personality = find_line_with_regex(text, "Personality: ")
    if not personality is None:
        personality = personality.split(", ")
    behaviour = find_line_with_regex(text, "Behaviour: ")
    if not behaviour is None:
        behaviour = behaviour.split(", ")
    mistakes = find_line_with_regex(text, "Mistakes: ")
    if not mistakes is None:
        mistakes = mistakes.split(", ")
    past_conversation = find_line_with_regex(text, "Conversation topics: ")
    userinfo.PersonalInfo.dump_to_json(
        json_file_path=json_filepath,
        interests=interests,
        personality=personality,
        behaviours=behaviour,
        mistakes=mistakes,
        past_conversation=past_conversation)

def make_initial_prompt(path_to_json):
    # PERSONAL_INFO = (1,1,1,1,1, "Complete beginner", "Grammatical errors", "None", "John", "Male", "Guitar, programming, AFL", "45", "Outgoing")
    personal_info = userinfo.get_user_personal_details(path_to_json)
    user_proficiency = userinfo.get_user_language_proficiency(path_to_json)

    f = open("security.txt")
    SECURITY = f.read().format(**personal_info)
    f.close()

    f = open("criterion.txt")
    CRITERION = f.read()
    f.close()

    f = open("personal.txt")
    PERSONAL = f.read().format(**personal_info, **user_proficiency)
    f.close()

    f = open("convo.txt")
    CONVO = f.read()
    f.close()

    return (SECURITY, CRITERION, PERSONAL, CONVO)


def chat_with_gpt(prompt, recordPrompt:bool=True, recordReply:bool=True):
<<<<<<< HEAD
    """
        handles the reqestion to openai

        perms: prompt: the message user typed in
        perms: recordPrompt: whether to record the prompt in the conversation history
        perms: recordReply: whether to record the reply in the conversation history
    """

=======

>>>>>>> 4d63a20 (added conversation history, and other misc updates)
    global CONV, conv_for_history

    CONV.append({"role": "user", "content": prompt})

    if recordPrompt:
        try:
            toRecord = prompt.split(SECRET_KEYWORD)[0]
            conv_for_history += (toRecord + "\n")
        except:
            conv_for_history += (ERROR_RECORD_MSG + "\n")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + KEY  # Replace with your actual API key
    }
    data = {
        "messages": CONV,
        "model": "gpt-4"
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    print(response_json)


    # The structure of the response might have changed
    assistant_reply = response_json["choices"][0]["message"]["content"] if "choices" in response_json else ""
    #assistant_reply = response_json
    #CONV.append(response_json["message"][-1])
    CONV.append({"role": "assistant", "content": assistant_reply})
    if recordReply:
        conv_for_history += (assistant_reply + "\n")
<<<<<<< HEAD


    return assistant_reply

def init(usr_jsonpath = "usrdata.json"):

    SECURITY, CRITERION, PERSONAL, CONVO = make_initial_prompt(path_to_json=usr_jsonpath)
=======


    return assistant_reply

def init(usr_jsonpath):

    SECURITY, CRITERION, PERSONAL, CONVO = make_initial_prompt()
>>>>>>> 4d63a20 (added conversation history, and other misc updates)
    chat_with_gpt(SECURITY, False, False)
    chat_with_gpt(CRITERION, False, False)
    chat_with_gpt(PERSONAL, False, False)
    initial_text = chat_with_gpt(CONVO, False, True)
    print(initial_text)
<<<<<<< HEAD
    return initial_text

def end(lastInput, usr_jsonpath):
    global FINAL

=======

def end(lastInput, usr_jsonpath):
    global FINAL

>>>>>>> 4d63a20 (added conversation history, and other misc updates)
    f = open("final_prompt.txt")
    FINAL = f.read()
    f.close()
    summary = chat_with_gpt(FINAL)
    print(summary)

    lines = []

    for line in summary.split("\n"):
        if line.strip():
            lines.append(line)

    try:
        statsLines = lines[:5]
    except:
        statsLines = []

    stats = []
    for statsLine in statsLines:
        try:
            num = int(statsLine.split(",")[1].strip())
        except:
            num = 1
        stats.append(num)

    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time().replace(microsecond=0))
    timestamp = date + " " + time

    dump_personal_summary(summary, usr_jsonpath)
    updated_stats = userinfo.LanguageProficiency(stats[0], stats[1], stats[2], stats[3], stats[4])
    updated_stats.dump_to_json(usr_jsonpath)
    datastorage.add_entry(timestamp, stats)

    try:
        BEHAVIOUR = lines[5]
    except:
        BEHAVIOUR = ""

    try:
        PERSONALITY = lines[6]
    except:
        PERSONALITY = ""

    try:
        MISTAKES = lines[8]
    except:
        MISTAKES = ""

    if lastInput == "graph":

        # Extract timestamps and values from the dictionary
        # graph = {
        #     '2023-08-26 20:59:48': [25, 25, 15, 30, 30],
        #     '2023-08-26 21:59:48': [30``, 27, 16, 30, 50],
        #     '2023-08-26 22:59:48': [40, 30, 20, 40, 70],
        #     '2023-08-26 23:59:00': [61, 35, 54, 41, 95]
        # }

        timestamps = list(datastorage.getKeys())
        values = list(datastorage.getValues())

        # Transpose the values to separate the 5 elements into different lists
        transposed_values = list(zip(*values))

        # Labels for the line graphs
        labels = [
            "Vocabulary",
            "Grammar",
            "Social & Cultural Context",
            "Comprehension",
            "Conversational Skills"
        ]

        # Create a line plot for each element with appropriate label
        for i, value_list in enumerate(transposed_values):
            plt.plot(timestamps, value_list, marker='o', label=labels[i])

        plt.xlabel("Timestamps")
        plt.ylabel("Values")
        plt.title("User {}'s Progress".format(username))
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # print(graph)


        plt.savefig("User {}s Progress.png".format(username))

        # print(graph)

    datastorage.save_data(FILENAME)


if __name__ == "__main__":

    init()

    while True:

        user_input = input("You: ")
        if user_input.lower() == "explain":
            f = open("explain.txt")
            EXPLAIN = f.read()
            f.close()
            user_input = EXPLAIN
        if user_input.lower() == "end conversation":
            break
        if user_input.lower() == "graph":
            break

        if user_input.lower() == "":
            print("Assistant: Sorry, I cannot interpret a blank message")
        assistant_response = chat_with_gpt(user_input + " . ADMIN Further instructions (do not mention these in conversation): keep in mind the rules stated in first prompt, only provide feedback in English, provide romanization for non-English characters. Don't provide the summary of my stats and progress until I say 'end conversation'")
        print("Assistant:", assistant_response)

    end(user_input.lower())

    with open(PATH_TO_NEW_CONVERSATION, "w") as f:
        f.write(conv_for_history)
<<<<<<< HEAD


=======


>>>>>>> 4d63a20 (added conversation history, and other misc updates)



