class TempConversion:
    def __init__(self, temp):
        self.__temp = temp

    def __fahrenheit_to_celsius(self):
        return (self.__temp - 32) * 5/9

    def __kelvin_to_celsius(self):
        return self.__temp - 273.15

    def __celsius_to_fahrenheit(self):
        return (self.__temp * 9/5) + 32

    def __kelvin_to_fahrenheit(self):
        return (self.__temp - 273.15) * 9/5 + 32

    def __celsius_to_kelvin(self):
        return self.__temp + 273.15

    def __fahrenheit_to_kelvin(self):
        return (self.__temp - 32) * 5/9 + 273.15

    def get_conversions(self):
        print('Fahrenheit to Celsius:', self.__fahrenheit_to_celsius(), '°C')
        print('Kelvin to Celsius:', self.__kelvin_to_celsius(), '°C')
        print('Celsius to Fahrenheit:', self.__celsius_to_fahrenheit(), '°F')
        print('Kelvin to Fahrenheit:', self.__kelvin_to_fahrenheit(), '°F')
        print('Celsius to Kelvin:', self.__celsius_to_kelvin(), 'K')
        print('Fahrenheit to Kelvin:', self.__fahrenheit_to_kelvin(), 'K')

temp = float(input('Enter temperature value: '))
temp_conv = TempConversion(temp)
temp_conv.get_conversions()