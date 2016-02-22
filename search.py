import psycopg2
conn = psycopg2.connect(user="sports_user", database="sports_db")
cur = conn.cursor()


def read_file():
   with open("rushing_db") as infile:
       data = infile.readlines()
   return [line.replace('\n', '').split('\t') for line in data]
new_name = True
new_att_new = True
new_yds_new = True
new_avg_new = True
new_long_new = True
new_td_new = True

lookup = True
cur.execute("select * from player_stats")
while lookup:
    option = input("Would you like to search or add? s/a ")
    if option == 'a':
        d = []
        while new_name:
            new_player_name = input("Enter new player name: ")
            if new_player_name.isalpha():
                d.append(new_player_name)
                new_name = False
            else:
                print("Not, valid entry ")
        while new_name == False:
            while new_att_new:
                new_att= input("Enter new att: ")
                if new_att.isnumeric():
                    d.append(new_att)
                    new_att_new = False
                else:
                    print("Not, valid entry ")
        while new_att_new == False:
            while new_yds_new:
                new_yds = input("Enter yds: ")
                if new_yds.isnumeric():
                    d.append(new_yds)
                    new_yds_new = False
                else:
                    print("Not valid entry")
        while new_yds_new == False:
            while new_avg_new:
                new_avg = input("Enter avg: ")
                if new_avg.isnumeric():
                    d.append(new_avg)
                    new_avg_new = False
                else:
                    print("Not valid entry")
        while new_avg_new == False:
            while new_long_new:
                new_long = input("Enter long: ")
                if new_long.isnumeric():
                    d.append(new_long)
                    new_long_new = False
                else:
                    print("Not vaild entry")
        while new_long_new == False:
            while new_td_new:
                new_td = input("Enter td:  ")
                if new_td.isnumeric():
                    d.append(new_td)
                    print("Awesome, you added a new player!")
                    new_td_new = False
                else:
                    print("Not a valid entry")
        insert_template = "INSERT INTO player_stats VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(insert_template, d)
        conn.commit()
    elif option == 's':
        search_input = input("You can search by:  player name(enter pn), att, yds, avg, long, and td. ")

        if search_input == 'pn':
            search_request = input("Who would you like to search for? ")
            cur.execute("select player_name from player_stats where player_name = (%s);", (search_request,))
            existing_player = cur.fetchall()
            if existing_player == []:
                print("player dosen't exist")
            else:
                cur.execute("select * from player_stats where player_name = (%s);", (search_request,))
                player_name_search = cur.fetchone()
                print("name" + "\t", "\t", "\t", "\t", player_name_search[0])
                print("att" + "\t", "\t", "\t", "\t", "\t", player_name_search[1])
                print("yds" + "\t", "\t", "\t", "\t", "\t", player_name_search[2])
                print("avg" + "\t", "\t", "\t", "\t", "\t", player_name_search[3])
                print("long" + "\t", "\t", "\t", "\t", player_name_search[4])
                print("td" + "\t", "\t", "\t", "\t", "\t", player_name_search[5])
        elif search_input == 'att':
            less_or_greater = input("enter > or < ")
            search_request = input("Enter the number for att search: ")
            if less_or_greater == '>':
                cur.execute("select player_name from player_stats where att > (%s);", (search_request,))
                att_search = cur.fetchall()
                print("Players who have greater than " + search_request + " att:")
                for player in att_search:
                    print(player[0])
            elif less_or_greater == '<':
                cur.execute("select player_name from player_stats where att < (%s);", (search_request,))
                att_search = cur.fetchall()
                print("Players who have less than " + search_request + " att:")
                for player in att_search:
                    print(player[0])
        elif search_input == 'yds':
            less_or_greater = input("enter > or < ")
            search_request = input("Enter the number for yds search: ")
            if less_or_greater == '>':
                cur.execute("select player_name from player_stats where yds > (%s);", (search_request,))
                yds_search = cur.fetchall()
                print("Players who have more than " + search_request + " yds:")
                for player in yds_search:
                    print(player[0])
            elif less_or_greater == '<':
                cur.execute("select player_name from player_stats where yds < (%s);", (search_request,))
                yds_search = cur.fetchall()
                print("Players who have less than " + search_request + " yds:")
                for player in yds_search:
                    print(player[0])
        elif search_input == 'avg':
            less_or_greater = input("enter > or < ")
            search_request = input("Enter the number for avg search: ")
            if less_or_greater == '>':
                cur.execute("select player_name from player_stats where avg > (%s);", (search_request,))
                avg_search = cur.fetchall()
                print("Players who have more than " + search_request + " avg:")
                for player in avg_search:
                    print(player[0])
            elif less_or_greater == '<':
                cur.execute("select player_name from player_stats where avg < (%s);", (search_request,))
                avg_search = cur.fetchall()
                print("Players who have less than " + search_request + " avg:")
                for player in avg_search:
                    print(player[0])
        elif search_input == 'long':
            less_or_greater = input("enter > or < ")
            search_request = input("Enter the number for long search: ")
            if less_or_greater == '>':
                cur.execute("select player_name from player_stats where long > (%s);", (search_request,))
                long_search = cur.fetchall()
                print("Players who have more than " + search_request + " long:")
                for player in long_search:
                    print(player[0])
            elif less_or_greater == '<':
                cur.execute("select player_name from player_stats where long < (%s);", (search_request,))
                long_search = cur.fetchall()
                print("Players who have less than " + search_request + " long:")
                for player in long_search:
                    print(player[0])
        elif search_input == 'td':
            less_or_greater = input("enter > or < ")
            search_request = input("Enter the number for td search: ")
            if less_or_greater == '>':
                cur.execute("select player_name from player_stats where td > (%s);", (search_request,))
                td_search = cur.fetchall()
                print("Players who have more than " + search_request + " td:")
                for player in td_search:
                    print(player[0])
            elif less_or_greater == '<':
                cur.execute("select player_name from player_stats where td < (%s);", (search_request,))
                td_search = cur.fetchall()
                print("Players who have less than " + search_request + " td:")
                for player in td_search:
                    print(player[0])

        end_search = input('Would you like to search again? y/n ')
        if end_search.lower() == "n":
            print("Search over!")
            lookup = False
        else:
            pass

cur.close()
conn.close()
