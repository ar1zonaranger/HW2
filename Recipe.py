from Ingredient import Ingredient

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient : Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")
        newRecipe = Recipe(self.title, [])
        for ingredient in self.ingredients:
            newRecipe.add_ingredient(Ingredient(ingredient.name, ingredient.quantity*ratio, ingredient.unit))
        return newRecipe
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        return f"{self.title}:\n" + "\n".join(str(i) for i in self.ingredients)


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным")
        newRecipe = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, newRecipe.ingredients)
    
    def __str__(self):
        return f"[{self.diet_type}] {self.title}:\n" + "\n".join(str(i) for i in self.ingredients)