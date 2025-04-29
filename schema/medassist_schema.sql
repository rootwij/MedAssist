
-- Table: patients
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE,
    gender TEXT,
    email TEXT UNIQUE,
    phone TEXT
);

-- Table: medications
CREATE TABLE medications (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    name TEXT,
    start_date DATE,
    frequency TEXT,
    time_of_day TEXT
);

-- Table: appointments
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    specialist TEXT,
    appointment_date TIMESTAMP,
    urgency_level TEXT
);

-- Table: ehr_records
CREATE TABLE ehr_records (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    diagnosis TEXT,
    visit_date DATE,
    summary TEXT
);
