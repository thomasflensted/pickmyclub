import random, time

def main():

    with open("football-clubs.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        clubs = [line.strip() for line in lines]
    
    input("What's Your Favorite Animal? ")
    input("What's Your Favorite Holiday Destination? ")
    input("What's Your Favorite Color? ")
    print("Finding the perfect club for you", end = '')
    time.sleep(.5)
    print(".", end = '')
    time.sleep(.5)
    print(".", end = '')
    time.sleep(.5)
    print(".", end = '')
    time.sleep(.5)
    print(f"\nCongrats on your new club: {random.choice(clubs)}!\n")

main()