import random

import self as self


class Meals:
    """"showing me what to eat in a week"""

    def __init__(self, vegan_meals, meat_meals, items = None):
        self.vegan_meals = vegan_meals
        self.meat_meals = meat_meals
        self.items = items


    def make_week_schedule(self, vegan_meals, meat_meals):

        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        meal_schedule = {}
        while weekdays:
            day = weekdays[0]

            if day in ['monday','wednesday', 'friday', 'sunday']:
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


    def print_weekschedule(self, schedule):
        print("So this is how you meal schedule will look like:")
        print(schedule)
        for day, meal in schedule.items():
            print(f"On {day} you will eat: {meal}")



current_vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
current_meat_meals = ['chicken madras', 'sparibs', 'salmon/veg', 'chickenburger']

lala = Meals(current_vegan_meals, current_meat_meals)
baba = lala.make_week_schedule(lala.vegan_meals, lala.meat_meals)
lala.print_weekschedule(baba)
