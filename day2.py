import os

def calculate_directory_size(directory_path):
    max_file_name = ""
    max_file_size = 0
    total_size = 0
    
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            total_size += file_size 
            if file_size > max_file_size:  
                max_file_size = file_size
                max_file_name = file
                
    return total_size, max_file_name

directory_path = r"C:\Users\Seshagiri\Desktop\Handson\oop\src\oop"
directory_size, max_file_name = calculate_directory_size(directory_path)

print(f"The largest file is: {max_file_name}")
print(f"Total size of the directory '{directory_path}' is: {directory_size} bytes")