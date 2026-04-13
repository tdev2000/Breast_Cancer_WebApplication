import sqlite3
#---------------------------------------------
#CONNECT TO DATABASE
#---------------------------------------------
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#---------------------------------------------
#DOCTORS TABLE (LOGIN)
#---------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    specialization TEXT  
) 
""")

#---------------------------------------------
#PATIENTS TABLE
#---------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    date_of_birth TEXT,
    history INTEGER,
    prediction TEXT,
    confidence REAL,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
)
""")

#---------------------------------------------
#INSERT SAMPLE DOCTOR
#---------------------------------------------
cursor.execute("""
INSERT OR IGNORE INTO doctors (id, name, email, password, specialization)
VALUES (1, 'Dr. Dave Doe', 'dr.davedoe@example.com', 'password123', 'A medical oncologist')
""")

#---------------------------------------------
#SAVE AND CLOSE
#---------------------------------------------
conn.commit()
conn.close()

print("Database created succesfully")