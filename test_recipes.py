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

def test_recipe_add_new_ingredient():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    r.add_ingredient(Ingredient("Сыр", 50, "г"))
    assert Ingredient("Сыр", 50, "г") in r.ingredients

def test_recipe_add_existing_ingredient():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    r.add_ingredient(Ingredient("Яйца", 1, "шт"))
    assert Ingredient("Яйца", 4, "шт") in r.ingredients

def test_recipe_scale_new_object():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    r2=r.scale(2)
    assert r2 is not r
    assert r2==Recipe("Омлет", [Ingredient("Масло", 40, "г"), Ingredient("Яйца", 6, "шт"), Ingredient("Молоко", 200, "мл")])

def test_recipe_scale_multiplication():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    r2=r.scale(2)
    quantities = [i.quantity for i in r.ingredients]
    scaledQuantities = [i.quantity for i in r2.ingredients]
    for i in range(len(quantities)):
        assert scaledQuantities[i] == quantities[i]*2

def test_scale_invalid_ratio():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    try:
        r.scale(0)
        assert False
    except ValueError:
        assert True
    try:
        r.scale(-1)
        assert False
    except ValueError:
        assert True

def test_recipe_len():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    assert len(r) == 3

