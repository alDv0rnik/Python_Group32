text = "1_2,40_5,5_32"
lst = [int(i) for i in text.replace("_",",").split(",")]
print(lst)
