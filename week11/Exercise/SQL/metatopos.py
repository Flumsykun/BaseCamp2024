import sqlite3


# read json file
# def read_file_as_data_with_json_load() -> list:
#     content = []
#     with open('metatopos-places.json') as jsonfile:
#         content = json.load(jsonfile)
#     return content


# def dict_factory(cursor, row):
#     names = [column[0] for column in cursor.description]
#     return dict(zip(names, row))


# def create_postcodes_table(conn: sqlite3.Connection) -> None:
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS postcodes (
#             postcode TEXT PRIMARY KEY,
#             latitude REAL,
#             longitude REAL
#         )
#     ''')

def main() -> None:
    # Connect to the database
    conn = sqlite3.connect('postcodes.db')
    cur = conn.cursor()

    # Create the table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS postcodes (
            postcode TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL
        )
    ''')

    # Insert a new postcode into the table
    new_postcode = {'postcode': 'GLHZ', 'latitude': 2222, 'longitude': 2222}
    cur.execute('SELECT * FROM postcodes WHERE postcode = ?', (new_postcode['postcode'],))
    if cur.fetchone() is None:
        cur.execute('''
            INSERT INTO postcodes (postcode, latitude, longitude)
            VALUES (?, ?, ?)
        ''', (new_postcode['postcode'], new_postcode['latitude'], new_postcode['longitude']))
        print(f"Inserted postcode {new_postcode['postcode']}")
    else:
        print(f"Postcode {new_postcode['postcode']} already exists")

    # Print out all the postcodes in the table
    cur.execute('SELECT * FROM postcodes')
    for row in cur.fetchall():
        print(row)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

# ([{=============================================================================================}])

# list with sorted postodes sql query
# query = """SELECT pcstart, pcend
# FROM place
# ORDER BY pcstart ASC"""

# list select from where
# query = """SELECT pcstart, pcend
# FROM place
# WHERE pcstart < 1000"""

# ([{=============================================================================================}])

# list from places where the postcode is startswith 1, 2,  and 3
# query =  """SELECT pcstart, pcend
# FROM place
# WHERE pcstart LIKE '1%' OR pcstart LIKE '2%' OR pcstart LIKE '3%'"""

# list from places where the postcode starts with the letter R
# query = """SELECT pcstart, pcend
# FROM place
# WHERE pcstart LIKE 'R%'"""

# list from places that contain more than 10 postcodes
# query = """SELECT pcstart, pcend
# FROM place
# GROUP BY pcstart
# HAVING COUNT(pcstart) > 10"""

# ([{=============================================================================================}])

# SELECT * FROM place
# WHERE pcstart < 4000

# SELECT * FROM place
# WHERE name >= "R" AND name < "S"

# SELECT * FROM place
# WHERE (pcstart >= 2000 AND pcstart <= 2999)
#    OR (pcstart >= 4000 AND pcstart <= 4999)

# SELECT * FROM place
# WHERE pcend - pcstart > 10

# query = """UPDATE place
# SET pcend = ?
# WHERE name = ?"""

# query = """DELETE
# FROM place
# WHERE pcend >=?"""

# Add a new city with the code 99999 that has postcodes between 3990 and 3999 so (code, name, pcstart, pcend)
# query = """INSERT
# INTO place (code, name, pcstart, pcend)
# VALUES(?, ?, ?, ?)"""

# ([{=============================================================================================}])

# print(read_file_as_data_with_json_load())

#
# # create tables for the database
# def create_postcodes_table(conn: sqlite3.Connection) -> None:
#     cur = conn.cursor()
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS postcodes (
#             postcode TEXT PRIMARY KEY,
#             latitude REAL,
#             longitude REAL
#         )
#     ''')
#
#
# # insert postcodes into the table
# def insert_postcodes_into_table(conn: sqlite3.Connection, postcodes: list) -> None:
#     database_cursor = conn.cursor()  # connect to the database
#     for postcode in postcodes:  # loop through the postcodes
#         if isinstance(postcode, dict):  # check if the postcode is a dictionary
#             database_cursor.execute('''
#                 INSERT INTO postcodes (postcode, latitude, longitude)
#                 VALUES (?, ?, ?)
#             ''', (postcode.get('postcode'), postcode.get('latitude'), postcode.get('longitude')))
#         else:
#             print(f"Skipping invalid postcode: {postcode}")
#
#
# # read the json file and return the data
# def read_json_file(filename: str) -> list:
#     with open(filename, 'r') as f:
#         return json.load(f)
#
#
# def main() -> None:
#     # Connect to the database
#     conn = sqlite3.connect('metatopos.db')
#     cur = conn.cursor()
#
#     # Read the JSON file
#     postcodes = read_json_file('metatopos-places.json')
#
#     # Create the table
#     create_postcodes_table(conn)
#
#     # Insert the data into the table
#     insert_postcodes_into_table(conn, postcodes)
#
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()
#
#
# if __name__ == "__main__":
#     main()
