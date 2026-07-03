-- TASK 1

-- Find all students who are enrolled in more courses than the average number of enrollments per student

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    COUNT(e.course_id) AS courses_enrolled
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(enrollment_count)
    FROM
    (
        SELECT COUNT(*) AS enrollment_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_enrollments
);

-- List courses in which all enrolled students have received a grade of 'A'.

SELECT
    c.course_name,
    c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND (e.grade <> 'A' OR e.grade IS NULL)
);

-- Find the professor with the highest salary in each department.

SELECT
    p.prof_name,
    d.dept_name,
    p.salary
FROM professors p
INNER JOIN departments d
ON p.department_id = d.department_id
WHERE p.salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- Using a derived table, calculate the average salary per department and display departments whose average salary exceeds 85,000.

SELECT
    dept_name,
    average_salary
FROM
(
    SELECT
        d.dept_name,
        ROUND(AVG(p.salary), 2) AS average_salary
    FROM departments d
    INNER JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.department_id, d.dept_name
) AS department_salary
WHERE average_salary > 85000;

-- TASK 2

----------------------------------------------------------------

-- Create vw_student_enrollment_summary

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4
                WHEN 'B' THEN 3
                WHEN 'C' THEN 2
                WHEN 'D' THEN 1
                WHEN 'F' THEN 0
            END
        ),2
    ) AS gpa
FROM students s
INNER JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, full_name, d.dept_name;

-- Create vw_course_stats

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4
                WHEN 'B' THEN 3
                WHEN 'C' THEN 2
                WHEN 'D' THEN 1
                WHEN 'F' THEN 0
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name, c.course_code;

-- Find students with GPA above 3.0
SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3.0;

-- Attempt to UPDATE through the view

UPDATE vw_student_enrollment_summary
SET full_name = 'Emma Watson'
WHERE student_id = 9;

--ERROR
--ERROR 1288 (HY000):
--The target table vw_student_enrollment_summary
--of the UPDATE is not updatable.

-- Multi-table views containing JOIN, GROUP BY or aggregate
-- functions are generally not updatable because MySQL
-- cannot determine which underlying table should be modified.

-- Drop both views

DROP VIEW vw_student_enrollment_summary;
DROP VIEW vw_course_stats;

-- Recreate vw_student_enrollment_summary using a single table with WITH CHECK OPTION

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    email,
    enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH CHECK OPTION;

-- Test check options

UPDATE vw_student_enrollment_summary
SET enrollment_year = 2023
WHERE student_id = 1;

-- TASK 3

----------------------------------------------------------------



-- Create Department Transfer Log Table
CREATE TABLE department_transfer_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_date DATE
);

DELIMITER $$

-- Stored Procedure to enroll a student checking for duplicates
CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    DECLARE v_count INT;

    SELECT COUNT(*) INTO v_count
    FROM enrollments
    WHERE student_id = p_student_id AND course_id = p_course_id;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Duplicate enrollment. Student is already enrolled in this course.';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
    END IF;
END$$

-- Stored Procedure to transfer student with transactions
CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department_id INT
)
BEGIN
    DECLARE v_old_department_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Transfer failed. Transaction rolled back.';
    END;

    START TRANSACTION;

    SELECT department_id INTO v_old_department_id
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department_id
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_department_id, new_department_id, transfer_date)
    VALUES (p_student_id, v_old_department_id, p_new_department_id, CURDATE());

    COMMIT;
END$$

DELIMITER ;

-- Test transaction rollback
SELECT student_id, department_id FROM students WHERE student_id = 1;
-- CALL sp_transfer_student(1, 999);
SELECT student_id, department_id FROM students WHERE student_id = 1;

-- Test SAVEPOINT functionality
START TRANSACTION;
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (1, 3, CURDATE(), 'B');
SAVEPOINT after_first_enrollment;
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (999, 3, CURDATE(), 'A');
ROLLBACK TO SAVEPOINT after_first_enrollment;
COMMIT;
SELECT * FROM enrollments WHERE student_id = 1 AND course_id = 3;
