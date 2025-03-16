def calculate_gross_pay(hourly_rate, hours_worked):
    return hourly_rate * hours_worked

if __name__ == "__main__":
    try:
        hourly_rate = float(input("Enter hourly Pay rate: "))
        hours_worked = float(input("Enter hours worked: "))

        gross_pay = calculate_gross_pay(hourly_rate, hours_worked)

        print("Gross Pay: ${:,.2f}".format(gross_pay))

    except ValueError:
        print("Error: Please enter valid numeric values for hourly rate and hours worked.")
