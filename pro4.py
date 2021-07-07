# 4: Write a Python program to sort a list of dictionaries using Lambda.


def main():
    mob_list = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2','color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
        ]

    lamb_fun = lambda li : int(li.get("model", 0))
    result = sorted(mob_list, key=lamb_fun, reverse=True)
    print(result)


if __name__ == "__main__":
    main()