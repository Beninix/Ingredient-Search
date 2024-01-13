import csv

ingredient_set = set()
blacklist = {"bake","boil","Ingredients", "fry", "england", "alcoholic", "kosher", "kosher for passover", "fat free", "whipped topping mix", "fajita seasoning to taste", "japan", "london", "mexico","low fat", "gummi", "calories", "brine", "side", "low sodium", "lunch", "roast", "taco", "sauce", "party", "breakfast", "chill", "lecithin", "macaroni and cheese", "marinate", "sandwich", "rating", "raw", "pie", "salad", "spring", "drinks", "dip", "frozen dessert","leftovers","topping thawed", "vegetarian", "pancake", "dough"}
#not sure; cookies?, cake?, cereal? biscuit? protein?
#items to group gumdrop, salt

#File reading
f = open('C:\\Users\\Brandon\\Downloads\\archive(4)\\clean_recipes.csv', 'r', encoding='utf8')
recipes = f.readlines()
#Read recipe data for ingredients
for line in recipes:
    contents = line.split(";")
    ingredients = contents[7].split(",")
    #print(ingredients)
    valid = True
    for ingredient in ingredients:
        if ingredient < 'almond' or ingredient in blacklist or not(ingredient.replace(" ","").isalpha()):
            valid = False
    if valid:
        for ingredient in ingredients:
            ingredient_set.add(ingredient)
        count+=1
#print(recipes[1].split(";")[7].split(","))
ingredient_set = sorted(ingredient_set)

#Initialize graph based on ingredient_set
ingredient_graph = [[0 for x in range(len(ingredient_set))] for y in range(len(ingredient_set))]
print(ingredient_set)
print(count)


