
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def is_valid_input(value):
    try:
        float_value = float(value)
        return float_value > 0
    except ValueError:
        return False

def main():
    print("Welcome to the Enhanced BMI Calculator!")
    
    while True:
        weight_input = input("Please enter your weight in kilograms (or type 'exit' to quit): ")
        if weight_input.lower() == 'exit':
            print("Thank you for using the BMI Calculator. Goodbye!")
            break
        if not is_valid_input(weight_input):
            print("Invalid input. Please enter a positive number for weight.")
            continue
        
        weight = float(weight_input)

        height_input = input("Please enter your height in meters: ")
        if not is_valid_input(height_input):
            print("Invalid input. Please enter a positive number for height.")
            continue
        
        height = float(height_input)

        bmi = calculate_bmi(weight, height)
        
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()