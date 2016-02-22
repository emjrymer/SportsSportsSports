'''
search for someone like this (name or position)
insert someone
close program
start database back up
migration is only run once
not running while main is running
remember people added in between runs
type in someone into input and return stats
'''


player_names = []
with open("rushing_db") as infile:
    data = infile.readlines()
database_list = [line.replace('\n', '').split('\t') for line in data]
for player in database_list:
    player_names.append(player[0])

lookup = True
unknown_entry = True

# user_search = input("Which play you want to search for?" )
# cur.execute("SELECT * FROM sports_db WHERE player_name = %s", (user_search,))
#http://espn.go.com/nfl/team/stats/_/name/sea/year/2013
while lookup:
    option = input("Would you like to search or add? s/a ")

    if option == 's':
        print("Too bad, feature not available yet.")
        # search_type = input("How would you like to search?" )
        # cur.execute("SELECT * FROM sports_db WHERE = %s", (search_type)
        pass
    elif option == 'a':
        while unknown_entry:
            add_new_user = input("Want to add new player? y/n ")
            if add_new_user.lower() == 'y':

                    new_player_name = input("Enter new player name: ")
                    if new_player_name not in player_names:
                        outfile.write("\n" + (new_player_name).lower())
                        outfile.write("\t" + input("Enter new att: ").lower())
                        outfile.write("\t" + input("Enter yds: ").lower())
                        outfile.write("\t" + input("Enter avg: ").lower())
                        outfile.write("\t" + input("Enter long ").lower())
                        print("Awesome, you added a new player!")
                        continue
                    else:
                        print("That's embarrassing, that player already exists.")
            else:
                unknown_entry = False


    else:
        end = input("not a valid entry, do you want to quit? y/n ")
        if end =='y':
            lookup = False
        else:
            pass