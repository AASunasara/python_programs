# 1: Write a Python program to read a file line by line and store it into a list.


def read_file(f_path):
    # read file and store line by line into list
    result = {}
    try:
        data = open(f_path, "r").readlines()
        result["data"] = [line.strip() for line in data if line.strip()]
        result["error"] = False
    except Exception as e:
        result["error"] = e.__str__()
    return result


def main():
    while True:
        # ask if user want to give any file
        ans = input("You want to give file path? y/n : ")
        
        if ans.lower().strip() == "y":
            file_path = input("Please enter the file location : \n")
            res = read_file(file_path)
            if res["error"]:
                print("Error :", res["error"])
                continue
            else:
                print("Result :", res["data"])
                break
        
        elif ans.lower().strip() == "n":
            file_path = "files/pro1_file.txt"
            print("Here 'pro1_file.txt' file will be used.\n")
            res = read_file(file_path)
            print("Result :", res["data"])
            break
        
        else:
            print("Please choose betwee : y(yes) or n(no)!")
            continue



if __name__ == "__main__":
    main()