from utils import load_sessions, read_session
from events import *


def main():

    sessions = load_sessions()
    events = read_session(sessions[0])

    text_buffer = []
    cursor_pos = 0

    for event in events:
        if event["eventName"] == "system-initialize":
            system_initialize()
        if event["eventName"] == "cursor-backward":
            cursor_backward()
        if event["eventName"] == "cursor-forward":
            cursor_forward()
        if event["eventName"] == "cursor-select":
            cursor_select()
        if event["eventName"] == "suggestion-close":
            suggestion_close()
        if event["eventName"] == "suggestion-down":
            suggestion_down()
        if event["eventName"] == "suggestion-get":
            suggestion_get()
        if event["eventName"] == "suggestion-hover":
            suggestion_hover()
        if event["eventName"] == "suggestion-open":
            suggestion_open()
        if event["eventName"] == "suggestion-reopen":
            suggestion_reopen()
        if event["eventName"] == "suggestion-select":
            suggestion_select()
        if event["eventName"] == "suggestion-up":
            suggestion_up()
        if event["eventName"] == "text-delete":
            text_delete()
        if event["eventName"] == "text-insert":
            text_insert()


if __name__ == "__main__":
    main()
