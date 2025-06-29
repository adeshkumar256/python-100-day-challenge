"""For creating 100 directories and files"""
import os

for i in range(1, 101):
    folder_name = f"Day {i}"
    os.makedirs(folder_name, exist_ok=True)
    # old_file_path = os.path.join(folder_name, f"day_{i}.py")
    # if os.path.exists(old_file_path):
    #     os.remove(old_file_path)
    file_path = os.path.join(folder_name, f"day{i}.py")
    with open(file_path, "w") as f:
        f.write(f"# Day {i} challenge\n")
