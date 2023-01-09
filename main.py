import os
import sys
import time

from utils import read_file, read_id
from operations import build_text
from events import generate_event_seq
from summary import stats, print_summary_stats
from graph import draw_graph


# Function to generate entire text buffer from the event sequence
def generate_buffer(events):
    text_buffer = []
    for event in events:
        buffer = build_text(text_buffer, event)
        text_buffer.append(buffer)
    return text_buffer


# Function to play the text buffer
def play(buffer, speed='fast'):
    speed_dict = {
        "fast": 0.001,
        "medium": 0.01,
        "slow": 0.1,
        "instant": True,
    }
    if speed_dict[speed] == True:
        print(buffer[-1])
    else:
        for text in buffer:
            os.system('clear')
            print(text)
            time.sleep(speed_dict[speed])


def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = "coauthor-v1.0/7c1e066d0c9c4901921cab117a0b7e73.jsonl"
    try:
        events = read_file(file_name)
    except:
        print("Invalid file path!")
        sys.exit()
    text_buffer = generate_buffer(events)
    play(buffer=text_buffer, speed="instant")
    event_seq_dict = generate_event_seq(buffer=text_buffer, events=events)
    sentence_metrics, api_metrics = stats(event_seq_dict)
    print_summary_stats(event_seq_dict)
    file_id = read_id(file_name)
    draw_graph(event_seq_dict, name=file_id)


if __name__ == "__main__":
    main()
