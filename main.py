# score = 0
# height = 1.75
# isWinning = True
#
# #f-String (Deixa tudo como string, nao precisa colocar em cada um)
#
# print(f"Your score is {score}")
# print(f"Your height is {height}")
# print(f"You are Winning is {isWinning}")
#
#
# age = input("Quantos anos voce tem? ")
#
# age_as_int = int(age)
#
# anos_restantes = 90 - age_as_int
# dias_restantes = anos_restantes * 365
# semanas_restantes = anos_restantes * 52
# meses_restantes = anos_restantes * 12
#
# mensagem = f"Voce tem {dias_restantes} dias restantes, {semanas_restantes} semanas, {meses_restantes} meses"
#
# print(mensagem)

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip_percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
bill_with_tip = tip_percentage / 100 * bill + bill

print(f"Each person should pay ${final_amount}")










