snake = input("Enter snake string: ")
snake = snake.replace("_"," ").title().replace(" ","")
snake = snake[0].lower() + snake[1:]
print("Camel string: " + snake)