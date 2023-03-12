import random

def make_week_schedule(vegan_meals, meat_meals):

    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    meal_schedule = {}
    while weekdays:
        day = weekdays[0]

        if day in ['monday', 'wednesday', 'friday', 'sunday']:
            vegan_item = random.choice(vegan_meals)
            meal_schedule[day] = vegan_item
            weekdays.remove(day)
            vegan_meals.remove(vegan_item)

        else:
            meat_item = random.choice(meat_meals)
            meal_schedule[day] = meat_item
            weekdays.remove(day)
            meat_meals.remove(meat_item)

    return meal_schedule



def print_weekschedule(schedule):
    print("So this is how you meal schedule will look like:")
    for day, meal in schedule.items():
        print(f"On {day} you will eat: {meal}")


def amount_meals(vegan_meals, meat_meals):
    total_meals = len(vegan_meals) + len(meat_meals)
    print(f"I have {total_meals} meals")


current_vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
current_meat_meals = ['chicken madras', 'sparibs', 'salmon/veg', 'chickenburger']


amount_meals(current_vegan_meals, current_meat_meals)
lala = make_week_schedule(current_vegan_meals,current_meat_meals)
print_weekschedule(lala)
amount_meals(current_vegan_meals, current_meat_meals)

