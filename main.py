import os
import time

from utils import load_sessions, read_session, read_file
from operations import build_text


def main():

    sessions = load_sessions()
    # 7c1e066d0c9c4901921cab117a0b7e73.jsonl
    events = read_file("7c1e066d0c9c4901921cab117a0b7e73.jsonl")
    # events = read_file("6a0e4a84b6624948b9373a84488399cd.jsonl")
    # events = read_session(sessions[0])

    text_buffer = []

    for event in events:
        buffer = build_text(text_buffer, event)
        text_buffer.append(buffer)
        os.system('clear')
        print(buffer)
        time.sleep(0.001)

    os.system('clear')
    print(text_buffer[-1])
    print(len(text_buffer), len(events))


if __name__ == "__main__":
    main()
