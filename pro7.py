'''
7: Write a script which can read the files line by line with .log ext and print it into a
file , while printing the data from the suffix with present date and time of the system.
'''
from datetime import datetime


file_paths = (
    "files/pro7_logs/test.log",
    "files/pro7_logs/test-1.log",
    "files/pro7_logs/test2.log"
)

for path in file_paths:
    # read file
    log_file = open(path, "r").readlines()

    for index in range(len(log_file)):
        try:
            # extract the suffix
            suffix = log_file[index].split()[:2]
            datetime.strptime(suffix[0]+suffix[1], "%m-%d%H:%M:%S.%f")
            del log_file[index]
        except Exception as e:
            pass
    
    # clean the lines
    log_file = [line for line in log_file if line.strip()]

    with open("files/pro7_logs/log_file.txt", "a") as main_file:
        main_file.writelines(log_file)
