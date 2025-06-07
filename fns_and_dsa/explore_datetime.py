from datetime import datetime, timedelta

def display_current_datetime():
    """
    Fetches and prints the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """
    Calculates and prints the date 'days' days from now in YYYY-MM-DD format.
    """
    future_date = datetime.now() + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: display current date & time
    display_current_datetime()

    # Part 2: prompt for days and calculate future date
    days_str = input("Enter the number of days to add to the current date: ")
    try:
        days = int(days_str)
    except ValueError:
        raise ValueError("Invalid input. Please enter an integer number of days.")
    calculate_future_date(days)

if __name__ == "__main__":
    main()