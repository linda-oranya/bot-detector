import pandas as pd
import string

def extract_features(df):
    def num_punct(text):
        return sum(1 for ch in text if ch in string.punctuation)

    def has_link(text):
        return int("http" in text or "www" in text)

    df["msg_length"] = df["message"].str.len()
    df["word_count"] = df["message"].str.split().apply(len)
    df["avg_word_length"] = df["msg_length"] / df["word_count"].replace(0, 1)
    df["num_punct"] = df["message"].apply(num_punct)
    df["contains_link"] = df["message"].apply(has_link)
    df["is_question"] = df["message"].str.endswith("?").astype(int)

    return df

df = pd.read_csv("synthetic_chat.csv")
X = extract_features(df)
y = (df["sender_type"] == "bot").astype(int)

X.to_csv("processed/features.csv", index=False)
y.to_csv("processed/labels.csv", index=False)

