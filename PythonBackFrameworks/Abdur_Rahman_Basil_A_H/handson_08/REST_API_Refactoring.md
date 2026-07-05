# REST API Refactoring Notes

This document describes the changes made during the refactoring of the course management API to align it with RESTful API design best practices. The project was refactored starting from the implementation in Hands-on 7.

## Modified Files
* database.py
* models.py
* schemas.py
* main.py

---

## Refactoring Breakdown

### 1. API Versioning
* **Before**: Endpoints were served under the `/api/` prefix directly, for example, `/api/courses/`.
* **After**: Endpoints are now served under the `/api/v1/` prefix, such as `/api/v1/courses/`.
* **Reason**: Introduces versioning to allow backward compatibility as the API evolves without breaking existing client integrations.
* **Code Snippet**:
```python
@app.post('/api/v1/courses/', response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
```

### 2. Semantic HTTP Methods (PUT vs PATCH)
* **Before**: The `PUT` endpoint was acting as a partial update, allowing clients to send only a subset of fields.
* **After**:
  * `PUT /api/v1/courses/{course_id}` replaces the entire course resource. All fields are required in the request payload.
  * `PATCH /api/v1/courses/{course_id}` is introduced for partial updates, allowing clients to modify only specific fields.
* **Reason**: Aligns with the HTTP protocol specification, where PUT represents full replacement and PATCH represents partial modifications.
* **Code Snippet**:
```python
# PUT (Full Replace)
@app.put('/api/v1/courses/{course_id}', response_model=CourseResponse)
async def replace_course(course_id: int, course_replace: CourseCreate, db: AsyncSession = Depends(get_db)):
    ...

# PATCH (Partial Update)
@app.patch('/api/v1/courses/{course_id}', response_model=CourseResponse)
async def update_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    ...
```

### 3. Response Status Codes and Location Headers
* **Before**: `POST` endpoints returned a `201 Created` status code but did not specify where the newly created resource could be accessed.
* **After**:
  * Added a `Location` header to the response on all successful resource creations (`POST` requests).
  * Ensured `DELETE` endpoints return `204 No Content` with an empty response body instead of returning a success message dictionary.
* **Reason**: Follows RFC guidelines for HTTP response headers. The `Location` header informs client applications where they can fetch the newly created resource.
* **Code Snippet**:
```python
@app.post('/api/v1/courses/', response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, response: Response, db: AsyncSession = Depends(get_db)):
    ...
    response.headers['Location'] = f'/api/v1/courses/{db_course.id}'
    return db_course
```

### 4. Pagination and Filtering
* **Before**: The course retrieval endpoint `GET /api/courses/` returned a raw list of courses with simple offsets.
* **After**:
  * Implemented offset-based pagination on `GET /api/v1/courses/` using query parameters `page` and `page_size`.
  * The response is now wrapped in a standardized envelope returning total count, next page link, previous page link, and the results list.
  * Added a case-insensitive `search` filter matching against the course name or code.
* **Reason**: Prevents server load when dealing with large datasets and provides the client application with clear links for navigability.
* **Code Snippet**:
```python
# Pagination envelope structure in schemas.py
class CoursePaginatedResponse(BaseModel):
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[CourseResponse]
```

### 5. Standardised Error Responses
* **Before**: Exception handlers returned varying structures for request validation and HTTP errors.
* **After**: Registered global exception handlers for `StarletteHTTPException` and `RequestValidationError` to return error payloads in a consistent format:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Error details",
    "field": "field_name_or_null"
  }
}
```
* **Reason**: Ensures clients can parse all errors using a single, uniform JSON schema.

---

## Assumptions Made
* The SQLite database file resides locally at `./courses.db` inside the hands-on directory.
* The confirmation email background task remains a simulated print statement on enrollment.
