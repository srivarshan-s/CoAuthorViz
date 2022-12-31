def system_initialize(event):
    buffer = event["currentDoc"]
    return buffer, event["currentCursor"]


def move_cursor(event):
    return event["currentCursor"], False, None


def cursor_select(event):
    return True, event["cursorRange"]


def suggestion_close():
    pass


def suggestion_down():
    pass


def suggestion_get():
    pass


def suggestion_hover():
    pass


def suggestion_open():
    pass


def suggestion_reopen():
    pass


def suggestion_select():
    pass


def suggestion_up():
    pass


def text_delete(buffer, event, cursor_pos, cursor_select_flag, cursor_range):
    if cursor_select_flag:
        print("Cursor selection is performed!")
    else:
        buffer = list(buffer)
        buffer.pop(cursor_pos)
        buffer = ''.join(buffer)
    return buffer, event["currentCursor"], False, None


def text_insert(buffer, event, cursor_pos, cursor_select_flag, cursor_range):
    if cursor_select_flag:
        print("Cursor selection is performed!")
    else:
        insert_char = event["textDelta"]["ops"][1]["insert"]
        buffer = list(buffer)
        buffer.insert(cursor_pos, insert_char)
        buffer = ''.join(buffer)
    return buffer, event["currentCursor"], False, None
