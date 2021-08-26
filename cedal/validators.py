from django.forms import ValidationError

class minValueValidator:

    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < 0:
            raise ValidationError("El valor ingresado debe ser mayor a 0")
        return value