def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input(
        "Are your mearsurements in metric (m) or imperial (i) systems ?"
    ).lower().strip()
    return (height, weight, system)


def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi


while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = round(calculate_bmi(weight, system='imperial', height=height), 4)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = round(calculate_bmi(weight, height), 4)
        print(f"Your BMI is {bmi}")
        break
    else:
        print(
            "Error: Unknown measurement system. Please use imperial or metric."
        )
