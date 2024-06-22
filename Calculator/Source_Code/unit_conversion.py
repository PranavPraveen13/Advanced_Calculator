def convert_units(data):
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    value = float(data['value'])

    conversions = {
        'length': {
            'meters': 1,
            'centimeters': 100,
            'kilometers': 0.001,
            'inches': 39.3701,
            'feet': 3.28084
        },
        'mass': {
            'grams': 1,
            'kilograms': 0.001,
            'pounds': 0.00220462,
            'ounces': 0.035274
        },
        'time': {
            'seconds': 1,
            'minutes': 1 / 60,
            'hours': 1 / 3600,
            'days': 1 / 86400
        },
        'temperature': {
            'celsius': (lambda x: x, lambda x: x),
            'fahrenheit': (lambda x: (x - 32) * 5 / 9, lambda x: (x * 9 / 5) + 32),
            'kelvin': (lambda x: x - 273.15, lambda x: x + 273.15)
        }
    }

    category = None
    for cat, units in conversions.items():
        if from_unit in units and to_unit in units:
            category = cat
            break

    if category is None:
        return "Conversion not implemented"

    if category == 'temperature':
        to_celsius = conversions['temperature'][from_unit][0]
        from_celsius = conversions['temperature'][to_unit][1]
        result = from_celsius(to_celsius(value))
    else:
        base_value = value / conversions[category][from_unit]
        result = base_value * conversions[category][to_unit]

    return result
