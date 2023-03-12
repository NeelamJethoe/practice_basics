import random

vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup']
done_meals = []
eating_meals = []

print("would you like us to chose a diner for you? say yes/no")
answer_user = input()

if answer_user == 'no':
    print("oke!")

elif answer_user == 'yes':
    random_item = random.choice(vegan_meals)
    print(f"you will eat tonight: {random_item}")
    vegan_meals.remove(random_item)
    print(f"you have the following meals left: {vegan_meals}")


