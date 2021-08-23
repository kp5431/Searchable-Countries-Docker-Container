# Searchable-Countries-Docker-Container
The purpose of this exercise was to gain an understanding of how a
project with multiple languages/technologies can be contained inside a docker image. It is not supposed to be a complete webapp.

Dockerhub link: [kadep/searchable-countries](https://hub.docker.com/r/kadep/searchable_countries "Dockerhub link")

## What's Inside:
* A React frontend that allows the user to search for countries and see information on them
* A python file that creates a db.json for the react frontend
* A bash script to facilitate running the project

## Why Docker?
To run this project from the source files, the user would need to install:
* python3
* pip
* the requests library for python
* npm
* create-react-app
* json-server
* axios

This process is troublesome and tedious. By putting the project into a docker container, the user only has to install docker, pull the image, and then run it.

## Usage:
1. Install docker and create an account
2. Open a terminal or command prompt
3. Run the commands:
    * docker pull kadep/searchable_countries:latest
    * docker run -d -p 3000:3000 -p 8001:3001 kadep/searchable_countries:latest
4. Open a web browser (preferably Chrome)
5. Use the address bar to navigate to localhost:3000

**-p 8001:3001 must be present in the run command as the react app looks for the database at localhost:8001**

The react app runs internally on port 3000, and json-server on port 3001. 

You should now see the react app. Type into the search box for countries, and click the button to see more information. Note that the temperature and wind direction are randomly added by `main.py`.

If you want to view all of the country data, navigate to `localhost:8001/countries`

## React App:

![Screenshot of react app](demo.PNG?raw=true "Screenshot of React App")

