'''
2: Write a Python program to calculate the number of days between two dates.
Sample dates : (20200702), (20200711)
'''
from datetime import datetime


def days_by_daterange(start_date, end_date):
    if not all([start_date, end_date]):
        print("Error: 'start_date' and 'end_date' both required!\n")
    if start_date >= end_date:
        print("Error: 'start_date' should be less than 'end_date'!\n")
    
    days_gap = (end_date - start_date).days
    print(f"Result : The days between {start_date} and {end_date} is = {days_gap}")


def main():
    while True:
        ans = input("You want to give date_rage(start and end dates) ? y/n ")
        if ans.lower().strip() == "y":
            start_date = input("Enter start_date (yyyymmdd): \n")
            end_date = input("Enter end_date (yyyymmdd): \n")
            try:
                start_date = datetime.strptime(start_date, "%Y%m%d").date()
                end_date = datetime.strptime(end_date, "%Y%m%d").date()
            except Exception as e:
                print(e.__str__())
                continue
        
        elif ans.lower().strip() == "n":
            start_date = "20200702"
            end_date = "20200711"
            print(f"Using start_date : {start_date} and end_date : {end_date}. \n")
            start_date = datetime.strptime("20200702", "%Y%m%d").date()
            end_date = datetime.strptime("20200711", "%Y%m%d").date()
        else:
            print("Please choose betwee : y(yes) or n(no)!")
            continue

        if start_date >= end_date:
            print("Error: 'start_date' should be less than 'end_date'!\n")
            continue
        break        
    
    days_gap = (end_date - start_date).days
    print(f"Result : The days between {start_date} and {end_date} is = {days_gap}")

if __name__ == "__main__":
    main()