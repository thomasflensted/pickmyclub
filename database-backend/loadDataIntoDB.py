from leaguesAndClubs import leagueDict
import sqlite3

def main():
    
    conn = sqlite3.connect("clubs.db")

    try:
        conn.execute('''CREATE TABLE CLUBS
            (NAME          TEXT    NOT NULL,
            LEAGUE         TEXT     NOT NULL,
            HASFANS        INT);''')
        print("opened db successfully")
    except sqlite3.OperationalError:
        conn.execute("DROP TABLE CLUBS")
        conn.execute('''CREATE TABLE CLUBS
            (NAME          TEXT    NOT NULL,
            LEAGUE         TEXT     NOT NULL,
            HASFANS        INT);''')

    for league in leagueDict:
        
        currentLeague = leagueDict[league]
        for club in currentLeague:
            conn.execute( "insert into clubs (name, league, hasfans) values (?, ?, ?)", (club, league, 0))

    cursor = conn.execute("SELECT name,league FROM CLUBS WHERE league = 'Premier League'")
    for row in cursor:
        print(f"Club: {row[0]}, league: {row[1]}")

if __name__ == "__main__":
    main()