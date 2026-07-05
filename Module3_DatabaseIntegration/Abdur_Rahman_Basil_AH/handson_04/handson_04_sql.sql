-- Task 1 Baseline Performance - No Indexes

-- Run EXPLAIN (PostgreSQL) or EXPLAIN FORMAT=JSON (MySQL) on the following query and save_
-- the output as a comment in your .sql file: SELECT s.first_name, s.last_name, c.course_name FROM
-- enrollments e JOIN students s ON s.student_id = e.student_id JOIN courses c ON c.course_id =
-- e.course_id WHERE s.enrollment_year = 2022;

EXPLAIN FORMAT=JSON 
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e 
JOIN students s ON s.student_id = e.student_id 
JOIN courses c ON c.course_id = e.course_id 
WHERE s.enrollment_year = 2022;

-- OUTPUT:

-- [
-- 	{
-- 		"EXPLAIN" : "{\n  \"query\": \"/* select#1 */ select `s`.`first_name` AS `first_name`,`s`.`last_name` AS `last_name`,`c`.`course_name` AS `course_name` from `college_db`.`enrollments` `e` join `college_db`.`students` `s` join `college_db`.`courses` `c` where ((`e`.`student_id` = `s`.`student_id`) and (`c`.`course_id` = `e`.`course_id`) and (`s`.`enrollment_year` = 2022))\",\n  \"query_plan\": {\n    \"inputs\": [\n      {\n        \"inputs\": [\n          {\n            \"inputs\": [\n              {\n                \"alias\": \"s\",\n                \"operation\": \"Table scan on s\",\n                \"table_name\": \"students\",\n                \"access_type\": \"table\",\n                \"schema_name\": \"college_db\",\n                \"used_columns\": [\n                  \"student_id\",\n                  \"first_name\",\n                  \"last_name\",\n                  \"enrollment_year\"\n                ],\n                \"estimated_rows\": 10.0,\n                \"estimated_total_cost\": 2.0\n              }\n            ],\n            \"condition\": \"(s.enrollment_year = 2022)\",\n            \"operation\": \"Filter: (s.enrollment_year = 2022)\",\n            \"access_type\": \"filter\",\n            \"estimated_rows\": 1.0000000149011612,\n            \"filter_columns\": [\n              \"s.enrollment_year\"\n            ],\n            \"estimated_total_cost\": 2.0\n          },\n          {\n            \"inputs\": [\n              {\n                \"alias\": \"e\",\n                \"covering\": false,\n                \"operation\": \"Index lookup on e using student_id (student_id = s.student_id)\",\n                \"index_name\": \"student_id\",\n                \"table_name\": \"enrollments\",\n                \"access_type\": \"index\",\n                \"key_columns\": [\n                  \"student_id\"\n                ],\n                \"schema_name\": \"college_db\",\n                \"used_columns\": [\n                  \"student_id\",\n                  \"course_id\"\n                ],\n                \"estimated_rows\": 2.375,\n                \"lookup_condition\": \"student_id = s.student_id\",\n                \"index_access_type\": \"index_lookup\",\n                \"lookup_references\": [\n                  \"college_db.s.student_id\"\n                ],\n                \"estimated_total_cost\": 2.237499996460974\n              }\n            ],\n            \"condition\": \"(e.course_id is not null)\",\n            \"operation\": \"Filter: (e.course_id is not null)\",\n            \"access_type\": \"filter\",\n            \"estimated_rows\": 2.375,\n            \"filter_columns\": [\n              \"e.course_id\"\n            ],\n            \"estimated_total_cost\": 2.237499996460974\n          }\n        ],\n        \"join_type\": \"inner join\",\n        \"operation\": \"Nested loop inner join\",\n        \"access_type\": \"join\",\n        \"estimated_rows\": 2.375000035390258,\n        \"join_algorithm\": \"nested_loop\",\n        \"estimated_total_cost\": 4.237500033341348\n      },\n      {\n        \"alias\": \"c\",\n        \"covering\": false,\n        \"operation\": \"Single-row index lookup on c using PRIMARY (course_id = e.course_id)\",\n        \"index_name\": \"PRIMARY\",\n        \"table_name\": \"courses\",\n        \"access_type\": \"index\",\n        \"key_columns\": [\n          \"course_id\"\n        ],\n        \"schema_name\": \"college_db\",\n        \"used_columns\": [\n          \"course_id\",\n          \"course_name\"\n        ],\n        \"estimated_rows\": 1.0,\n        \"lookup_condition\": \"course_id = e.course_id\",\n        \"index_access_type\": \"index_lookup\",\n        \"lookup_references\": [\n          \"college_db.e.course_id\"\n        ],\n        \"estimated_total_cost\": 1.0421052625304774\n      }\n    ],\n    \"join_type\": \"inner join\",\n    \"operation\": \"Nested loop inner join\",\n    \"access_type\": \"join\",\n    \"estimated_rows\": 2.375000035390258,\n    \"join_algorithm\": \"nested_loop\",\n    \"estimated_total_cost\": 6.850000072270632\n  },\n  \"query_type\": \"select\",\n  \"json_schema_version\": \"2.0\"\n}"
-- 	}
-- ]

-- Identify whether the query plan shows a Sequential Scan (Postgres) or Full Table Scan (MySQL) on
-- any table.

--  It does a Full Table scan on 'students' table
--  Estimated rows examined: 10
--  Overall estimated cost : ~6.85

-- -------------------------------------------
--  TASK 2
-- -------------------------------------------

-- Create B Tree Index on students.enrollment_year

CREATE INDEX idx_enrollment_year ON students(enrollment_year);

-- Create a composite UNIQUE index on enrollments(student_id, course_id) — this also prevents duplicate enrollments.

CREATE UNIQUE INDEX idx_student_course ON enrollments(student_id,course_id);

--  Create an inndex on courses.course_code

CREATE INDEX idx_course_code ON courses(course_code);

-- After rerunning the explain

-- It does a Index scan on 'students' table
-- "operation": "Index lookup on s using idx_enrollment_year (enrollment_year = 2022)"
-- Estimated rows examined: 5.0
-- Overall estimated cost : ~7.03

--  In mysql it is not possible to create a true partial index with where clause because it will not support
--  partial indexes. We have to do workarounds. we create a regular index on grade instead
CREATE INDEX idx_unevaluated_enrollments ON enrollments(grade);

