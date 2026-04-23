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
               
    specialization TEXT NOT NULL DEFAULT 'General',
    oncology_type TEXT NOT NULL DEFAULT 'Diagnostic',
               
    breast_cancer_specialist INTEGER DEFAULT 0,

    years_of_experience INTEGER DEFAULT 0,
    cases_handled INTEGER DEFAULT 0,
    malignant_case_experience INTEGER DEFAULT 0,
    benign_case_experience INTEGER DEFAULT 0,
               
    treatment_types TEXT DEFAULT 'Not Specified',
    diagnostic_skills TEXT DEFAULT 'Basic',
    
    hospital_affiliation TEXT DEFAULT 'Not Specified',
    location TEXT DEFAULT 'UNKNOWN',         
    availability TEXT DEFAULT 'Based on appointments',
               
    rating REAL DEFAULT 0,
    description TEXT DEFAULT 'No description provided'
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

#---------------------------------------------
#SMART RECCOMNDATION
#---------------------------------------------

#Malignant
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(1, 3, 5)") #expert radiologist
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(3, 3, 5)") #expert surgeon
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(4, 3, 4)") #SECONDARY SPECIALIST

#Benign
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(2, 2, 5)") #imaging expert 
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(4, 2, 3)") #oncologist
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(1, 2, 3)") #support doctor

#Normal
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(2, 1, 4)")
cursor.execute("INSERT OR IGNORE INTO doctor_diagnosis VALUES(1, 1, 3)")    

#Doctors
cursor.execute("""
INSERT OR IGNORE INTO doctors (
id, name, email, password, specialization, oncology_type, breast_cancer_specialist, 
years_of_experience, cases_handled, malignant_case_experience, benign_case_experience, 
treatment_types, diagnostic_skills, hospital_affiliation, location, availability, rating, description)
VALUES 
               
(1, 'Dr. Dave Doe', 'dave@example.com', 'pass', 'Radiologist', 'diagnostic', 1, 12, 200, 90, 110, 'MRI, Ultrasound', 'Imaging', 'Cancer Hospital', 'London', 'Mon-Fri', 4.5, 'Senior radiologist'),

(2, 'Dr. Jane Smith', 'jane@example.com', 'pass', 'Oncologist', 'medical', 1, 15, 300, 150, 80, 'Chemotherapy', 'CT Scan', 'City Hospital', 'London', 'Mon-Fri', 4.8, 'Cancer treatment expert'),

(3, 'Dr. John Lee', 'john@example.com', 'pass', 'Surgeon', 'surgical', 1, 8, 220, 120, 60, 'Surgery', 'Biopsy', 'Royal Hospital', 'London', 'Mon-Fri', 4.6, 'Breast surgery specialist'),

(4, 'Dr. Emily Carter', 'emily@example.com', 'pass', 'Radiologist', 'diagnostic', 1, 10, 180, 70, 90, 'MRI', 'Ultrasound', 'General Hospital', 'Manchester', 'Mon-Fri', 4.3, 'Imaging expert'),

(5, 'Dr. Ahmed Khan', 'ahmed@example.com', 'pass', 'Oncologist', 'medical', 1, 20, 500, 200, 150, 'Radiation Therapy', 'CT Scan', 'Cancer Institute', 'London', '24/7', 4.9, 'Senior oncologist'),

(6, 'Dr. Sarah Lee', 'sarah@example.com', 'pass', 'Pathologist', 'diagnostic', 1, 9, 100, 50, 40, 'Lab Analysis', 'Biopsy', 'Medical Center', 'London', 'Mon-Fri', 4.2, 'Pathology specialist')
               
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