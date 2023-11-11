# Jokes-API Web-Application

## Description ##
Jokes_API is a web application written in Python that sends a random joke with every HTTP GET call,<br> 
The application also returns the id of the punchline that was received

## Specification ##

The Application is written in Python using FastAPI package

| Package  | Version |
| ------------- | ------------- |
| fastapi  | 0.104.1  |

## How to use  ##

1. Clone the code into your local server using this command:
```
git clone https://github.com/MaorYahalomi/Jokes_API.git
```
2. change to the cloned repo folder:
```
cd Jokes_API
```
3. Install FastApi package using pip:
```
pip3 install fastapi
```
4. Run the app using the command with your desired port (8877 for example):
```
uvicorn main:app --host 0.0.0.0 --port 8800  --reload
```
5. Access the web application using curl or browser using this url (replace x.x.x.x with your public IP):
```
http://x.x.x.x:8800
```

Example of the output:

![joke](https://github.com/MaorYahalomi/maven-project/assets/30255797/6e566de8-f2d7-40c9-9595-0e40a45cbd61)
