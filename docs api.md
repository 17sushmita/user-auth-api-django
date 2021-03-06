### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[POST] /registration/ :  Creates new User
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This endpoint accepts details like name, username, password, email, phone_number, is_staff,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_active.
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters
###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Object *required     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Example Model -
                
                {
                  "name": "string",
                  "username": "string",
                  "password": "string",
                  "phone_number": "string",
                  "email": "user@domain.com",
                  "is_staff": "false",
                  "is_active": "true"
                }
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Responses
###### Code
201
###### Description
&nbsp;
                {
                    "message": "The user has been successfully created."
                }
###### Code
201
###### Description
&nbsp;
                {
                    "message": "The user has been successfully created."
                }
###### Code
400
###### Description
&nbsp;
                {
    "name": [
        "This field is required."
    ]
},
{
    "username": [
        "This field is required."
    ],
    "password": [
        "Ensure this field has at least 8 characters."
    ],
    "phone_number": [
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    ]
{
    "email": [
        "This field is required."
    ],
    "password": [
        "This field is required."
    ]
}


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[POST] /login/ : Login User
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The user can login with (username or email) + password.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The token is valid for 60 days.
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters
###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Object *required     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Example Model -
                
                {
                  "email": "user@domain.com",
                  "password": "string",
                }




{
    "password": [
        "Ensure this field has at least 8 characters."
    ]
}
{
    "password": [
        "This field is required."
    ]
}
{
    "email": [
        "This field is required."
    ],
{
    "non_field_errors": [
        "A user with this email and password was not found."
    ]
}