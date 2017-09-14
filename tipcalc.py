#this is basic tip calculator

newTip="yes"
while newTip== "yes":
 meal = input("Enter value in EUROS")
 tax = 6.75 / 100
 tip = 15.0 / 100

 meal = meal + meal * tax
 total = meal + meal * tip

 print("%.2f" % total)

 newTip= raw_input(" do you wanna calculate a new tip? Type yes or no")
 while newTip== "no":
    print "Goodbay"
    break