import os
import sys
import time

from utils import read_file
from operations import build_text


def main():

    # # 7c1e066d0c9c4901921cab117a0b7e73.jsonl
    # events = read_file("7c1e066d0c9c4901921cab117a0b7e73.jsonl")
    # # events = read_file("6a0e4a84b6624948b9373a84488399cd.jsonl")
    # # events = read_session(sessions[0])

    # text_buffer = []

    # for event in events:
    #     buffer = build_text(text_buffer, event)
    #     text_buffer.append(buffer)
    #     # os.system('clear')
    #     # print(buffer)
    #     # time.sleep(0.001)

    # # os.system('clear')
    # # print(text_buffer[-1])
    # # print(len(text_buffer), len(events))

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = "coauthor-v1.0/7c1e066d0c9c4901921cab117a0b7e73.jsonl"

    try:
        events = read_file(file_name)
    except:
        print("Invalid file path!")
        sys.exit()

    text_buffer = []

    for event in events:
        


if __name__ == "__main__":
    main()
