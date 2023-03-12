import random

import self as self


class Meals:
    """"showing me what to eat in a week"""

    def __init__(self, vegan_meals, meat_meals, items = None):
        self.vegan_meals = vegan_meals
        self.meat_meals = meat_meals
        self.items = items


    def make_week_schedule(self):

        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        meal_schedule = {}
        while weekdays:
            day = weekdays[0]

            if day in ['monday','wednesday', 'friday', 'sunday']:
                vegan_item = random.choice(self.vegan_meals)
                meal_schedule[day] = vegan_item
                weekdays.remove(day)
                self.vegan_meals.remove(vegan_item)

            else:
                meat_item = random.choice(self.meat_meals)
                meal_schedule[day] = meat_item
                weekdays.remove(day)
                self.meat_meals.remove(meat_item)

        return meal_schedule


    def print_weekschedule(self, schedule):
        print("So this is how you meal schedule will look like:")
        print(schedule)
        for day, meal in schedule.items():
            print(f"On {day} you will eat: {meal}")


class Fridge(Meals):

    def __init__(self, vegan_meals, meat_meals):
        super().__init__(vegan_meals, meat_meals)

    def amount_meals(self, vegan_meals, meat_meals):
        total_meals = len(vegan_meals) + len(meat_meals)
        print(f"I have {total_meals} meals")


current_vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
current_meat_meals = ['chicken madras', 'sparibs', 'salmon/veg', 'chickenburger']


lala = Fridge(current_vegan_meals, current_meat_meals)
lala.amount_meals(current_vegan_meals, current_meat_meals)
baba = lala.make_week_schedule()
lala.print_weekschedule(baba)
lala.amount_meals()
