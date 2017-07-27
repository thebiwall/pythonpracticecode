def age100(age_input):
    import datetime
    today = datetime.date.today()
    year_cur = today.year
    if age_input <= 0:
        print("Incorrect age entered")
    else:
        year_diff = (year_cur - 2000)
        return 2000 + (100 - age_input) + year_diff

age_input = int(input("Please enter your age"))
print( " You will turn 100 in the year ", age100(age_input))
