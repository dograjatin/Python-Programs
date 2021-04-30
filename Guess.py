inc = False
dec = False
lgc = "" 
opr = 0 


print("Let Me Guess")


print("\nPlease Enter two numbers with some mathematical Logic")
a = input()
b = input()
num1 = int(a)
num2 = int(b)

if  num1 < num2: 
    inc = True
    #print("{} is greater: dec is {}: inc is {}".format(num1,dec,inc))
    
else: 
    dec = True
    #print("{} is greater: dec is {}: inc is {}".format(num1,dec,inc))

print("\nOkay! Please Enter another two numbers with same logic")
num3 = input()
num4 = input()

print("\nAlmost got it! Please Enter another two numbers with same logic")
num5 = input()
num6 = input()

if inc == True:
    if int(num4)/int(num3) == int(num6)/int(num5):
        lgc = "Multiplied"
        opr = int(num4)/int(num3)
    elif int(num4)-int(num3) == int(num6)-int(num5):
        lgc = "Added"
        opr = int(num4)-int(num3)
elif dec == True:
    if  int(num3)/int(num4) == int(num5)/int(num6):
        lgc = "Divided"
        opr = int(num4)/int(num3)
    elif int(num3)-int(num4) == int(num5)-int(num6):
        lgc = "Subtracted"
        opr = int(num4)-int(num3)

print("\nOkay! I GOT IT")
print("\n\n OH! you have {} the first number with {}".format(lgc,opr))
print("Claps If I got it :-)")
input("\nPress Enter to Exit")