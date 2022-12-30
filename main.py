import os
import json


def load_sessions():
    dataset_dir = './coauthor-v1.0'
    sessions = [
        os.path.join(dataset_dir, path)
        for path in os.listdir(dataset_dir)
        if path.endswith('jsonl')
    ]
    print(
        f'Successfully downloaded {len(sessions)} writing sessions in CoAuthor!')
    return sessions

def read_session(session):
    events = []
    with open(session, 'r') as f:
        for event in f:
            events.append(json.loads(event))
    print(f'Successfully read {len(events)} events in a writing session from {session}')
    return events

def main():
    sessions = load_sessions()
    events = read_session(sessions[0])
    print(events[0])


if __name__ == "__main__":
    main()
