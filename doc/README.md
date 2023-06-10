# Flask Application API Documentation

## API Endpoint: Create a User

### Endpoint

`POST /api/users`

### Description

Creates a new user in the application.

### Request Headers

| Key           | Value            |
|---------------|------------------|
| Content-Type  | application/json |

### Request Body (JSON)

| Key      | Type   | Description                            |
|----------|--------|----------------------------------------|
| username | String | The username of the user to be created |
| email    | String | The email of the user to be created    |
| password | String | The password of the user to be created |

Example:

```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword"
}
```

## Curl Example

```shell
curl -X POST -H "Content-Type: application/json" \
-d '{"username":"testuser", "email":"testuser@example.com", "password":"testpassword"}' \
http://localhost:9000/api/users
```

