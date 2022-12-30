import os
import json


def read_file(dir, index):
    paths = [
        os.path.join(dir, path) 
        for path in os.listdir(dir) 
        if path.endswith('jsonl')
    ]
    author_file = read_writing_session(paths[index])
    return author_file


def read_writing_session(path):
    events = []
    with open(path, 'r') as f:
        for event in f:
            events.append(json.loads(event))
    # print(f'Successfully read {len(events)} events in a writing session from {path}')
    return events

