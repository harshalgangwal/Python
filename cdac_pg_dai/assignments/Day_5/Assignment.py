def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def temperature_converter():
    try:
        temp_value = float(input("Enter the temperature value: "))
        temp_unit_from = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ").upper()
        temp_unit_to = input("Enter the unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

        if temp_unit_from == "C" and temp_unit_to == "F":
            result = celsius_to_fahrenheit(temp_value)
        elif temp_unit_from == "F" and temp_unit_to == "C":
            result = fahrenheit_to_celsius(temp_value)
        elif temp_unit_from == "C" and temp_unit_to == "K":
            result = celsius_to_kelvin(temp_value)
        else:
            raise ValueError("Invalid unit conversion specified.")

    except ValueError as ve:
        print(f"Error: {ve}")

    else:
        print(f"The converted temperature is: {result} {temp_unit_to}")

    finally:
        print("Temperature conversion process completed.")

temperature_converter()