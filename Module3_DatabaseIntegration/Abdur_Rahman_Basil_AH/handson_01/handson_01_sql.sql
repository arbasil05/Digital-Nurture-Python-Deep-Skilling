CREATE DATABASE college_db;

USE college_db;

-- CREATING THE TABLES

CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);



CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,

    CONSTRAINT fk_student_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    CONSTRAINT fk_course_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);



CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),

    CONSTRAINT fk_professor_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- enrollment_date and grade depend only on enrollment_id.
-- The table contains no transitive dependencies and satisfies 3NF.

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),

    CONSTRAINT fk_enrollment_student
        FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    CONSTRAINT fk_enrollment_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);


-- Display all tables
SHOW TABLES;

-- Display table structures
DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE professors;
DESCRIBE enrollments;

-- Display complete table definitions
SHOW CREATE TABLE departments;
SHOW CREATE TABLE students;
SHOW CREATE TABLE courses;
SHOW CREATE TABLE professors;
SHOW CREATE TABLE enrollments;

-- TASK 3

-- Altering Students table to add a new column called phone_number.
ALTER TABLE students ADD phone_number VARCHAR(15);

-- Add a column max_seats INT DEFAULT 60 to the courses table.
ALTER TABLE courses ADD max_seats INT DEFAULT 60;

--  Add a CHECK constraint to enrollments ensuring grade is one of ('A','B','C','D','F') or NULL.
ALTER TABLE enrollments ADD CONSTRAINT chk_grade CHECK (grade IN ('A', 'B', 'C', 'D', 'F'));

-- Rename the hod_name column in departments to head_of_dept (PostgreSQL: ALTER COLUMN ...RENAME TO; MySQL: ALTER TABLE ... CHANGE ...)
ALTER TABLE departments CHANGE hod_name head_of_dept VARCHAR(100);

-- Drop the phone_number column you added in step 1 (simulate a schema rollback)
ALTER TABLE students DROP COLUMN phone_number;
