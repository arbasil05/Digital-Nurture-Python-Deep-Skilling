# HANDSON 03: Automation Decision and Test Case Selection

---

## STEP 17: Automation Decision Criteria

Not every test should be automated. Here are 5 criteria to evaluate whether a test is a good candidate:

* **High Frequency / Repetitive:** The test is run multiple times across different builds (e.g., regression tests).
* **Stable Functionality:** The feature is complete and its behavior is not expected to change frequently (automating a feature that changes every day wastes time on maintenance).
* **High Business Criticality:** The feature is a core component; if it breaks, the business stops (e.g., checkout process, login).
* **Data-Driven Requirements:** The test needs to be run against many different sets of data (e.g., testing 50 different invalid email formats).
* **Time-Consuming Manually:** The test takes a human a long time to set up and execute, but a machine can do it in seconds.

### Application to `POST /api/courses/`
* **Scenario:** Test that the endpoint returns `201 Created` with the correct data when valid input is provided.
* **Analysis:** This is a perfect candidate for automation. Course creation is a critical business function. The API contract is stable. We will need to run this test on every single deployment (high frequency), and we can easily make it data-driven to test various valid course configurations.

---

## STEP 18: Selecting Test Cases (Automate vs. Manual)

### (a) Regression test for all CRUD endpoints after every code change
* **Decision:** Automate
* **Justification:** Regression tests are highly repetitive and time-consuming. Automating them provides instant feedback to developers after every code push.

### (b) Exploratory testing of a new search feature
* **Decision:** Manual
* **Justification:** Exploratory testing relies on human curiosity, intuition, and learning on the fly. A script cannot "explore."

### (c) Performance test: 100 concurrent users calling `GET /api/courses/`
* **Decision:** Automate
* **Justification:** It is physically impossible for a single human to simulate 100 simultaneous network requests. Tools like JMeter or Locust are required.

### (d) UI test for the login form
* **Decision:** Automate
* **Justification:** While heavy UI testing can be flaky, the login form is a highly stable, hyper-critical path that must work perfectly in every build.

### (e) Verify the API documentation (Swagger) is accurate
* **Decision:** Manual
* **Justification:** Verifying the accuracy and readability of documentation (like checking for typos or clear descriptions) requires human comprehension.

### (f) Smoke test: verify the API is reachable after deployment
* **Decision:** Automate
* **Justification:** Smoke tests gate the rest of testing. They need to run instantly after a deployment to ensure the environment isn't fundamentally broken.

---

## STEP 19: Test Automation ROI Calculation

* **Definition:** Test Automation ROI (Return on Investment) measures the time or cost saved by automating a test compared to the time/cost spent creating and maintaining that automation. Positive ROI means the script has saved you more hours than it took to write.

### The Calculation
* **Cost to Automate:** 4 hours (240 minutes)
* **Cost per Manual Run:** 30 minutes
* **Break-Even Point:** 240 minutes / 30 minutes per run = 8 runs

### Result
The automation pays for itself exactly on the 8th run. By run 8, you would have spent 240 minutes testing manually, which equals the time spent writing the script. Starting on the 9th run, you are saving 30 minutes every time it executes.

---

## STEP 20: Flaky Tests in Selenium

* **Definition:** A flaky test is an automated test that sometimes passes and sometimes fails, even when no changes have been made to the application code or the test script itself.
* **Example:** A Selenium script tries to click a "Submit" button immediately after logging in. 90% of the time, the page loads instantly and the test passes. 10% of the time, the testing server is slightly slow, the script tries to click the button before the page renders, and the test fails.

### 3 Strategies to Prevent or Fix Flaky Tests
1. **Use Explicit Waits (Never Hardcoded Sleeps):** Instead of telling the script to wait exactly 3 seconds (`Thread.sleep()`), use explicit waits to tell the script to wait until a specific condition is met (e.g., wait up to 10 seconds for the "Submit" button to be clickable).
2. **Isolate Test Data:** Tests become flaky when they rely on shared data. Ensure every test creates its own unique data at the start and deletes it at the end, so tests don't fail due to data collisions (like trying to create a user that a previous test already created).
3. **Run in a Stable, Dedicated Environment:** Network blips and server resource limits cause flakiness. Ensure automated tests run in a dedicated CI/CD environment with consistent resources, rather than a developer's local machine where background apps might slow things down.

---

## STEP 21: The 5 Automation Framework Types

