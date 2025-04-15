from datetime import datetime
from pkg_file import File

fs = File(".")
print(fs.getMaxSizeFile(2))  # Prints the names of the two largest files
print(fs.getLatestFiles(datetime(2018, 2, 1).date()))  # Prints files modified after Feb 1, 2018


