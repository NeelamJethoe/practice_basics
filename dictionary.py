import random

vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
meal_schedule = {}

while vegan_meals:
    random_item = random.choice(vegan_meals)
    day = weekdays[0]
    meal_schedule[day] = random_item
    weekdays.remove(day)
    vegan_meals.remove(random_item)

print(meal_schedule)
