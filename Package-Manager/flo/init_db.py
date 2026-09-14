import sqlite3  

conn = sqlite3.connect("mypkg.db")  
cursor = conn.cursor()  

# Create tables  
cursor.execute("""  
CREATE TABLE IF NOT EXISTS packages (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT UNIQUE NOT NULL,  
    version TEXT NOT NULL,  
    install_size INTEGER NOT NULL,  
    installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
)  
""")  

cursor.execute("""  
CREATE TABLE IF NOT EXISTS files (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    package_id INTEGER NOT NULL,  
    path TEXT UNIQUE NOT NULL,  
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE  
)  
""")  

cursor.execute("""  
CREATE TABLE IF NOT EXISTS dependencies (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    package_id INTEGER NOT NULL,  
    dependency_name TEXT NOT NULL,  
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE  
)  
""")  

conn.commit()  
conn.close()  
print("Database initialized: mypkg.db")  
