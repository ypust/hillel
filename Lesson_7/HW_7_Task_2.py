import os

path = input('Enter the directory path to search in: ')

if not os.path.exists(path):
    path = os.path.abspath(os.sep)

file_count = 0
dir_count = 0

smallest_file = None
largest_file = None
smallest_size = float('inf')
largest_size = 0

shortest_file = None
longest_file = None
shortest_name_len = float('inf')
longest_name_len = 0

for root, dirs, files in os.walk(path):
    dir_count += len(dirs)
    file_count += len(files)

    for filename in files:
        # Find smallest and largest files
        file_path = os.path.join(root, filename)
        file_size = os.path.getsize(file_path)
        if file_size < smallest_size:
            smallest_size = file_size
            smallest_file = file_path
        if file_size > largest_size:
            largest_size = file_size
            largest_file = file_path

        # Find shortest and longest file names
        file_path = os.path.join(root, filename)
        file_name_len = len(filename)
        if file_name_len < shortest_name_len:
            shortest_name_len = file_name_len
            shortest_file = file_path
        if file_name_len > longest_name_len:
            longest_name_len = file_name_len
            longest_file = file_path

print(f"Total number of directories: {dir_count}")
print(f"Total number of files: {file_count}")

print(f"Smallest file: {smallest_file} ({smallest_size} bytes)")
print(f"Largest file: {largest_file} ({largest_size} bytes)")

print(f"Shortest file name: {shortest_file} ({shortest_name_len} characters)")
print(f"Longest file name: {longest_file} ({longest_name_len} characters)")
