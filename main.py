from utils import read_file


def main():
    dataset_dir = "./coauthor-v1.0/"
    event = read_file(dir=dataset_dir, index=0)
    print(len(event))


if __name__ == "__main__":
    main()
