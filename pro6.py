'''
6: Write a Python program to convert an array to an array of machine values and
return the bytes representation.
'''
import array, binascii


def main():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # define an array
    arr = array.array("i", num_list)
    # covert to bytes
    arr_bytes = arr.tobytes()
    arr_of_bytes = binascii.hexlify(arr_bytes)
    return arr_of_bytes


if __name__ == "__main__":
    print("arr_of_bytes:", main())