### 1. Linear Framework (Record and Playback)
* **Description:** The simplest framework, where tests are recorded sequentially step-by-step. The script contains all the hardcoded data and actions in one long file, with no reusable functions.
* **Advantage:** Extremely fast to create and requires zero programming knowledge.
* **Disadvantage:** Nightmare to maintain; if the UI changes slightly, the entire script breaks and must be re-recorded.
* **Course Management Example:** Recording a quick, one-off script to ensure the main login page loads correctly after a server restart.

### 2. Modular Framework
* **Description:** The application is broken down into small, isolated modules. Testers write reusable functions (like `login()` or `navigateToCourses()`) and call those functions to build test cases.
* **Advantage:** High reusability and easier maintenance. If the login button changes, you only update the code in one place (the `login()` function).
* **Disadvantage:** Requires solid programming skills to design and implement the modular architecture.
* **Course Management Example:** Creating a reusable `addCourse(name, code, credits)` function that can be called by multiple different test scripts.

### 3. Data-Driven Framework
* **Description:** The test script is separated entirely from the test data. The script is written to loop through rows of an external file (like a CSV, JSON, or Excel sheet) and plug that data into the test steps.
* **Advantage:** Allows you to execute the exact same test case with hundreds of different inputs without rewriting code.
* **Disadvantage:** Setting up the logic to read external files and handle data parsing can be complex.
* **Course Management Example:** Testing the "Add Course" form by reading a CSV file containing 20 different combinations of valid and invalid course data.

### 4. Keyword-Driven Framework
* **Description:** Uses external tables (often Excel) containing "Action Keywords" (e.g., Click, EnterText, Verify). The automation code simply reads these keywords and executes the corresponding action.
* **Advantage:** Allows non-technical business analysts or manual testers to write automated tests purely by writing keywords in a spreadsheet.
* **Disadvantage:** Extremely high initial cost and time required to build the backend library that translates keywords into actual code.
* **Course Management Example:** A product manager writing a test in Excel: `[Login] [Admin] -> [Click] [Courses] -> [VerifyText] "Course List"`.

### 5. Hybrid Framework
* **Description:** A combination of two or more of the above frameworks (most commonly Modular + Data-Driven).
* **Advantage:** Leverages the strengths of multiple frameworks while mitigating their individual weaknesses.
* **Disadvantage:** It is the most complex architecture to build from scratch.
* **Course Management Example:** Using modular functions for the UI navigation, while feeding those functions data from a JSON file.

---

## STEP 22: Scenario Recommendation

* **Recommendation:** A Hybrid Framework (combining Data-Driven, Modular, and Keyword/BDD elements).
* **Justification:** No single basic framework meets all the team's requirements, but a Hybrid framework perfectly solves all three:
  * **"Test login with 50 different user/password combinations":** The Data-Driven component handles this by storing the 50 credentials in a CSV or JSON file and looping them through one login script.
  * **"Reuse login steps across 20 test cases":** The Modular component (specifically Page Object Model) handles this by abstracting the login actions into a reusable `login()` function.
  * **"Support non-technical team members":** The Keyword-Driven (or BDD like Cucumber) component allows non-technical members to write tests using plain English keywords, which then trigger the underlying modular code.

---

## STEP 23: Hybrid Framework Folder Structure

To build this Hybrid framework for the Course Management frontend, the codebase should be organized to separate logic, data, and configuration:

```
course_automation_suite/
├── config/
│   └── (Contains environment setups like QA vs Prod URLs, browser configurations)
├── data/
│   └── (Contains external test data files like login_credentials.csv, course_test_data.json)
├── pages/
│   └── (Contains Page Object files; Modular part holding element locators and reusable actions)
├── utils/
│   └── (Contains helper functions like database connectors, custom wait functions, external file readers)
└── tests/
    └── (Contains actual executable test scripts like test_login.py, test_course_creation.py)
```

### Folder Responsibilities
* **`config/`:** Contains environment setups (e.g., QA vs Prod URLs, browser configurations).
* **`data/`:** Contains external test data files (e.g., `login_credentials.csv`, `course_test_data.json`).
* **`pages/`:** Contains Page Object files. This is the Modular part (e.g., `login_page.py`, `dashboard_page.py`) holding the element locators and reusable actions.
* **`utils/`:** Contains helper functions (e.g., database connectors, custom wait functions, external file readers).
* **`tests/`:** Contains the actual executable test scripts (e.g., `test_login.py`, `test_course_creation.py`) that pull from the `pages/` and `data/` folders.
