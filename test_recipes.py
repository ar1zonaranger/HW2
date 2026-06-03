import pytest
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
    assert r2.title == r.title
    assert r2.ingredients == [Ingredient("Масло", 40, "г"), Ingredient("Яйца", 6, "шт"), Ingredient("Молоко", 200, "мл")]

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

#3: Тестирование класса ShoppingList

def test_shopping_list_add_recipe():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт")])
    sl=ShoppingList()
    sl.add_recipe(r, 2)
    assert sl.get_list() == [Ingredient("Масло", 40.0, "г"), Ingredient("Яйца", 6.0, "шт")]

def test_shopping_list_add_recipe_invalid_portions():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт")])
    sl=ShoppingList()
    try:
        sl.add_recipe(r, 0)
        assert False
    except ValueError:
        assert True
    try:
        sl.add_recipe(r, -1)
        assert False
    except ValueError:
        assert True

def test_shopping_list_remove_existing_recipe():
    r1=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт")])
    r2=Recipe("Яичница", [Ingredient("Масло", 10, "г"), Ingredient("Яйца", 2, "шт")])
    sl=ShoppingList()
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    sl.remove_recipe("Омлет")
    assert sl.get_list() == [Ingredient("Масло", 10.0, "г"), Ingredient("Яйца", 2.0, "шт")]

def test_shopping_list_remove_nonexistent_recipe():
    r=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт")])
    sl=ShoppingList()
    sl.add_recipe(r, 1)
    old_list=sl.get_list()
    sl.remove_recipe("Яичница")
    assert sl.get_list() == old_list

def test_shopping_list_get_list_sums_quantities():
    r1=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт")])
    r2=Recipe("Яичница", [Ingredient("Масло", 10, "г"), Ingredient("Яйца", 2, "шт")])
    sl=ShoppingList()
    sl.add_recipe(r1, 1)
    sl.add_recipe(r2, 1)
    assert sl.get_list() == [Ingredient("Масло", 30.0, "г"), Ingredient("Яйца", 5.0, "шт")]

def test_shopping_list_add_merge():
    r1=Recipe("Омлет", [Ingredient("Масло", 20, "г"), Ingredient("Яйца", 3, "шт"), Ingredient("Молоко", 100, "мл")])
    r2=Recipe("Яичница", [Ingredient("Масло", 10, "г"), Ingredient("Яйца", 2, "шт")])
    sl1=ShoppingList()
    sl2=ShoppingList()
    sl1.add_recipe(r1, 1)
    sl2.add_recipe(r2, 1)
    combined = sl1 + sl2
    assert combined.get_list() == [Ingredient("Масло", 30.0, "г"), Ingredient("Молоко", 100.0, "мл"), Ingredient("Яйца", 5.0, "шт")]
    assert sl1.get_list() == [Ingredient("Масло", 20.0, "г"), Ingredient("Молоко", 100.0, "мл"), Ingredient("Яйца", 3.0, "шт")]
    assert sl2.get_list() == [Ingredient("Масло", 10.0, "г"), Ingredient("Яйца", 2.0, "шт")]
