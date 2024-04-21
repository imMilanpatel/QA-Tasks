# This file is a Class template file for calculating BMI of a person


# Class definition
class BMICalculator:

    # BMI Logic
    def calculate_bmi(self, weight_kg, height_m):
        if weight_kg <= 0 or height_m <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight_kg / (height_m ** 2)
        return bmi
    
    # BMI related message post calculation to be indicated to the user
    def get_bmi_category(self, bmi):
        if bmi < 16.0:
            return "Underweight (Severe thinness)"
        elif 16.0 <= bmi < 17.0:
            return "Underweight (Moderate thinness)"
        elif 17.0 <= bmi < 18.5:
            return "Underweight (Mild thinness)"
        elif 18.5 <= bmi < 25.0:
            return "Normal range"
        elif 25.0 <= bmi < 30.0:
            return "Overweight (Pre-obese)"
        elif 30.0 <= bmi < 35.0:
            return "Obese (Class I)"
        elif 35.0 <= bmi < 40.0:
            return "Obese (Class II)"
        else:
            return "Obese (Class III)"
        
if __name__ == "__main__":
    BMICalculator