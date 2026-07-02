# Course Management System – Microservices Architecture

## Overview

This project demonstrates how a monolithic **Course Management System** can be decomposed into independent microservices using Domain-Driven Design (DDD) principles and bounded contexts.

Each service is responsible for a specific business capability, owns its own database, and exposes only the APIs related to its domain.

> **Note:** For this implementation, only the **Course Service** and **Student Service** are developed to demonstrate microservice communication.

---

# Service Architecture

| Service                  | Responsibility                                            | API Endpoints                     | Database                              |
| ------------------------ | --------------------------------------------------------- | --------------------------------- | ------------------------------------- |
| **Auth Service**         | Handles user authentication, registration, and security.  | `POST /register`<br>`POST /login` | `auth.db` (Users, Passwords)          |
| **Course Service**       | Manages the academic course catalog and departments.      | `GET /courses`<br>`POST /courses` | `courses.db` (Courses, Departments)   |
| **Student Service**      | Manages student profiles and course enrollments.          | `GET /students`<br>`POST /enroll` | `students.db` (Students, Enrollments) |
| **Notification Service** | Handles asynchronous notifications such as email and SMS. | Listens to background events      | Stateless (No Database)               |

---

# Microservices Implemented

## Course Service

### Responsibilities

* Create new courses
* Retrieve available courses
* Manage the academic course catalog
* Own the Course database

### Database

```
courses.db
├── Courses
└── Departments
```

### API Endpoints

```
GET  /courses
POST /courses
```

---

## Student Service

### Responsibilities

* Manage student information
* Enroll students into courses
* Demonstrate communication with the Course Service
* Own the Student database

### Database

```
students.db
├── Students
└── Enrollments
```

### API Endpoints

```
GET  /students
POST /enroll
```

---

# Planned Services

## Auth Service

Responsible for:

* User Registration
* User Login
* Password Management
* Authentication & Authorization

**Endpoints**

```
POST /register
POST /login
```

**Database**

```
auth.db
├── Users
└── Passwords
```

---

## Notification Service

Responsible for:

* Email Notifications
* SMS Notifications
* Event-driven communication

This service is **stateless** and listens to events published by other services.

---

# Service Communication

```
                +-------------------+
                |   Student Service |
                +-------------------+
                          |
                          | HTTP / REST
                          v
                +-------------------+
                |   Course Service  |
                +-------------------+
```

The Student Service communicates with the Course Service to validate course information during enrollment.

---

# Database Ownership

Each microservice owns its own database.

```
Auth Service
    └── auth.db

Course Service
    └── courses.db

Student Service
    └── students.db

Notification Service
    └── No Database
```

This ensures loose coupling, independent deployment, and better scalability.

---

# Project Goal

This project demonstrates:

* Microservices decomposition
* Bounded contexts
* Database-per-service pattern
* Service-to-service communication
* Separation of business domains
* Independent service ownership

## Inter-Service Communication Trade-offs

### Synchronous Communication (HTTP / REST)
* **How it works:** Service A makes an HTTP request to Service B and waits for the response (like our Student Service verifying a course).
* **Pros:** Easy to implement, simple to debug, and conceptually straightforward.
* **Cons (Tight Coupling):** If the Course Service goes down, the Student Service enrollment endpoint fails entirely. It causes cascading failures and increases latency since it waits for a response.

### Asynchronous Communication (Message Queues)
* **How it works:** Service A drops a message into a queue (like RabbitMQ or Kafka) saying "Student 1 wants to enroll in Course 1" and immediately returns a success to the user. Service B picks up the message whenever it's ready.
* **Pros (Loose Coupling):** Highly scalable. If the Course Service crashes, the message just waits in the queue until the service comes back online. The user doesn't experience a failure.
* **Cons:** Much more complex to set up and debug. Introduces "eventual consistency" (the data isn't perfectly synced the very millisecond the request finishes).
