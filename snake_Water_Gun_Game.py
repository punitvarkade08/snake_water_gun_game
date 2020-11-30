import random


def game(Devils, Gods):
    if Devils == Gods:
        return None
    elif Devils == "s":
        if Gods == "w":
            return False
        elif Gods == "g":
            return True

    elif Devils == "g":
        if Gods == "s":
            return False
        elif Gods == "w":
            return True

    elif Devils == "w":
        if Gods == "g":
            return False
        elif Gods == "s":
            return True


print("Devils Turn : snake(s) water(w) gun(g) ? :")
new = random.randint(1, 3)
# print(new)
if new == 1:
    Devils = "s"
elif new == 2:
    Devils = "w"
elif new == 3:
    Devils = "g"

Gods = input("Gods Turn : snake(s) water(w) gun(g) ? :")
gameWin = game(Devils, Gods)

print(f"Devils chose :-> {Devils}")
print(f"Gods chose :-> {Gods}")
if gameWin == None:
    print("the game is tie try again")
elif gameWin:
    print("you Win")
else:
    print("you Lose")
