# Project Management

List The Docs provides a set of REST APIs to manage the projects and the documentation versions.

The GET requests are not behind access control, while POST, PATCH and DELETE requests
require an API-Key to validate the user that make the request.

## Project

### Adding a Project

The following call will add a project:

``` http
POST /api/v1/projects HTTP/1.1
Content-Type: application/json
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png"
}
```

| Field       | Type  | Description |
|:-----------:|:-----:|:-----------:|
| name        | *str* | The name of the project |
| description | *str* | The description of the project. Custom HTML is allowed. |
| logo        | *str* | The Logo of the project (optional). |

The *logo* field is optional.

The response has the following format:

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png",
    "versions": []
}
```

### Reading a Project

The following call will read a project named *Project-Name*:

``` http
GET /api/v1/projects/Project-Name HTTP/1.1
```

If the project exists, the following response will returns:

``` http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png",
    "versions": []
}
```

If the project does not exists, a 404 response code will be returned.

### Reading all the Projects

The following call will read all the projects:

``` http
GET /api/v1/projects HTTP/1.1
```

The following response will returns:

``` http
HTTP/1.1 200 Ok
Content-Type: application/json

[
    {
        "name": "Project-Name-1",
        "description": "A not too long description of the project 1",
        "logo": "http://www.projectname1.com/logo.png",
        "versions": []
    },
    {
        "name": "Project-Name-2",
        "description": "A not too long description of the project 2",
        "logo": "http://www.projectname2.com/logo.png",
        "versions": []
    }
]
```

### Updating a Project

It is possible to update the *description* or the *logo* of a Project using the following
call:

``` http
PATCH /api/v1/projects/Project-Name HTTP/1.1
Content-Type: application/json
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da

{
    "description": "An optional new description",
    "logo": "http://www.projectname.com/an-optional-new-logo.png"
}
```

It is possible to update only the *logo* or only the *description*.

The response has the following format:

``` http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "An optional new description",
    "logo": "http://www.projectname.com/an-optional-new-logo.png",
    "versions": []
}
```

### Removing a Project

It is possible to remove a Project (and all its versions) using the following call:

``` http
DELETE /api/v1/projects/Project-Name HTTP/1.1
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da
```

The response has the following format:

``` http
HTTP/1.1 200 Ok
```

## Project Documentation Version

### Adding a new documentation Version to a Project

The following call will add a new documentation version to the *Project-Name*
project:

``` http
POST /api/v1/projects/Project-Name/versions HTTP/1.1
Content-Type: application/json
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da

{
    "name": "1.0.0",
    "url": "https://www.example.com/doc/1.0.0/"
}
```

| Field       | Type  | Description |
|:-----------:|:-----:|:-----------:|
| name        | *str* | The name of the docuemtation version (e.g. *1.0.0*). |
| url         | *str* | The url to the to the documentation files. |

The response has the following format:

``` http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png",
    "versions": [
        {
            "name": "1.0.0",
            "url": "https://www.example.com/doc/1.0.0/"
        }
    ]
}
```

Each Project can have multiple documentation versions.

### Updating a documentation Version

After adding a documentation version to a Project, it is possible to update
it (e.g. in case documentation has been moved to a different URL).

The *name* field can't be changed.

The following call will update the documentation URL:

``` http
PATCH /api/v1/projects/Project-Name/versions/1.0.0 HTTP/1.1
Content-Type: application/json
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da

{
    "url": "https://www.projectname.com/doc/1.0.0/"
}
```

The response has the following format:

``` http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png",
    "versions": [
        {
            "name": "1.0.0",
            "url": "https://www.projectname.com/doc/1.0.0/"
        }
    ]
}
```

### Removing a Version from a Project

It is possible to remove a Version from a Project using the following call:

``` http
DELETE /api/v1/projects/Project-Name/versions/1.0.0 HTTP/1.1
Api-Key: f9bf78b9a18ce6d46a0cd2b0b86df9da
```

The response has the following format:

``` http
HTTP/1.1 200 Ok
Content-Type: application/json

{
    "name": "Project-Name",
    "description": "A not too long description of the project",
    "logo": "http://www.projectname.com/logo.png",
    "versions": []
}
```