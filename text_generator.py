import random
import pandas as pd
from datetime import datetime, timedelta

human_phrases = ["hey what's up?", "lol that's crazy", "idk man", "brb", "you there?", "sounds good",
    "same here", "let's goooo", "what do you mean?", "hahahaha", "i'm eating rn", "come get me", "Tell me about yourself"
]

bot_phrases = [
    "Hello. How may I assist you today?", "Please provide your account number.",
    "Thank you for contacting support.", "This request has been received.",
    "I will now escalate this issue.", "Your issue has been logged in the system."
]

def generate_text(n_messages=400):
    logs = []
    base_time = datetime.now()
    for i in range(n_messages):
        is_bot = random.random() < 0.5
        sender_type = "bot" if is_bot else "human"
        message = random.choice(bot_phrases if is_bot else human_phrases)
        timestamp = base_time + timedelta(seconds=random.randint(1, 300))
        user_id = f"{sender_type}_{random.randint(1, 5)}"
        logs.append({
            "timestamp": timestamp.isoformat(),
            "user_id": user_id,
            "sender_type": sender_type,
            "message": message
        })
        base_time = timestamp
    return pd.DataFrame(logs)

df = generate_text()
df.to_csv("synthetic_chat.csv", index=False)
print(df.head())