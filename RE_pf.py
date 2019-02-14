def percentage_grade(percentage):
    if percentage >= 90 and percentage <= 100:
        return("You received an A")

    elif percentage >= 80 and percentage < 90:
        return("You received a B")

    elif percentage >= 70 and percentage < 80:
        return("You received a C")

    elif percentage >= 60 and percentage < 70:
        return("You received a D")

    else:
        return("Sorry, you received an F")

print ("Enter your grade.")
percentage = 0
percentage = int(input())
print(percentage_grade(percentage))
