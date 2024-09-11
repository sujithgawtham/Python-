class multipleFunctions():
    def subFields():
        list = ["Machine Learnng", "Neural Network",
           "Vision", "Robotics",
           "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are :")
        for topics in list:
            print(topics)

    def OddEven():
        number = int(input("Enter a number:"))
        print("Enter a number :",number)
        if(number % 2) == 0:
            print("Even Number")
            result = "It is an Even Number"
        else:
            print("Odd Number")
            result = "it is Odd Number"
        return result
    
    def checkEligible():
        gender = input("Enter your Gender")
        print("Enter your Gender :",gender)
        age = int(input("Enter your age "))
        print("Enter your age",age)
        if(gender == "Male" and age <= 20):
            print("Not Eligible")
            eligible = "Not Eligible"
        else:
            print("Eligible")
            eligible = "Eligible"

    def marksTotal():
        sub1 = int(input("Subject1"))
        print("Subject1 =",sub1)
        sub2 = int(input("Subject2"))
        print("Subject1 =",sub2)
        sub3 = int(input("Subject3"))
        print("Subject1 =",sub3)
        sub4 = int(input("Subject4"))
        print("Subject1 =",sub4)
        sub5 = int(input("Subject5"))
        print("Subject1 =",sub5)
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print("total : ",total)
        resultTotal = total
        percentage = (total / 500.0) * 100
        print("Percentage :",percentage)
        resultPercent = percentage
        return resultTotal,resultPercent
    
    def triangle(Height,Breadth,Height1,Height2,Breadth1):
            area = (Height * Breadth) / 2
            print("Height :",Height)
            print("Breadth :",Breadth)
            print( "Area of Triangle :",area)
            perimeter = (Height1 + Height2 + Breadth1)
            print("Height1 :",Height1)
            print("Height2 :",Height2)
            print("Breadth :",Breadth1)
            print("Perimeter formula :",perimeter)
            return area,perimeter
    
