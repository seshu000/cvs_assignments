#Given a directory, find out the file Name having max size recursively
import os
def calculate_dir_size(dir_path):
    max_file_name = ""
    max_file_size = 0
    total_size = 0
    
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            total_size += file_size 
            if file_size > max_file_size:  
                max_file_size = file_size
                max_file_name = file
                
    return total_size, max_file_name

dir_path = r"C:\Users\Seshagiri\Desktop\Handson\oop\src\oop"
dir_size, max_file_name = calculate_dir_size(dir_path)

print(f"The largest file is: {max_file_name}")
print(f"Total size of the directory '{dir_path}' is: {dir_size} bytes")




'''Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)'''

from pathlib import Path

def dump_files():
    folder = Path(r"C:\Users\Seshagiri\desktop\handson")
    output_file = folder / "combined_output.txt"
    if not folder.is_dir():
        print("NO folder")
        return
    content = ""
    for path in folder.rglob("*.txt"):
        if path == output_file:
            continue
        try:
            content += path.read_text() + "\n"
        except:
            print(path)
    output_file.write_text(content)
    print(output_file.read_text())
    
dump_files()


