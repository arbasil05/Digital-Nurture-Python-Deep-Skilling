# Task 2: Verify Normalisation

## 1. First Normal Form (1NF)

### Definition

A table is in **First Normal Form (1NF)** if:

- Every column contains only atomic (indivisible) values.
- Each record is unique.
- There are no repeating groups or multiple values stored in a single column.

### Analysis

The `college_db` schema satisfies **1NF** because:

- Every column stores a single value.
- There are no arrays or comma-separated values.
- Each table has a primary key that uniquely identifies every record.

### Hypothetical Violation

The following table **violates 1NF** because multiple phone numbers are stored in a single column.

| student_id | first_name | phone_numbers |
|------------|------------|---------------|
| 101 | John | 9876543210, 9123456780 |

This violates 1NF because the `phone_numbers` column contains multiple values.

A better design would be:

| student_id | phone_number |
|------------|--------------|
| 101 | 9876543210 |
| 101 | 9123456780 |

---

## 2. Second Normal Form (2NF)

### Definition

A table is in **Second Normal Form (2NF)** if:

- It is already in 1NF.
- Every non-key attribute is fully dependent on the entire primary key.
- There are no partial dependencies.

### Analysis

The `departments`, `students`, `courses`, and `professors` tables each have a single-column primary key, so partial dependency is not possible.

The `enrollments` table has a surrogate primary key (`enrollment_id`) and a candidate key consisting of (`student_id`, `course_id`).

Its non-key attributes are:

- `enrollment_date`
- `grade`

Both attributes describe the enrollment itself and depend on the relationship between a student and a course rather than only one of them.

Therefore, the schema satisfies **2NF**.

---

## 3. Third Normal Form (3NF)

### Definition

A table is in **Third Normal Form (3NF)** if:

- It is already in 2NF.
- There are no transitive dependencies.
- Non-key attributes depend only on the primary key.

### Analysis

The schema satisfies **3NF** because:

- Department information is stored only in the `departments` table.
- Student records store only the `department_id` instead of duplicating department details.
- Course records reference departments using `department_id`.
- Professor records reference departments using `department_id`.
- The `enrollments` table stores only information related to a student's enrollment in a course.

### Hypothetical Violation

Suppose the `students` table contained the following columns:

| student_id | first_name | department_id | dept_name |
|------------|------------|---------------|-----------|
| 101 | John | 1 | Computer Science |

Here, `dept_name` depends on `department_id` rather than directly on `student_id`.

This creates a **transitive dependency**, violating **3NF**.

Instead, only `department_id` should be stored in the `students` table, while `dept_name` remains in the `departments` table.

---