import sqlite3

def test_queries():
    conn = sqlite3.connect('sqlite_db_pythonsqlite.db')
    cursor = conn.cursor()
    
    print("Testing Q1: Facilities that charge fees to members")
    cursor.execute("SELECT name FROM Facilities WHERE membercost > 0;")
    results = cursor.fetchall()
    for row in results:
        print(f"  {row[0]}")
    
    print("\nTesting Q2: Count of facilities that don't charge fees")
    cursor.execute("SELECT COUNT(*) FROM Facilities WHERE membercost = 0;")
    count = cursor.fetchone()[0]
    print(f"  Count: {count}")
    
    print("\nTesting Q5: Facilities labeled as cheap/expensive")
    cursor.execute("""
        SELECT name, monthlymaintenance,
               CASE 
                   WHEN monthlymaintenance > 100 THEN 'expensive'
                   ELSE 'cheap'
               END AS cost_category
        FROM Facilities;
    """)
    results = cursor.fetchall()
    for row in results:
        print(f"  {row[0]}: ${row[1]} - {row[2]}")
    
    conn.close()

if __name__ == "__main__":
    test_queries()