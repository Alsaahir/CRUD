# Django REST API for Managing Persons

## API Documentation

This is a simple Django REST API for managing person records. It supports basic CRUD (Create, Read, Update, Delete) operations for the "Person" resource.

# Setup and Installation

1. Clone the repository `https://github.com/Alsaahir/CRUD.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`


#### Create a Person (POST /api)

**Request Format:**

```json
{
    "name": "John Doe",
    "email": "johndoe@email.com"
}
```

**Response format:**
```json
{
    "message": "Person created successfully",
    "person_id": "2297fccd-4141-4123-8b4f-f9f2ff9aaec4"
}
```

**IF USER WITH THE SAME EMAIL EXISTS**

**Response format:**
```json
{
    "message": "Person already exists",
    "person_id": "2297fccd-4141-4123-8b4f-f9f2ff9aaec4"
}
```

**Get Person Details (GET /api/UUID)**
***Response Format:***

```json
{
    "id": "2297fccd-4141-4123-8b4f-f9f2ff9aaec4",
    "name": "John Doe",
    "email": "johndoe@email.com"
}
```

**Update Person Details (PUT /api/UUID)**
***Request Format:***

```json
{
    "name": "Updated Name",
    "email": "updated@email.com"
}
```

***Response Format:***
```json
{
    "message": "Person updated successfully"
}
```

**Delete Person (DELETE /api/UUID)**
***Response Format:***

```json
{
    "message": "Person deleted successfully"
}
```

# SAMPLE USAGE

**CREATE PERSON (POST /api)**

***Example Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "name": "John Doe",
    "email": "johndoe@email.com"
}' http://127.0.0.1:8000/api
```

***Example Response***
```json
{
    "message": "Person created successfully",
    "person_id": "2297fccd-4141-4123-8b4f-f9f2ff9aaec4"
}
```

**Get person information (Get /api/2297fccd-4141-4123-8b4f-f9f2ff9aaec4)**

***Example Response***
```json
{
    "id": "2297fccd-4141-4123-8b4f-f9f2ff9aaec4",
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

**Update Person Details (PUT /api/2297fccd-4141-4123-8b4f-f9f2ff9aaec4)**

***Example Request***

```bash
curl -X PUT -H "Content-Type: application/json" -d '{
    "name": "Updated Name",
    "email": "updated@example.com"
}' http://127.0.0.1:8000/api/2297fccd-4141-4123-8b4f-f9f2ff9aaec4
```

***Example Response***

```json
{
    "message": "Person updated successfully"
}
```

**Delete Person (DELETE /api/2297fccd-4141-4123-8b4f-f9f2ff9aaec4)**

***Example Request***

```json
curl -X DELETE http://127.0.0.1:8000/api/2297fccd-4141-4123-8b4f-f9f2ff9aaec4
```

***Example Response***
```json
{
    "message": "Person deleted successfully"
}
```

# Known Assumptions and Limitations

* Assumption: The email field is optional, and if not provided, it defaults to an empty string.
* Limitation: The API will not return all person in the database but instead, the API will only return the details of the person whose id you provided. which means that, if you dont know the id of the user, you will not be able to see their details


Have fun!

