# create table
# load data


import psycopg2

conn = psycopg2.connect(user="sports_user", database="sports_db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS player_stats;")


create_table_string = """
    CREATE TABLE player_stats (
      player_name varchar(50),
      att numeric(4),
      yds numeric(4),
      avg real,
      long numeric(4),
      td numeric(4)
    )
"""
cur.execute(create_table_string)
conn.commit()

insert_template = "INSERT INTO player_stats VALUES (%s, %s, %s, %s, %s, %s)"

# database
'''roster = [["playername", 17, "fafood", 42],
          ["payertwo", 13, "favfooood", 23],
          ["playthree", 1, "favfood", 25]]'''

with open("rushing_db") as infile:
    data = infile.readlines()
database_list = [line.replace('\n', '').split(',') for line in data]
for player in database_list:
    cur.execute(insert_template, player)
    conn.commit()

cur.close()
conn.close()

