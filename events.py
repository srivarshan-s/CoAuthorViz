def system_initialize(event):
    buffer = event["currentDoc"]
    return buffer, event["currentCursor"]


def cursor_backward():
    pass


def cursor_forward():
    pass


def cursor_select():
    pass


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


def text_delete():
    pass


def text_insert(buffer, event, cursor_pos):
    if len(event["textDelta"]["ops"]) == 2:
        insert_char = event["textDelta"]["ops"][1]["insert"]
        buffer = list(buffer)
        buffer.insert(cursor_pos, insert_char)
        buffer = ''.join(buffer)
    return buffer, event["currentCursor"]
