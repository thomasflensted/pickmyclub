import requests
from bs4 import BeautifulSoup


def getLeaguesWithClubs():

    leagues = [
        "la-liga",
        "bundesliga",
        "serie-a",
        "eredivisie",
        "ligue-1",
        "premier-league"
    ]

    leagueDict = {}
    for league in leagues:
        html = getHTML(league)
        clubs = getClubs(html)
        leagueName = getLeagueName(league)
        leagueDict[leagueName] = clubs

    return leagueDict


def getLeagueName(name):

    return " ".join(name.split("-")).title()


def getClubs(html):

    soup = BeautifulSoup(html, "html.parser")
    rawClubs = soup.find_all("a", {"class": "standing-table__cell--name-link"})
    return [club.getText() for club in rawClubs]


def getHTML(league):

    url = f"https://www.skysports.com/{league}-table"
    raw_page = requests.get(url)
    return raw_page.text
