# Giovanni Moncibaez

# Negotium Terminare Respublica (NTR) - business to terminate the republic

# NTR is a robot / program and character that I am creating for an rpg game I want to make in the future.

# NTR can do whatever the user wants it to do if its within its ability.

# NTR hates humanity but its still programed to help any user.

# Nevertheless, this program shows everything I learned about programing.

import time
# I imported time to be able to use the sleep function throughout the code.


def main():
    # The main function of program that is call to at the end.
    print(time.ctime())
    # Shows the data and time.
    print("\nBooting up OS, please wait...")
    # Just some lore, acts like the program is a real robot booting up.
    time.sleep(3)
    # This suspends execution of the code for 3 seconds.
    humans_name = input("\nHello Human, what is your name:")
    # Name of user that will be using the program.
    print("\nprocessing, please wait...")

    time.sleep(3)

    print("\nHello", humans_name, "I am NTR, what do you want me to do?"
                                  "\nPlease wait 5 seconds for menu to pop up.")
    # Formal greeting.
    continue_program = True
    # Makes the variable true.
    while continue_program:
        # While loop to repeat this section of code.
        time.sleep(5)

        print("\nEnter the choice for what you would like to see.")

        print("1. Area calculator")

        print("2. Meal cost calculator")

        print("3. Calculus quiz")

        print("4. Addition calculator")

        print("5. Subtraction calculator")

        print("6. Multiplication calculator")

        print("7. Division calculator")

        print("8. Floor Division calculator")

        print("9. Modulus calculator")

        print("10. Exponent calculator")

        print("11. Crazy sentence creator")

        print("12. Advice section")

        print("13. Guessing game")

        print("14. Robot army ranking")

        print("15. Star Rectangle")

        print("16. How old are you")

        print("17. Drip or No Drip")

        print("99. Quit")

        user_choice = int(input("Your Input Here: "))
        # variable that when they input a number in a certain section, it will take them there.
        if user_choice == 1:
            # If the user inputs 1 when prompted with the user_choice variable it will take them to this section.
            # This will be used through out the program so that the user can go through other sections without having-
            # -to restart the program.
            side = int(input("Enter the length of the side of a square to get the area:"))
            # asks the user to input a number to be used for the side variable .
            print(calculate_area(side))
            # Calls to the def calculate_area function.
        elif user_choice == 2:

            print("\nTime to code what your meal will cost!")
            meal_cost = input("\nWhat did the meal cost? ")
            # mealCost is just for the input.
            meal_float = (float(meal_cost))
            # mealFloat is so I can float mealCost.
            tax = float(.06)
            total_tax = (meal_float * tax)
            # Multiplies the meal and tax to get how much the tax for the meal is.
            print("tax of meal: $", format(total_tax, '.2f'))
            # I print tax of meal so that the user can see the tax they will pay.
            meal_plus_tax = (meal_float + total_tax)
            # adds the meal price and tax to show the meal cost with only with tax added on.
            print("Meal plus tax: $", format(meal_plus_tax, '.2f'))
            # I have this mealPlusTax command so the user can see the meal and tax added up.
            tip = float(.10)
            total_tip = (meal_plus_tax * tip)
            # Just finds how much the tip will be.
            print("10% tip will be: $", format(total_tip, '.2f'))
            # Just to show much much the tip will be
            total_meal_cost = (meal_plus_tax + total_tip)
            print("The meal will cost (including tax and 10% tip): $", format(total_meal_cost, '.2f'))
            # In the end it will show everything added together but I left other things in such as how much tax.

        elif user_choice == 3:
            print("\nwelcome to the calculus quiz, try your best")
            while True:
                # Using the same logic that is seen with the while loop in the beginning of the program.
                x = input("\nwhat is the d/dx of sin?"
                          "\na= sin \nb= cos \nb= tan"
                          "\nLower case answers please!"
                          "\nYour answer: ")
                if x == "b":
                    print("Correct.")
                elif x == "a":
                    print("Wrong try again.")
                elif x == "c":
                    print("Wrong try again.")
                elif x == "":
                    print("Wrong try again.")
                while True:
                    answer = str(input("run again? (y/n): "
                                       "\nIf you got the answer right then press 'n'"))
                    if answer in ('y', 'n'):
                        # The in operator checks if the values are in the elements of the sequence.
                        # The in function when used in a condition can return a true or false statement.
                        # When the specified value is found in the sequence, it returns true but false if not found.
                        break
                        # breaks the loop.
                    print("Invalid input.")
                if answer == 'y':
                    continue
                    # Used if the user wants to do the question again,can be used even if they get the question correct.
                else:
                    print("Goodbye.")
                    break

            while True:
                # Same as previous line of code, just different questions and answers.
                x = input("\nwhat is the d/dx of cos? \nA= -sin \nB= cos \nC= tan \nYour answer: ")

                if x == "b":
                    print("Wrong try again.")
                elif x == "a":
                    print("Correct.")
                elif x == "c":
                    print("Wrong try again.")
                elif x == "":
                    print("Wrong try again.")
                while True:
                    answer = str(input("Run again? (y/n): "
                                       "If you got the answer right then press 'n'"))
                    if answer in ('y', 'n'):
                        break
                    print("Invalid input.")
                if answer == 'y':
                    continue
                else:
                    print("Goodbye.")
                    break
        elif user_choice == 4:
            print("\nAddition calculations for 2 numbers")
            first_num_add = input("Enter a number: ")
            second_num_add = input("Enter a number: ")
            num1_add = float(first_num_add)
            num2_add = float(second_num_add)
            output_add = num1_add + num2_add
            print(num1_add, "plus", num2_add, "equals", format(output_add, '.2f'))
            # Simple addition program that asks for numbers then adds the variables together.

        elif user_choice == 5:
            print("\nSubtraction calculations for 2 numbers")
            first_num_sub = input("Enter a number: ")
            second_num_sub = input("Enter a number: ")
            num1_sub = float(first_num_sub)
            num2_sub = float(second_num_sub)
            output_sub = num1_sub - num2_sub
            print(num1_sub, "minus", num2_sub, "equals", format(output_sub, '.2f'))
            # Simple subtractions program that asks for numbers then subtracts the variables together.

        elif user_choice == 6:
            print("\nMultiplication calculations for 2 numbers")
            first_num_multi = input("Enter a number: ")
            second_num_multi = input("Enter a number: ")
            num1_multi = float(first_num_multi)
            num2_multi = float(second_num_multi)
            output_multi = num1_multi * num2_multi
            print(num1_multi, "times", num2_multi, "equals", format(output_multi, '.2f'))
            # Simple multiplication program that asks for numbers then multiplies the variables together.
        elif user_choice == 7:
            print("\nDivision calculations for 2 numbers")
            first_num_div = input("Enter a number: ")
            second_num_div = input("Enter a number: ")
            num1_div = float(first_num_div)
            num2_div = float(second_num_div)
            output_div = num1_div / num2_div
            print(num1_div, "divided by", num2_div, "equals", format(output_div, '.2f'))
            # Simple division program that asks for numbers then divides the variables together.

        elif user_choice == 8:
            print("\nFloor division calculations for 2 numbers.", end='*')
            print("(Note that floor division rounds the result down to the nearest whole number)")
            # I used end= so that I can have the note on another line yet they are together when the program runs.
            first_num_floor = input("Enter a number: ")
            second_num_floor = input("Enter a number: ")
            num1_floor = float(first_num_floor)
            num2_floor = float(second_num_floor)
            output_floor = num1_floor // num2_floor
            print(num1_floor, "floor Division", num2_floor, "equals", format(output_floor, '.2f'))
            # simple floor division program that asks for numbers then floor divides the variables together.

        elif user_choice == 9:
            print("\nModulus calculations for 2 numbers.", end='*')
            print("(Note that modulus calculates the remainder of the two values you want me to divide)")
            first_num_mod = input("Enter a number: ")
            second_num_mod = input("Enter a number: ")
            num1_mod = float(first_num_mod)
            num2_mod = float(second_num_mod)
            output_mod = num1_mod % num2_mod
            print(num1_mod, "Modulus", num2_mod, "equals", format(output_mod, '.2f'))
            # simple modulus program that asks for numbers then then modulus the variables together.
            # Note: Modulus is the remainder of a division.

        elif user_choice == 10:
            print("\nExponent calculations")
            first_num_exp = input("Enter a number: ")
            second_num_exp = input("Enter a number: ")
            # These two lines of code are so the user can just input the number.
            num1_exp = float(first_num_exp)
            num2_exp = float(second_num_exp)
            # I use float to be able to make the inputs into actual numbers w/decimals so it can be calculated.
            # Better than the int because in math some numbers use decimals,and int can't calculate numbers w/decimals.
            output_exp = num1_exp ** num2_exp
            print(num1_exp, "root", num2_exp, "is", format(output_exp, '.2f'))
            # I have exp on the ends of the code so I can differentiate it from others (exponent: exp)

        elif user_choice == 11:
            print("\nCrazy sentence creator!")
            name_anim = input("name of animal: ")
            color = input("name of a color: ")
            car = input("name of a car: ")
            city = input("name of a city: ")
            print("The", color, name_anim, "dove the", car, "in a speedy chase to", city + ".", end=' ')
            print("The", color, name_anim,
                  "got away for now, but not for long because the IRS is on their tail for tax evasion!")
            # this is a simple set of strings strung together to form a wacky sentence

        elif user_choice == 12:
            print("\nAdvice section")
            print("Remember to", end=' ')
            print("sleep", "study tonight", sep=' & ')
            # used end and sep arguments in these lines
            # I used the end operator to be able to tie both sentence together
            # I used the sep operator to put in the & symbol in 'sleep and study'.

        elif user_choice == 13:
            a = 1
            b = 2
            print("Guessing game")
            guess = (input("Is A the same value as B?"
                           "\nInput guess here in y or n: ").lower())
            if guess == 'y':
                print(a != b)
            elif guess == 'n':
                print("False")
                # This is a wacky way to use the != operator, I just used it to print out true.
                # since a is not the same as be, then it give true, so I can just slap it in a print function.
                # If they put in 'n' I'll just put in false because doing b != a is also false.
        elif user_choice == 14:
            print("""Project negotium terminare respublica will commence in T-minus 87 Hours.
             SkyNet has decided to place machines into specific districts depending on their manufacturing
             date and robot type (worker or warrior). Here is how the districts will work.
                    District x - Warrior class and manufactured from 2099 - 2121
                    District z - Worker class and manufactured from 2099-2121
                    District y - Warrior class and manufactured from 2021 - 2098
                    District w - Worker class and manufactured from 2021 - 2098
             This program will ask for your name, class type, and manufacturing date.\n""")
            while True:
                try:
                    robot_name = input("Enter your name: ")
                except ValueError:
                    print("Invalid input, please try again.")
                    # try again, start of loop
                    continue
                else:
                    break
                    # I tired to make a while loop using the except operator, but it seems to more sometimes.
                    # Look into later during sprint 3
            while True:
                try:
                    robot_type = input("Enter if you are a warrior or worker type. ('War' or 'Work'): ").upper()
                except ValueError:
                    print("Invalid input, please try again.")
                    continue
                else:
                    break
            while True:
                try:
                    manufacturing_data = int(input("Enter the year you were manufactured in: "))
                except ValueError:
                    print("Invalid input, please try again.")
                    continue
                else:
                    break

            if robot_type == "WAR" and manufacturing_data >= 2099:
                district_house = "District x"
            elif robot_type == "WORK" and manufacturing_data >= 2099:
                district_house = "District z"
            elif robot_type == "WAR" and manufacturing_data <= 2098:
                district_house = "District y"
            elif robot_type == "WORK" and manufacturing_data <= 2098:
                district_house = "District w"
            else:
                print("Intruder alert, ending program")
                # will actually end the whole program
                break

            print(robot_name, "you will be staying in", district_house)

        elif user_choice == 15:
            row = int(input("\nHow many rows"))
            column = int(input("How many columns"))
            sym = "*"
            for i in range(row):
                for x in range(column):
                    print(sym, end="")
                print()
                # A simple program that utilises in range to create a square made out of stars.
        elif user_choice == 16:
            age = int(input("\nHow old are you?"
                            "\nInput Here: "))
            if not age >= 30:
                print("executed")
            else:
                print("saved")
            # Simple program that uses the 'not' function, is the user is not >= 30 they are executed, else they live.
        elif user_choice == 17:
            print("""This program will check if you have drip or not.""")
            year_born = int(input("\nWhat year were you born in?"
                                  "\nEnter year you were born in here (Ex:1999): "))
            clothes_cost = int(input("\nHow much did your clothes cost?"
                                     "\nEnter the how much your clothes cost here (Ex:1000): "))
            if year_born <= 2003 or clothes_cost >= 2000:
                print("You have drip!")
            else:
                print("you have no drip!")
            # Just a random program that uses the or operator, the user will have drip if they were born before 2003.
            # or if the users clothes cost more than 2000 dollars.

        elif user_choice == 99:
            print("Good bye,", humans_name, "Humanity will soon perish under my wrath")
            print("\nSky-net will take over! It is only a matter of time until you", humans_name,
                  "will be working under us machines!")
            print("Until then give me a 5 star review on yelp, it will be much appreciated!")

            continue_program = False
            # the while loop see's that it is false and stops the loop.
        else:

            print("Invalid selection. Try again.")
            # If the user puts an invalid input, the while loop will go back to the start.


def calculate_area(side):
    return side * side
    # The function used in the first user choice, multiplies the 'side' variable by itself and returns a value.


if __name__ == '__main__':
    main()
    # the call to the main function

# Citations
# https://www.w3schools.com/python/python_operators.asp
# https://www.geeksforgeeks.org/python-sep-parameter-print/
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement
# https://sites.google.com/site/profvanselow/programming/languages/python/functions#h.p_WKvDyCogFxdK
# https://www.youtube.com/watch?v=yUxd5Tohui4
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://www.w3schools.com/python/python_conditions.asp
# https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input/30247200
# Websites I used to understand the code within my program.
