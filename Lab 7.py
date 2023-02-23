# Ethan Newton Lab 7

sports_leagues = {"NFL": "National Football League (American football)", "MLB": "Major League Baseball (Baseball)",
                  "NBA": "National Basketball Association (Basketball", "EPL": "Premier League (Association football)",
                  "NHL": "National Hockey League (Ice hockey)", "MLS": "Major League Soccer (Association football)",
                  "IPL": "Indian Premier League (Twenty20 cricket",
                  "AFL": "Australian Football League (Australian rules football)",
                  "NRL": "National Rugby League (Rugby league football",
                  "CFL": "Canadian Football League (Canadian Football)"}


def delete_league():
    global sports_leagues
    inputted_league_abbreviation = str(input("enter the abbreviation of a league to be deleted"))
    if inputted_league_abbreviation.upper() in sports_leagues:
        removed_league_name = sports_leagues.pop(inputted_league_abbreviation.upper())
        print(removed_league_name, "has been removed")
    else:
        print("there is no league named", inputted_league_abbreviation)


def main():
    delete_league()


if __name__ == '__main__':
    main()
