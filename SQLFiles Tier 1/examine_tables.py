import sqlite3

def examine_database():
    conn = sqlite3.connect('sqlite_db_pythonsqlite.db')
    cursor = conn.cursor()
    
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  {table[0]}")
    
    # Get schema for each table
    for table in tables:
        table_name = table[0]
        print(f"\n=== {table_name} ===")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
    
    # Sample data from each table
    for table in tables:
        table_name = table[0]
        print(f"\n=== Sample data from {table_name} ===")
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
        rows = cursor.fetchall()
        for row in rows:
            print(f"  {row}")
    
    conn.close()

if __name__ == "__main__":
    examine_database()