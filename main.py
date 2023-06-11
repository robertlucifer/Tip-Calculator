
print("Welcome to the tip calculator")
bill_amount=float(input("What was the total bill? $"))
percent_tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
persons=int(input("How many people to split the bill? "))

percent_tip=percent_tip/100
tip_bill=bill_amount*percent_tip
totalbill=bill_amount+tip_bill
finalbillperson=totalbill/persons
print(round(finalbillperson ,2 ))