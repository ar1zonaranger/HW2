class Ingredient:
    def __init__(self, name, quantity, unit):
        self._name = name
        self._quantity = quantity
        self._unit = unit

    @property
    def quantity(self):
        return self._quantity
    
    @property.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество должно быть положительным.")
        self._quantity = float(value)

    def __str__(self):
        return f"{self._name}: {self._quantity} {self._unit}"

    def __repr__(self):
        return f"Ingredient(\'{self._name}\', {self._quantity}, \'{self._unit}\')"
    
    def __eq__(self, other):
        return (isinstance(other, Ingredient) and
                self._name == other._name and self._unit == other._unit)
    
    