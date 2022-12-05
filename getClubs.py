def main():

    clubs = getClubs("leagues/seriea.txt")
    print(clubs)

def getClubs(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        clubs = [line.strip() for line in f]
        return clubs


main()