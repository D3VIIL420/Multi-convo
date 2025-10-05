import json

print("\n--- S A I I M FACEBOOK TOOL SETUP ---\n")
token_file = input("Enter Token File Path: ")
thread_id = input("Enter Facebook Thread ID: ")
prefix = input("Enter The Haters Nam: ")
message_file = input("Enter message file path: ")
delay = input("Enter Delay Between Messages (in Seconds): ")

config = {
    "token_file": token_file.strip(),
    "thread_id": thread_id.strip(),
    "prefix": prefix.strip(),
    "message_file": message_file.strip(),
    "delay": delay.strip()
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print("\n[+] Configuration saved successfully!")
print("[*] Use main.sh to run the tool.")
