def exec_ops(original_text, ops):

    new_text = ""

    # for idx, op in enumerate(ops):
    for op in ops:

        # Retain
        if 'retain' in op:
            cursor_pos = op['retain']
            retained_text = original_text[:cursor_pos]
            original_text = original_text[cursor_pos:]
            new_text += retained_text

        # Insert
        elif 'insert' in op:
            insert_text = op['insert']
            new_text += insert_text

        # Delete
        elif 'delete' in op:
            idx_del = op['delete']

            if original_text:
                original_text = original_text[idx_del:]
            else:
                new_text = new_text[:-idx_del]

        # Ignore other ops
        else:
            print('Ignore other operations:', op)
            pass

    final_text = new_text + original_text
    return final_text


def build_text(text_buffer, event):

    if len(text_buffer) == 0:
        text = event["currentDoc"].strip()
        return text

    if "ops" not in event["textDelta"]:
        return text_buffer[-1]

    ops = event["textDelta"]["ops"]
    text = exec_ops(text_buffer[-1], ops)

    return text
