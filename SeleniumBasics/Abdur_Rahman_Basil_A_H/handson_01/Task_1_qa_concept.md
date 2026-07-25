# TASK 1: Map Testing Types to a Real System

---

## STEP 1

### Unit Testing
* **Description:** Testing a single function in isolation
* **Test Cases:** Test the `make_response_json(data,status_code)` helper function. If we pass the data `{"name" : "Biology"}`, the function should return a JSON object formatted exactly as `{'status':'success','data':{"name":"Biology"},'code':200}` with a 200 status code.

### Integration Testing
* **Description:** Testing two components working together
* **Test Case:** Test the integration between `POST /api/courses/` endpoint and SQLAlchemy database (db). When a valid JSON payload `(containing name, code, credits, department_id)` is sent to the endpoint, verify that a new `Course` record is successfully committed and saved in the database tables.

### System Testing
* **Description:** Testing a full end-to-end flow.
* **Test Case:** Test the complete course creation flow over HTTP. Send an HTTP POST request to `/api/courses/` with course data, verify the API returns a `201 Created` status code, and then immediately send a `GET /api/courses/` request to ensure the newly created course is returned in the full list of courses.

### User Acceptance Testing (UAT)
* **Description:** Testing from the perspective of an actual user.
* **Test Case:** As a college administrator, I want to log into the system and add a new 4-credit course called "Intro to Python" so that it appears in the active college catalog for students to enroll in next semester.

---

## STEP 2: Functional vs. Non-Functional Testing

### Classification of Step 1 Tests
All four test cases provided in Step 1 (Unit, Integration, System, and UAT) are Functional Tests. They verify what the system does—ensuring the API correctly processes inputs, saves data to the database, and returns the expected values.

### Non-Functional Test Example
* **Test Type:** Performance Testing (Non-Functional)
* **Description:** Testing how well (how fast and reliably) the API handles high traffic.
* **Concrete Test Case:** Send 500 simultaneous GET requests per second to the GET /api/courses/ endpoint. Verify that the server does not crash and that the average response time remains under 200 milliseconds.

---

## STEP 3: Black-Box vs. White-Box Testing

### Black-Box Testing
* **Definition:** Testing software without any knowledge of its internal code, structure, or implementation details. The tester only focuses on providing inputs and verifying if the outputs match the expected results.
* **Who performs it:** Typically performed by QA Testers. They test the application exactly as an end-user would, focusing on the software's requirements and behavior.

### White-Box Testing
* **Definition:** Testing software with full knowledge of its internal source code and logic. The tester writes tests specifically to verify the internal workings, loops, database connections, and specific functions.
* **Who performs it:** Typically performed by Developers. They write unit and integration tests (like we discussed in Step 1) as they are building the application.

---

## STEP 4: Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_001** | Verify successful creation of a course when all required fields are provided. | API server is running and database is connected. | 1. Send a POST request to /api/courses/.<br>2. Include a valid JSON body: {"name": "Physics", "code": "PHY101", "credits": 4, "department_id": 1}. | API returns a 201 Created status code. Response JSON shows status: 'success' and includes the new course data. | | |
| **TC_002** | Verify API returns an error when a required field is missing. | API server is running. | 1. Send a POST request to /api/courses/.<br>2. Include a JSON body missing the credits field: {"name": "Physics", "code": "PHY101", "department_id": 1}. | API returns a 400 Bad Request status. Response JSON shows status: 'error' and message: 'Missing required field: credits'. | | |
| **TC_003** | Verify API returns an error when the JSON payload is completely empty. | API server is running. | 1. Send a POST request to /api/courses/.<br>2. Do not include any JSON body (empty request). | API returns a 400 Bad Request status. Response JSON shows status: 'error' and message: 'Invalid or missing JSON payload'. | | |

