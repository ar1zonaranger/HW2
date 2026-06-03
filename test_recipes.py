from Ingredient import Ingredient
from Recipe import Recipe, DietaryRecipe
from ShoppingList import ShoppingList

#1: Тестирование класса Ingredient

def test_ingredient_init():
    i=Ingredient("Мука", 500, "г")
    assert i.name == "Мука"
    assert i.quantity == 500
    assert i.unit == "г"

def test_ingredient_str():
    i=Ingredient("Мука", 500, "г")
    assert str(i) == "Мука: 500.0 г"

def test_ingredient_eq_different_quantities():
    i1=Ingredient("Мука", 500, "г")
    i2=Ingredient("Мука", 1000, "г")
    assert i1 == i2

def test_ingredient_eq_different_names():
    i1=Ingredient("Мука", 500, "г")
    i2=Ingredient("Сахар", 500, "г")
    assert i1 != i2

def test_ingredient_eq_different_units():
    i1=Ingredient("Мука", 500, "г")
    i2=Ingredient("Мука", 500, "кг")
    assert i1 != i2

#2: Тестирование класса Recipe

def test_recipe_init():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    assert r.title == "Омлет"
    assert r.ingredients == [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")]