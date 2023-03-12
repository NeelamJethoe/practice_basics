from importclasses2 import Meals


current_vegan_meals = ['buritto', 'chana masala', 'shoarma', 'lentilsoup', 'tomatoe soup', 'risotto', 'pasta']
current_meat_meals = ['chicken madras', 'sparibs', 'salmon/veg', 'chickenburger']

lala = Meals(current_vegan_meals, current_meat_meals)
baba = lala.make_week_schedule(lala.vegan_meals, lala.meat_meals)
lala.print_weekschedule(baba)
