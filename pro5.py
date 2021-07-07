'''
5: Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space.
'''


def main():
    data_file = open("files/pro5_file.txt", "r").readlines()
    count = 0
    for line in data_file:
        words = line.split()
        for word in words:
            sep_words = word.split(",")
            sep_words = [word for word in sep_words if word.strip()]
            count += len(sep_words)

    return count


if __name__ == "__main__":
    print(main())
