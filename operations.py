def system_init(event):
    buffer = event["currentDoc"]
    return buffer, event["currentCursor"]

def text_insert(text_buffer, cursor, event):
    insert_char = event["textDelta"]["ops"][1]["insert"]
    if len(text_buffer) == 0:
        buffer = str(insert_char)
    else:
        buffer = text_buffer[-1]
        if (cursor+1) >= len(buffer):
            buffer += insert_char
        else:
            buffer = list(buffer)
            buffer.insert(cursor, insert_char)
            buffer = ''.join(buffer)
    return buffer, event["currentCursor"]
