class Inthefridge:

    def __init__(self, ingredients_meals):
        self.ingredients_meals = ingredients_meals


    def product_in_fridge(self):
        products = []
        print("Hey! What products do you have? enter 1 product at the time, type 'done' when you dont have any more products")
        while True:
            answer = input("Enter a value: " )
            if answer == 'done':
                break
            else:
                products.append(answer)

        return products
        print(products)


    def which_meal(self, products):
        meal_list = []
        for recipe, meals in self.ingredients_meals.items():
            for item in products:
                if item in meals:
                    meal_list.append(item)



            if all(item in meal_list for item in meals):
                print(f"we have a match! you can eat: {recipe}")
                meal_list = []






