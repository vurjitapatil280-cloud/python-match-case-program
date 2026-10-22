# 1 DAY OF THE WEEK

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# 2. SIMPLE CALCULATOR

a = 10
b = 5
op = "+"

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")



# 3. TRAFFIC SIGNAL

signal = "red"

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")




# 4  NUMBER CHECK

num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")




# 5 VOWEL CHECK

ch = "a"

match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")



# 6 MONTH NAME

month = 3

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _:
        print("Other month")




# 7 POSITIVE, NEGATIVE OR ZERO

num = 0

match num:
    case 0:
        print("Zero")
    case _ if num > 0:
        print("Positive")
    case _:
        print("Negative")



# 8. GRADE CALCULATOR

grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case _:
        print("Invalid grade")




# 9. MENU SELECTION

choice = 2

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Sandwich")
    case _:
        print("Invalid choice")




# 10. EVEN OR ODD

num = 4

match num % 2:
    case 0:
        print("Even number")
    case 1:
        print("Odd number")