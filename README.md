# Casting-Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies

# Motivation
The motivation of this project is to create a webapp where small companies can assign actors to movies as well as expand on my knowledge of postgres & SQLAlchemy, API endpoints, unit testing, authorization and role based access, and deployment.

# How to use
To run the program, simply navigate to ____ where you can access all the API endpoints


JWT tokens are listed here, while other important variables can be found in models.py or config.py :

bearer_tokens = {
  
  "casting_assistant": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3V1BsZ2dGVXVXemF2OVpCNGl0eCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQxMjM0NS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBkNzhlNDVmMzVlNDIwMDcxOWMxNWY5IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwLyIsImlhdCI6MTYyNDc2Mjc2NCwiZXhwIjoxNjI0ODQ5MTY0LCJhenAiOiJoMFpnNWNoQXR4OWowWE84VmFpQmh1eGVnYmJkWEM3WiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.XwKJgg8Ew-u8S5aYKzGn0zOu0opyFQrKK6Sdp_1IbBfQLOTEgsQErHVSDUGkHFj5nWdYWOcNAoOajgQexbYLhTK_idSDP-sOFNLfCvA6J19a5uaifHQBOzdCRe-GZ7seZVFJQRfGY242fLOlg05Vx8-TwmXr8dR3C1V9VwF0Nx7DaaKNRybTV1U9B9W8g0fr8694Jh2F-69JSwrWMzKFDQJfrE2_i2tY-P3fN-T-U1S5tkuL5bFZNCeq-rSJYujGNGGm-SszJPzf8f615tjV09wAnN7pG2QFKpdwJayTwRctXlnC8pVVKSQ2N82ocsMFjUVf0dJLGYLAynU5v9zacQ",
  
  "executive_producer": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3V1BsZ2dGVXVXemF2OVpCNGl0eCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQxMjM0NS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBjNGY3Nzc2MTJkODIwMDcwYTVlNjFjIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwLyIsImlhdCI6MTYyNDc2MzEwMSwiZXhwIjoxNjI0ODQ5NTAxLCJhenAiOiJoMFpnNWNoQXR4OWowWE84VmFpQmh1eGVnYmJkWEM3WiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.ZvwOfquW-fa6GCtcEyno9JX4vO8hQcML_9g1uvHk87AtmR5XW78MT2v_7F1aqGb3VCGkXQhB6Wmolm0cnk0ySyIbfb5h9bftfr7eGz_9CCfCtY0JsKRRVZSuthMcTjNrba0Yc1EE0lfq5q9vpIQXrKLflhqOrFQUEmR54kVs9QWCPsmb_USPYwDyXP0xb-im90XIumWO7eZuwM1ul4p8r7LhFZjR9FCGBKHqgnX8ecchu0v3gZhHg9oqYwLPczvHtVmBOczXuOdxJObQ3s2Z8Q-gWu6kWOZ_eHqxrWrxOE99sy4FcqwRu624KK83jgUje6xTRQhixwAacZWY_p2kPg",
  
  "casting_director": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3V1BsZ2dGVXVXemF2OVpCNGl0eCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQxMjM0NS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBkNzhkZmYzODUxZDMwMDY5MmViOTQ5IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwLyIsImlhdCI6MTYyNDc2Mjk3NywiZXhwIjoxNjI0ODQ5Mzc3LCJhenAiOiJoMFpnNWNoQXR4OWowWE84VmFpQmh1eGVnYmJkWEM3WiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciJdfQ.cRBzv-v6-383rk0sLFY0_Est8JqKeG_VWrIdcUg7SAXv_A3aRtIAsI7tcNa48Lq5fyc5MViIrVGvVUFs4oTeYhIo8HS5iRBzUmFHS7Bpye45OtHAfpbPuL5kRy7W4DrqzlbbFRwg3bGAHVkf3wZVykL7bTKQSs6sY_rFeP6UtPEorZkRQrZgUl3pDrVW7LvmQxrPAFLcrPbQY17XFzLWISy_R9ctMoOvdHfhUaRblysYI4wlQ85bUUHrd9gyTqL_cJGNDvtYR8SaCBIUmY1NHPHYxyAU7R9OYLisnOTi94X8eQH-EUXRKlqk-wEJ8PixjHOedBjBapyO2Wroo3ZEAg"
}

# How to run test cases
To run the 16 different test cases to verify that the program is running correctly, cd to the project directory and type "python test_app"

# Roles and Permissions

There are three different roles which all have varying permissions: 

Casting assistant : Can view actors and movies
Casting director : Can view actors and movies, edit actors and movies, and add/delete actor
Executive producer : Can view actors and movies, edit actors and movies, add movies and actors, remove movies and actors

# API Documentation

## Endpoints

There are several different functionalities, mainly view actors/movies, add actors/movies, edit actors/movies, and delete actors/movies

### /actors

This will display a paginated list of the actors with details such as name, age, and gender

### /movies

This will display a paginated list of the movies with details such as release and title

### delete /movies/<movie_id>

This will delete movie with the id specified by the user

### delete /actors/<actor_id>

This will delete actor with the id specified by the user

### post /actors

This will create an actor with a name, gender, and age in the database

### post /movies

This will create a movie with a release date and a title in the database

### patch /actors/<actor_id>

This will edit a actor with id specified by user in the database

### patch /movies/<movie_id>

This will edit a movie with id specified by the user in the database