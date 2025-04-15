import os
import glob
import datetime

class MaxFile:
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError(f"The path '{path}' does not exist.")
        self.path = path

    def getMaxSizeFile(self, n=1):
        files = []
        for dirpath, _, filenames in os.walk(self.path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                if os.path.isfile(full_path):
                    files.append((filename, os.path.getsize(full_path)))
        files.sort(key=lambda x: x[1], reverse=True)
        return [f[0] for f in files[:n]]

    def get_newer_files(self, since_date):
        pattern = f"{self.path}"
        result = []
        for file in glob.glob(pattern, recursive=True):
            if os.path.isfile(file):
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file)).date()
                if mtime > since_date:
                    result.append(os.path.basename(file))
        return result

# Example usage
fs = MaxFile(".")
print(fs.get_largest_files(2))  # Prints the names of the two largest files
print(fs.get_newer_files(datetime.date(2025, 4, 1)))  
