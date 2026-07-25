# TASK 2: Defect Lifecycle & Classification

---

## STEP 5: The Detect Lifecycle

The defect lifecycle represents the journey a bug takes from discovery to resolution. Here is the standard flow:

### The Main Path (Happy Path for Bug Fixing)
* **New:** A QA tester finds a bug and logs it for the first time.
* **Assigned:** The QA lead or project manager assigns the bug to a specific developer.
* **Open:** The developer starts actively working on analyzing and fixing the bug.
* **Fixed:** The developer has made the code changes and pushed them. They pass it back to QA.
* **Retest:** The QA tester re-runs the exact steps from the original bug report to see if it still happens.
* **Verified:** The QA tester confirms the bug is actually gone.
* **Closed:** The bug is officially shut down. End of the line!

### Alternative Paths
* **Rejected:** The developer looks at the "bug" and decides it is not actually a bug (e.g., the system is working as intended, or it's a duplicate of another bug). The bug skips straight to Closed.
* **Deferred:** The bug is real, but it's not important enough to fix right now. It is pushed to a future release or backlog.

---

## STEP 6: Bug Classification (Severity vs Priority)

### a) POST /api/courses/ returns 500 Internal Server Error for all requests.
* **Severity:** Critical
* **Priority:** P1
* **Justification:** Core functionality (adding a course) is completely broken for everyone, and there is no workaround. It causes a server crash (500 error). This is a "showstopper" that must be fixed immediately before any other work continues.

### b) Course names longer than 150 characters are silently truncated without an error.
* **Severity:** Medium
* **Priority:** P3
* **Justification:** The system still functions, and courses are still being created, but there is minor data loss (truncation) occurring for extreme edge cases. It's an annoying bug that needs fixing, but it doesn't stop the system from working for 99% of users.

### c) The /docs Swagger page has a typo in the API description.
* **Severity:** Low
* **Priority:** P4
* **Justification:** This is purely a cosmetic issue. It has absolutely zero impact on the actual functionality of the API or the database. It can be fixed whenever a developer has some free time.

### d) Login with correct credentials occasionally returns 401 on the first attempt (intermittent).
* **Severity:** Medium
* **Priority:** P1 (or P2)
* **Justification:** The severity is Medium because the user can eventually log in (there is a workaround: just try again). However, the priority is very High (P1/P2) because login is the gateway to the app, it causes massive user frustration, and intermittent security bugs often point to deeper, more dangerous instability in the system.

---

## STEP 7: Defect Report

* **Defect ID:** BUG-1042
* **Title:** POST /api/courses/ endpoint fails with 500 Internal Server Error on all valid requests.
* **Environment:** QA Environment (Test Server)
* **Build Version:** API v1.2.0
* **Severity:** Critical
* **Priority:** P1
* **Steps to Reproduce:**
  1. Open Postman (or any API client).
  2. Set the request method to POST and the URL to `http://<qa-environment>/api/courses/`.
  3. Add a valid JSON payload in the request body (e.g., `{"name": "Chemistry", "code": "CHM101", "credits": 3, "department_id": 2}`).
  4. Send the request.
* **Expected Result:** The API should process the request successfully, save the course to the database, and return a 201 Created status code with the newly created course data.
* **Actual Result:** The API immediately returns a 500 Internal Server Error. The course is not saved to the database.
* **Attachments:** 'screenshot of 500 error'

---

## STEP 8: Severity vs Priority

### The Difference
* **Severity** is technical. It measures the extent of the damage the bug causes to the system. It answers: How badly is the software broken?
* **Priority** is business-driven. It measures how quickly the bug needs to be fixed based on business needs and user impact. It answers: How urgently do we need to fix this?

### Example of High Severity, but Low Priority
Imagine a bug where an application completely crashes and shows a "Fatal Error" screen (High Severity because the system breaks completely and the user is blocked).

However, this crash only happens if a user is trying to run the modern web application on an extremely outdated browser, like Internet Explorer 8. Because fewer than 0.01% of users still use Internet Explorer 8, the business decides it is not worth the developers' time to fix it immediately (Low Priority). The bug is devastating, but it affects almost nobody.
