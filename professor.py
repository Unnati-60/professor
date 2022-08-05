import random


def main():
    n = get_level()
    score = start_game(n)
    print("Score : ",score)

# function to get level from player
def get_level():
    while True:
        try:
            n = int(input("Level : "))
            if n in [1,2,3] :
                break
        except :
            pass
    return(n)

# function to generate number of 'n'digits
def generate_integer(level):
    start = 0
    stop = 0
    if level == 1:
        stop = 9
        return random.randint(start,stop)
    else:
        start = 10**(level-1)
        stop = 10**level
        return random.randrange(start,stop)

# function to start game , asking player 10 math problems
def start_game(z):
    round = 0
    score = 0
    while round < 10:
        x = generate_integer(z)
        y = generate_integer(z)
        if start_round(x,y):
            score += 1
        round += 1
    return score

# fuction to check players answer
def start_round(x,y):
    tries = 0
    while tries < 3:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x+y):
                return True
            else:
                print("EEE")
                tries += 1
        except:
            print("EEE")
            tries += 1
    print(f"{x} + {y} = ",(x+y))
    return False


if __name__ == "__main__":
    main()
