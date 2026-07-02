-- TASK 1

-- departments

INSERT INTO departments (dept_name, hod_name, budget) VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00),
('Architecture', 'Ted Mosby', 900000.00),
('Business Administration', 'Barney Stinson', 850000.00),
('Law', 'Marshall Eriksen', 780000.00),
('Education', 'Lily Aldrin', 650000.00);

-- students

INSERT INTO students (first_name, last_name, email, date_of_birth, department_id, enrollment_year) VALUES
('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022),
('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022),
('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021),
('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023),
('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022),
('Kavya', 'Menon', 'kavya.menon@college.edu', '2002-05-17', 2, 2021),
('Aditya', 'Singh', 'aditya.singh@college.edu', '2004-03-22', 4, 2023),
('Deepika', 'Rao', 'deepika.rao@college.edu', '2003-08-09', 1, 2022),
('Emma', 'Johnson', 'emma.johnson@college.edu', '2003-02-14', 5, 2022),
('Olivia', 'Williams', 'olivia.williams@college.edu', '2004-06-18', 6, 2023),

-- courses

INSERT INTO courses (course_name, course_code, credits, department_id) VALUES
('Data Structures & Algorithms', 'CS101', 4, 1),
('Database Management Systems', 'CS102', 3, 1),
('Object Oriented Programming', 'CS103', 4, 1),
('Circuit Theory', 'EC101', 3, 2),
('Thermodynamics', 'ME101', 3, 3),
('Cloud Computing', 'CC301', 4, 5),
('Artificial Intelligence', 'AI302', 4, 6),
('Operating Systems', 'OS201', 3, 7),
('Computer Networks', 'CN205', 3, 8),
('Cyber Security', 'CS401', 4, 5);

-- enrollments

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2022-07-01', 'A'),
(1, 2, '2022-07-01', 'B'),
(2, 1, '2022-07-01', 'B'),
(2, 3, '2022-07-01', 'A'),
(3, 4, '2021-07-01', 'A'),
(4, 5, '2023-07-01', NULL),
(5, 1, '2022-07-01', 'C'),
(5, 2, '2022-07-01', 'A'),
(6, 4, '2021-07-01', 'B'),
(7, 5, '2023-07-01', NULL),
(8, 1, '2022-07-01', 'A'),
(8, 3, '2022-07-01', 'B'),
(9, 6, '2022-07-10', 'A'),
(9, 10, '2022-07-10', 'B'),
(10, 7, '2023-07-15', 'A'),
(11, 8, '2021-07-12', 'B'),
(12, 9, '2022-07-20', 'A'),
(13, 6, '2023-07-18', NULL),
(14, 7, '2022-07-14', 'A'),
(15, 8, '2021-07-12', 'C'),
(16, 9, '2023-07-16', NULL),
(16, 10, '2023-07-16', 'B');

-- professors

INSERT INTO professors (prof_name, email, department_id, salary) VALUES
('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00),
('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00),
('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00),
('Dr. Latha Gopal', 'latha.g@college.edu', 3, 79000.00),
('Dr. Kartik Bose', 'kartik.b@college.edu', 4, 76000.00),
('Richard Hendricks', 'richard@college.edu', 5, 98000.00),
('Bertram Gilfoyle', 'gilfoyle@college.edu', 6, 102000.00),
('Dinesh Chugtai', 'dinesh@college.edu', 7, 95000.00),
('Jared Dunn', 'jared@college.edu', 8, 91000.00),
('Monica Hall', 'monica@college.edu', 5, 99000.00);

-- Update the grade of student_id = 5 for course_id = 1 from 'C' to 'B'
UPDATE enrollments SET grade = 'B' WHERE student_id = 5 and course_id = 1;

-- Delete enrollments where grade IS NULL
DELETE FROM enrollments WHERE grade IS NULL;

-- Verify row counts using SELECT COUNT(*) after each operation.
SELECT COUNT(*) FROM departments;
SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM courses;
SELECT COUNT(*) FROM enrollments;
SELECT COUNT(*) FROM professors;

-------------------------------------------------------------

-- TASK 2

--  Retrieve all students enrolled in 2022, ordered by last_name alphabetically
SELECT * FROM students WHERE enrollment_year = 2022 ORDER BY last_name;

-- Find all courses with more than 3 credits, sorted by credits descending.
SELECT * FROM courses WHERE credits > 3 ORDER BY credits DESC;

-- List all professors whose salary is between 80,000 and 95,000
SELECT * FROM professors WHERE salary BETWEEN 80000 AND 950000;

--  Find all students whose email ends with '@college.edu' using the LIKE operator
SELECT * FROM students WHERE email LIKE '%@college.edu';

-- Count the total number of students per enrollment_year.
SELECT enrollment_year,count(*) AS count_by_enrollment_year FROM students GROUP BY enrollment_year;

-------------------------------------------------------------

-- TASK 3

-- List each student's full name (first_name + ' ' + last_name) alongside the name of their department.(JOIN students and departments.)
SELECT s.first_name,s.last_name,d.dept_name from students s
INNER JOIN departments d ON
s.department_id = d.department_id;

-- Show each enrollment along with the student's name and the course name. (3-table JOIN:enrollments, students, courses.)
SELECT 
	e.enrollment_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name
    c.course_name
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON c.course_id = e.course_id;

-- Find all students who are NOT enrolled in any course using a LEFT JOIN and WHERE ... IS NULL pattern
SELECT * FROM students
LEFT JOIN enrollments ON
enrollments.student_id = students.student_id
WHERE course_id is NULL;

-- Display every course along with the number of students enrolled in it. Courses with zero enrolments must still appear. (LEFT JOIN courses with enrollments, GROUP BY course.)
SELECT
    courses.course_name,
    COUNT(enrollments.student_id) AS total_students
FROM courses
LEFT JOIN enrollments
ON courses.course_id = enrollments.course_id
GROUP BY courses.course_name;

-- List each department along with its professors and their salaries. Include departments that have no professors yet.
SELECT
	departments.dept_name,
    professors.prof_name,
    professors.salary
FROM 	departments
LEFT JOIN professors
ON professors.department_id = departments.department_id;

-------------------------------------------------------------

-- TASK 4

-- Calculate the total number of enrollments per course. Display course_name and enrollment_count.

SELECT
	courses.course_name AS 'course_name',
    count(enrollments.course_id) AS 'enrollment_count'
FROM courses
INNER JOIN enrollments
ON courses.course_id = enrollments.course_id
GROUP BY courses.course_name;

-- Find the average salary of professors per department. Round to 2 decimal places.
SELECT
	departments.dept_name,
	ROUND(AVG(professors.salary),2) AS 'Average Salary'
FROM departments
INNER JOIN professors
ON departments.department_id = professors.department_id
GROUP BY departments.dept_name;

-- Find all departments where the total budget exceeds 600,000.
SELECT * FROM departments WHERE budget > 600000;

-- . Show the grade distribution for course CS101: count of each grade (A, B, C, D, F).
SELECT
    enrollments.grade,
    COUNT(enrollments.grade) AS 'Grade Count'
FROM enrollments
INNER JOIN courses
ON enrollments.course_id = courses.course_id
WHERE courses.course_code = 'CS101'
GROUP BY enrollments.grade;

-- Using HAVING, list departments where more than 2 students are enrolled across all courses in that department

SELECT
    d.dept_name,
    COUNT(s.student_id) AS total_students
FROM departments d
INNER JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(s.student_id) > 2;








