import sqlite3
#---------------------------------------------
#CONNECT TO DATABASE
#---------------------------------------------
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#---------------------------------------------
#DOCTORS TABLE 
#---------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    password TEXT,
               
    specialization TEXT,
    oncology_type TEXT,
               
    breast_cancer_specialist BOOLEAN DEFAULT 0,

    years_of_experience INTEGER,
    cases_handled INTEGER,
    malignant_case_experience INTEGER,
    benign_case_experience INTEGER,
               
    treatment_types TEXT,
    diagnostic_skills TEXT,
    
    hospital_affiliation TEXT,
    location TEXT,
               
    availability TEXT,
    rating REAL DEFAULT 0,
               
    description TEXT
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
#DIAGNOSIS TABLE
#---------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS diagnosis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT CHECK(type IN ('Normal', 'Benign', 'Malignant')),
    description TEXT
)
""")
#----------------------------------------------
#SMART RECCOMNDATION 
#---------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctor_diagnosis (
    doctor_id INTEGER,
    diagnosis_id INTEGER,
    priority_level INTEGER,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id),
    FOREIGN KEY (diagnosis_id) REFERENCES diagnosis(id)
)
""")

#---------------------------------------------
#INSERT SAMPLE DATA
#---------------------------------------------

#Diagnosis
cursor.execute("INSERT OR IGNORE INTO diagnosis (id, type) VALUES (1, 'Normal')")
cursor.execute("INSERT OR IGNORE INTO diagnosis (id, type) VALUES (2, 'Benign')")
cursor.execute("INSERT OR IGNORE INTO diagnosis (id, type) VALUES (3, 'Malignant')")

#Doctors
cursor.execute("""
INSERT OR IGNORE INTO doctors 
               (id, name, email, password, specialization, oncology_type, breast_cancer_specialist, 
               years_of_experience, malignant_case_experience, benign_case_experience, 
               treatment_types, diagnostic_skills, hospital_affiliation, location, availability, rating, description)
VALUES 
               (1, 'Dr. Dave Doe', 'dr.davedoe@example.com', 'password@123', 'Oncologist', 'medical', 1, 15, 200, 50, 'Chemotherapy, Immunotherapy', 'Ultrasound', 'Cancer Hospital', 'London', 'Mon-Fri 9am-5pm', 4.5, 'Experienced oncologist specializing in breast cancer.')
""")
#---------------------------------------------
#MATCHING 
#---------------------------------------------
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(1, 3, 5)") #Malignant 

#----------------------------------------------
#SAVE AND CLOSE
#---------------------------------------------
conn.commit()
conn.close()

print("Database created succesfully")