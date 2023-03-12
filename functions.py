import random


def make_week_schedule():

    vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    meal_schedule = {}

    while vegan_meals:
        random_item = random.choice(vegan_meals)
        day = weekdays[0]
        meal_schedule[day] = random_item
        weekdays.remove(day)
        vegan_meals.remove(random_item)

    return meal_schedule

def print_weekschedule(schedule):
    print("So this is how you meal schedule will look like:")
    print(schedule)
    for day, meal in schedule.items():
        print(f"On {day} you will eat: {meal}")


meal_schedule =  make_week_schedule()
print_weekschedule(meal_schedule)