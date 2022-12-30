from utils import read_file
from operations import system_init, text_insert


def main():
    dataset_dir = "./coauthor-v1.0/"
    author_file = read_file(dir=dataset_dir, index=0)
    text_buffer = []
    cursor_pos = 0
    for event in author_file:
        event_name = event["eventName"]
        buffer = str("")
        if event_name == "system-initialize":
            buffer, cursor_pos = system_init(event)
        if event_name == "text-insert":
            buffer, cursor_pos = text_insert(text_buffer, cursor_pos, event)
        text_buffer.append(buffer)
    print(text_buffer)


if __name__ == "__main__":
    main()
