# User Authentication API
Deployed at [https://user-auth-api-django.herokuapp.com/](https://user-auth-api-django.herokuapp.com/)

### [POST] /registration/ :  Creates new User
This endpoint accepts details like name, username, password, email, phone_number, is_staff, is_active.



#### Parameters
###### Object *required     
Example Model -
                
                {
                  "name": "string",
                  "username": "string",
                  "password": "string",
                  "phone_number": "string",
                  "email": "user@domain.com",
                  "is_staff": "false",
                  "is_active": "true"
                }
                
Example:
[POST] : https://user-auth-api-django.herokuapp.com/user/register/
```
            {
              "email": "sush@gmail.com",
              "username": "sush",
              "name": "Sushmita",
              "password": "password@123"
            }
```

#### Responses
###### Code
201
###### Description
&nbsp;
```
{
    "message": "The user has been successfully created."
}
```
###### Code
400
###### Description
&nbsp;
```
{
    "name": [
        "This field is required."
    ]
}
```
```
{
    "username": [
        "This field is required."
    ]
}
```
```
{
    "email": [
        "This field is required."
    ]
}
```
```
{
    "password": [
        "This field is required."
    ]
}
```

```
{
    "password": [
        "Ensure this field has at least 8 characters."
    ]
}
```

```
{
    "phone_number": [
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    ]
}
```


### [POST] /login/ : Login User
The user can login with email + password.  
The token is valid for 60 days.
#### Parameters
###### Object *required     
Example Model -
                
                {
                  "email": "user@domain.com",
                  "password": "string",
                }

Example:
[POST] : https://user-auth-api-django.herokuapp.com/user/login/
```
            {
              "email": "sush@gmail.com",
              "password": "password@123"
            }
```

#### Responses
###### Code
200
###### Description
&nbsp;
```
{
    "name": "string",
    "username": "string",
    "phone_number": "string",
    "token": "string"
}
```
###### Code
400
###### Description
&nbsp;

```
{
    "password": [
        "This field is required."
    ]
}
```
```
{
    "email": [
        "This field is required."
    ]
}
```
```
{
    "email": [
        "user with this email already exists."
    ]
}
```
```
{
    "username": [
        "user with this username already exists."
    ]
}
```

```
{
    "password": [
        "Ensure this field has at least 8 characters."
    ]
}
```
```
{
    "non_field_errors": [
        "A user with this email and password was not found."
    ]
}
```
