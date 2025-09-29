from classfridge1 import Inthefridge

ingredients_meals = {
    'pasta': ['pasta', 'tomatoesauce'],
    'burrito': ['wrap', 'guacomole', 'beans'],
    'chana masala': ['chickpeas', 'tomatoesauce', 'curry'],
    'shoarma': ['pita', 'vegan shoarma', 'garlic sauce'],
    'lentilsoup': ['lentils'],
    'tomatoe soup': ['tomatoesauce'],
    'risotto': ['rice', 'mushrooms', 'cream'],
    'chicken madres': ['chicken', 'curry'],
    'sparibs': ['ribs', 'sweetsauce'],
    'salmon/veg': ['salmon', 'veg'],
    'chickenburger': ['chickenpatty', 'bun']
    }

lala = Inthefridge(ingredients_meals)
baba = lala.product_in_fridge()
lala.which_meal(baba)

