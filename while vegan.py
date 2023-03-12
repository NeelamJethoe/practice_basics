import random

vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup']
done_meals = []
eating_meals = []

random_item = random.choice(vegan_meals)

print(vegan_meals)
done_meals.append(random_item)
vegan_meals.remove(random_item)
print(vegan_meals)
print(random_item)


while vegan_meals:
    random_item = random.choice(vegan_meals)
    print(f"you just ate {random_item}")
    done_meals.append(random_item)
    vegan_meals.remove(random_item)



