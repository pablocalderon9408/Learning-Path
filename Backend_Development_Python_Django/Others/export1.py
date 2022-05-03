# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


if __name__ == '__main__':

    print("Voy a crear el objeto")
    human = Celsius(37)
    print("Objeto creado")

    print("Imprimir temperatura ----------------------")
    print(human.temperature)
    print("Finaliazo de Imprimir temperatura ----------------------")

    print("Inicio conversión")
    print(human.to_fahrenheit())
    print("Fin conversión")

    print("inicio consulta temp mala")
    human.temperature = -300
    print("fin consulta temp mala")