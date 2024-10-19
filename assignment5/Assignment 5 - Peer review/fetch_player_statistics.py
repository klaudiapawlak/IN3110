from requesting_urls import get_html
from bs4 import BeautifulSoup
from IPython import embed
from filter_urls import find_articles
import matplotlib.pyplot as plt
import re


def extract_url(url):
    """Extract team url from the Conference semifinals
    for the 2021 NBA playoffs
    args:
        url (str) -- The url to the 2021 NBA playoffs
    returns:
        urls (list) -- A list containg the url to each team
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_all_next("table")[0]
    rows = bracket_table.find_all("tr")

    conf_semi = [4, 6, 16, 18, 28, 30, 40, 42]

    urls = []
    for c in conf_semi:
        row = rows[c]
        cells = row.find_all("td")
        urls.append(find_articles(str(cells))[0])

    return urls


def extract_player(url):
    """Extract the player url + name.
    args:
        urls (str) -- The url to the team from 2021 NBA playoffs
    returns:
        urls (list) -- A list containg the url to each player
        names (list) -- A list containg the names to each player
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    bracket_header = soup.find(id="Roster")
    bracket_table = bracket_header.find_all_next("table")[1]
    rows = bracket_table.find_all("tr")
    names = [row.findAll("td")[2].get_text(strip=True)
             for row in rows[1:]]

    urls = []
    for row in rows[1:]:
        cells = row.find_all("td")[2]
        urls.append(find_articles(str(cells))[0])

    return urls, names


def extract_player_statistics(url):
    """Extract player statistics for NBA player.
    args:
        url (str) -- URL to the Wikipedia article of a player.
    returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    try:
        bracket_header = soup.find(id="NBA")
        bracket_table = bracket_header.find_all_next("table")[0]
        rows = bracket_table.find_all("tr")
        name = soup.find('h1').get_text()
        for row in rows[1:]:
            season = row.findNext("td").get_text(strip=True).replace("†", "")
            if season[:4] == '2020' and season[-2:] == '21':
                cells = row.find_all("td")
                rpg = float(cells[8].get_text().replace("*", ""))
                bpg = float(cells[11].get_text().replace("*", ""))
                ppg = float(cells[12].get_text().replace("*", ""))
                break
            else:
                rpg, bpg, ppg = 0, 0, 0

    except AttributeError:
        rpg, bpg, ppg = 0, 0, 0

    return rpg, bpg, ppg


def team_stats(team_url):
    """Create a dictionary for each player for each team. Contains the player's
    name, rpg, bpg and ppg.
    args:
        url (str) -- URL to the Wikipedia article of a NBA team.
    returns:
        team (list) -- A list containing a dictionary for each player.
    """
    players, names = extract_player(team_url)
    team = []

    for i, player_url in enumerate(players):
        current_player = {"name": names[i]}
        rpg, bpg, ppg = extract_player_statistics(player_url)
        current_player["rpg"] = rpg
        current_player["bpg"] = bpg
        current_player["ppg"] = ppg
        team.append(current_player)
    return team


def plot_top3(teams):
    """Creates a plot for rpg, bpg and ppg. Saves the plots as a PNG file.
    args:
        teams (list) -- A list containg the url to each team
    """
    count_so_far = 0
    all_names = []

    for team in teams:
        rpg = []
        bpg = []
        ppg = []
        names = []
        players = team_stats(team)
        for player in players:
            names.append(player["name"])
            rpg.append(player["rpg"])
            bpg.append(player["bpg"])
            ppg.append(player["ppg"])
        zipped = zip(rpg, bpg, ppg, names)
        top3 = sorted(zipped, key=lambda x: x[2])

        top3_rpg = [rpg for (rpg, bpg, ppg, names) in top3[-3:]]
        top3_bpg = [bpg for (rpg, bpg, ppg, names) in top3[-3:]]
        top3_ppg = [ppg for (rpg, bpg, ppg, names) in top3[-3:]]
        names = [names for (rpg, bpg, ppg, names) in top3[-3:]]
        all_names.append(names)

        name = []
        for name_from_team in all_names:
            for one_name in name_from_team:
                name.append(one_name)

        x = range(count_so_far, count_so_far + 3)
        count_so_far += 3

        team_name = re.findall(r"_(.*)_season", team)

        rpg_plot = plt.figure(1)
        plt.xticks(range(len(name)), name, rotation=90)
        plt.title('Players over rebounds per game')
        plt.bar(x, top3_rpg, label=team_name[0].replace("_", " "))
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        bpg_plot = plt.figure(2)
        plt.xticks(range(len(name)), name, rotation=90)
        plt.title('Players over blocks per game')
        plt.bar(x, top3_bpg, label=team_name[0].replace("_", " "))
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        ppg_plot = plt.figure(3)
        plt.xticks(range(len(name)), name, rotation=90)
        plt.title('Players over points per game')
        plt.bar(x, top3_ppg, label=team_name[0].replace("_", " "))
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    rpg_plot.savefig("players_over_rpg.png", bbox_inches='tight')
    bpg_plot.savefig("players_over_bpg.png", bbox_inches='tight')
    ppg_plot.savefig("players_over_ppg.png", bbox_inches='tight')

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    teams = extract_url(url)
    plot_top3(teams)
