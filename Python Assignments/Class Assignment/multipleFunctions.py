class SubfieldsInAI:
    def subfieldsInAI():
        courses = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fieldls in AI are:")
        for course in courses:
            print(course)


class OddEven:
    def oddEven():
        num = int(input("enter a number: "))
        if num % 2 == 1:
            message = "Odd Number"
        else:
            message ="Even Number"
        return f"{num} is {message}"

class ElegiblityForMarriage:
    def marraige_eligibility():
        gender = input("Your Gender:").strip().lower()
        age = int(input("Your Age:"))
    
        if gender == "male":
            if age >= 21:
                return "ELIGIBLE"
            else:
                return "NOT ELIGIBLE"
    
        if gender == "female":
            if age >= 18:
                return "ELIGIBLE"
            else:
                return "NOT ELIGIBLE"
    
        else:
            return "Invalid gender! Please enter male or female."


class FindPercent:
    def percentage():
        sub1 = int(input("Subject1="))
        sub2 = int(input("Subject2="))
        sub3 = int(input("Subject3="))
        sub4 = int(input("Subject4="))
        sub5 = int(input("Subject5="))
        
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print(f"Total :{total}")
        percentage = total / 5
        print( f"Percentage : {percentage}")


class Triangle:
    def triangle():
        h = int(input("Height:"))
        b = int(input("Breadth:"))
        area = (h*b) / 2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area)
        
        h1 = int(input("Height1:"))
        h2 = int(input("Height2:"))
        b1 = int(input("Breadth:"))
        perimeter = h1 + h2 + b1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter)













            