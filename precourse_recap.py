cohort = "SR10"
first_name = "Mike"
last_name = "Langley"
cups_before_lunch = 4
cups_after_lunch = 3
max_recommended_coffee = 6

def full_name(first_name, last_name, cohort):
    return f"{first_name} {last_name} from {cohort}"


def daily_coffee(cups_before_lunch, cups_after_lunch):
    return cups_before_lunch + cups_after_lunch


name = full_name(first_name, last_name, cohort)
coffee_consumed = daily_coffee(cups_before_lunch,  cups_after_lunch)

print(f"{name} consumes {coffee_consumed} cups of coffee a day")

if coffee_consumed > max_recommended_coffee:
    print(f"Yay {first_name}, ride that coffee train!")
else:
    print(f"How does {first_name} stay awake?")

