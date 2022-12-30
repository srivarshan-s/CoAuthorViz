from utils import load_sessions, read_session


def main():

    sessions = load_sessions()
    events = read_session(sessions[0])

    text_buffer = []
    cursor_pos = 0

    for event in events:
        if event["eventName"] == "system-initialize":
            print("system-initialize")
        if event["eventName"] == "cursor-backward":
            print("cursor-backward")
        if event["eventName"] == "cursor-forward":
            print("cursor-forward")
        if event["eventName"] == "cursor-select":
            print("cursor-select")
        if event["eventName"] == "suggestion-close":
            print("suggestion-close")
        if event["eventName"] == "suggestion-down":
            print("suggestion-down")
        if event["eventName"] == "suggestion-get":
            print("suggestion-get")
        if event["eventName"] == "suggestion-hover":
            print("suggestion-hover")
        if event["eventName"] == "suggestion-open":
            print("suggestion-open")
        if event["eventName"] == "suggestion-reopen":
            print("suggestion-reopen")
        if event["eventName"] == "suggestion-select":
            print("suggestion-select")
        if event["eventName"] == "suggestion-up":
            print("suggestion-up")
        if event["eventName"] == "text-delete":
            print("text-delete")
        if event["eventName"] == "text-insert":
            print("text-insert")


if __name__ == "__main__":
    main()
