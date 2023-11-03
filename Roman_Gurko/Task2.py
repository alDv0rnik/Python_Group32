# need python 3.10 or higher
match input("What the beast says? "):
    case "Woof":
        print("Dog goes woof!")
    case "Meow":
        print("Cat goes meow!")
    case "Tweet":
        print("Bird goes tweet!")
    case "Squeek":
        print("And mouse goes squeek!")
    case "Moo":
        print("Cow goes moo!")
    case "Croak":
        print("Frog goes croak!")
    case "Toot":
        print("And the elephant goes toot!")
    case "Quack":
        print("Ducks say quack!")
    case "Blub":
        print("And fish go blub!")
    case "Ow ow ow":
        print("And the seal goes ow ow ow!")
    case "Ring-ding-ding-ding-dingeringeding!":
        print("But there's one sound!")
    case "Wa-pa-pa-pa-pa-pa-pow!":
        print("That no one knows!")
    case "Hatee-hatee-hatee-ho!":
        print("What does the fox say?")
    case "Joff-tchoff-tchoffo-tchoffo-tchoff!":
        print("What does the fox say?")
    case "Bark":
        print("That's a dog!")
    case _:
        print("Undefined beast!")