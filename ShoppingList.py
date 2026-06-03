import Ingredient
import Recipe

class ShoppingList:
    def __init__(self, recipes):
        self._items = []
        for recipe in recipes:
            for ingredient in recipe.ingredients:
                self._items.append((ingredient, recipe.title))

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        newRecipe = recipe.scale(portions)
        if recipe.title in [i[1] for i in self._items]:
            for item in self._items:
                if item[1] == recipe.title:
                    item[0].quantity += newRecipe.ingredients[0].quantity
            return
        for ingredient in newRecipe.ingredients:
            self._items.append((ingredient, recipe.title))
    
    def remove_recipe(self, title: str):
        for i in self.items:
            if i[1] == title:
                self._items.remove(i)

    def get_list(self):
        shopping_list = {}
        for item in self.items:
            if (item[0].name, item[0].unit) in shopping_list:
                shopping_list[(item[0].name, item[0].unit)] += item[0].quantity
            else:
                shopping_list[(item[0].name, item[0].unit)] = item[0].quantity
        res=[]
        for (name, unit), quantity in shopping_list.items():
            res.append(Ingredient(name, quantity, unit))
        res.sort(key=lambda x: x.name)
        return res
    
    def __add__(self, other):
        if not isinstance(other, ShoppingList):
            raise ValueError("Объект должен быть экземпляром класса ShoppingList")
        new_list = ShoppingList([])
        for ingredient, title in self._items+other._items:
            new_list._items.append((Ingredient(ingredient.name, ingredient.quantity, ingredient.unit), title))
        return new_list