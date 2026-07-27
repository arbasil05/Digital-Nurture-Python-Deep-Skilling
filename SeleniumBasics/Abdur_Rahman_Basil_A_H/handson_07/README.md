# Selenium Hands-on 07

## POM Explanation

**Question:** What problem would occur in a flat (non-POM) script if the Submit button's ID changed from 'submit' to 'btn-submit'? How does POM solve this?

**Answer:** 
In a flat, non-POM (Page Object Model) script, locators like `driver.find_element(By.ID, 'submit')` are typically scattered directly inside the test methods. If the Submit button's ID changes to 'btn-submit', every single test that interacts with the Submit button will fail. A QA engineer would need to manually find and update the hardcoded ID in all those test files, which makes maintenance tedious and error-prone.

POM solves this by centralizing all locators into a single Page Class. For instance, in `InputFormPage`, the Submit button locator is defined once as a class-level variable: `SUBMIT_BUTTON = (By.ID, 'submit')`. If the ID changes, we only need to update it in one place (the Page Class). All test files that call `page.submit_form()` will automatically use the updated locator, eliminating widespread script breakages and drastically reducing maintenance effort.
