import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='tournament',
                                         user='root',
                                         password='atli2369')

    sql_select_Query = "select * from team"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print(records)
    print("Total number of rows in team is: ", cursor.rowcount)

    # print("\nPrinting each laptop record")
    # for row in records:
    #     print("Id = ", row[0], )
    #     print("Name = ", row[1])
    #     print("Price  = ", row[2])
    #     print("Purchase date  = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
# finally:
#     if (connection.is_connected()):
#         connection.close()
#         cursor.close()
#         print("MySQL connection is closed")