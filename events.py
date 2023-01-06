import pandas as pd
import nltk
import numpy as np


def init_df(buffer, events):
    df = pd.DataFrame()
    df["text_buffer"] = buffer
    df["events"] = events
    return df


def extract_sent(df):
    sentence_buffer = []
    num_sentences = []

    for text in df["text_buffer"]:
        sentences = nltk.tokenize.sent_tokenize(text)
        sentence_buffer.append(sentences)
        num_sentences.append(len(sentences))

    df["sentences"] = sentence_buffer
    df["num_sentences"] = num_sentences

    return df


def extract_event_name(df):
    df["event_name"] = df["events"].apply(lambda x: x["eventName"])
    return df


def correct_sent_num(df):
    df = df.groupby("num_sentences", group_keys=True).apply(lambda x: x)
    df = df.sort_index()

    num_sentences = np.array(df["num_sentences"])
    event_names = np.array(df["event_name"])

    start_idx = 0
    select_flag = False

    for idx, event in enumerate(event_names):
        if event == "suggestion-get":
            start_idx = idx
        if event == "suggestion-select":
            select_flag = True
        if select_flag and event == "text-insert":
            if num_sentences[start_idx] == num_sentences[idx]:
                end_idx = idx + 1
            elif num_sentences[start_idx] < num_sentences[idx]:
                end_idx = idx
            for i in range(start_idx, end_idx):
                num_sentences[i] += 1
            select_flag = False

    df["num_sentences"] = num_sentences

    return df


def generate_event_seq(buffer, events):
    df = init_df(buffer, events)
    df = extract_sent(df)
    df = extract_event_name(df)
    print(df.head())
