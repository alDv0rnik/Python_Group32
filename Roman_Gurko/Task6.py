telNum = input("Enter your cell number: ")
telNum = telNum.replace("8(0","+375").replace(")","").replace("-","")
print("Your number in international format is " + telNum)