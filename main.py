import os

dataset_dir = "./coauthor-v1.0/"

paths = [
    os.path.join(dataset_dir, path) 
    for path in os.listdir(dataset_dir) 
    if path.endswith('jsonl')
]

print(f'Successfully downloaded {len(paths)} writing sessions in CoAuthor!')
