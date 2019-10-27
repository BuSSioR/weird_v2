# Project Title

Weird Text API - Recruitment task

## Getting Started


### Prerequisites

In order to run project locally, you have to create a virtual environment (or not, I'm not the one to judge) and install all requirements from requirements.txt.
### Running project locally

To run the project locally, navigate to a project directory and run 

```
python3 manage.py run 
```

in terminal.

The project should be available on 127.0.0.1:8000
### Running the tests

To run automated tests just run 
```
python3 manage.py test
```
In order to check test coverage run
```
python3 manage.py cov
```
Test reports are generated if needed.
### 3rd party libraries

To develop this app I have used flask with flask_testing package. The app is served by gunicorn, tests coverage can be checked thanks to coverage package. To allow cross-origin requests, flask_corse has been used.

## Endpoints

### v1/encode

Accepts POST requests. Example body:
```
{
    "sentence":"Hello world!"
}
```
String under sentence key will be encoded and returned as response. 
Example response body:
```
{
    "encoded":"Hlelo wrlod!"
}
```

### v1/decode_without_list
Reverses the encoding algorithm that is used by this app. Does not require a list of orginal words. Accepts POST requests.
Example body:
```
{
    "sentence":"Hlelo wrlod!"
}
```
Returns decoded sentence as output:
```
{
    "decoded":"Hello world!"
}
```
This one works only with sentences encoded by this App!!! 


### v1/decode
Decodes any sentence if original words list provided.  Accepts POST requests. 
Example body:
```
{
    "sentence":"Hlelo wrlod!",
    "decode_list": ["Hello","world"]
}
```
Returns decoded sentence as result:
```
{
    "decoded":"Hello world!"
}
```
## Deployment

Deployment is fully automated. CircleCi is used to provide continuous integration. It runs tests and autopep8, and also deploys app to heroku if tests pass.
APP_SETTINGS and SECRET_KEY env variables should be set up. Config file provides production, development and testing config. SECRET_KEY is up to you. These env variables shoud be added on heroku and on circleci projects.
Moreover CircleCi project should have your heroku API key and app name set up as env variables for deployment purposes. 
