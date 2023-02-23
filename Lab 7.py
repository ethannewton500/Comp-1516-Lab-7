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


def add_league():
    global sports_leagues
    print("please enter the three-letter abbreviation followed by the full string description of the new league")
    inputted_new_abbreviation = str(input("enter the abbreviation here")).upper()
    if inputted_new_abbreviation not in sports_leagues:
        inputted_new_league_desc = str(input("enter the full string description here")).title()
        sports_leagues[inputted_new_abbreviation] = inputted_new_league_desc
        print(inputted_new_league_desc, "has successfully been added")
    else:
        print(inputted_new_abbreviation, "is already in listed")


def get_abbreviations():
    return list(sports_leagues.keys())


def get_league_descriptions_tuple():
    return tuple(sports_leagues.values())


def get_league_descriptions_set():
    league_descriptions_set = {keys for keys in sports_leagues}
    league_descriptions_set.update(sports_leagues.values())
    return league_descriptions_set


def main():
    delete_league()
    add_league()
    print(get_abbreviations())
    print(get_league_descriptions_tuple())
    print(get_league_descriptions_set())


if __name__ == '__main__':
    main()
