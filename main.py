import os
from json import load as json_load


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def select_faction(
    options: list[str], map_selection: str, blufor_selection=None, is_redo=False
):
    clear()
    if is_redo:
        print("Something went wrong, make a new selection")
    print(f"Selected Map: {map_selection}")
    if blufor_selection is not None:
        print(f"Selected BluFor Faction: {blufor_selection}")

    print("")
    for i, option in enumerate(options):
        print(f"{i+1}: {option}")

    print("")

    if blufor_selection is None:
        faction_type = "BluFor"
    else:
        faction_type = "OpFor"

    try:
        selection = options[int(input(f"Select {faction_type} faction: ").strip()) - 1]
    except:
        return select_faction(options, map_selection, blufor_selection, True)

    return selection


def main():
    clear()
    try:
        with open("settings.json", "r") as settings:
            json_file = json_load(settings)
    except:
        print("Something went wrong while loading settings file")
        return

    maps = json_file.get("MAPS")

    if maps is None or len(maps) == 0:
        print("No maps were found in settings file")

    factions = json_file.get("FACTIONS")

    if factions is None or len(factions) == 0:
        print("No factions were found in settings file")

    try:
        print("")
        for i, option in enumerate(maps):
            print(f"{i+1}: {option}")
        print("")
        map_selection = maps[int(input("Select a map: ").strip()) - 1]

        try:
            blufor_selection = select_faction(factions, map_selection)
            opfor_selection = select_faction(factions, map_selection, blufor_selection)

            clear()

            print()
            print(
                f"Admin servertravel {map_selection}?BluForFaction={blufor_selection}?OpForFaction={opfor_selection}"
            )
            print()

        except Exception as e:
            print("Something went wrong in faction selection")

    except Exception as e:
        print("Something went wrong in map selection")
        return main()


if __name__ == "__main__":
    main()
