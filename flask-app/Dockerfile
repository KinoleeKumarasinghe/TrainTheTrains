# this is where we are going to put commands for docker to 
# know how to construct what docker calls an image 
# (a structure that will ultimately be a container)

# we need to tell Docker what our base image is going to be
FROM python:3.9-alpine
# this is an image that already exists on DockerHub

# need to set up our working directory
RUN mkdir /usr/src/app/
# mkdir is making a directory, or making  afolder

WORKDIR /usr/src/app/ 
# WORKDIR is the source of code where whenever you'll see 
# later we're going to actually have a command to start 
# an application and in the absence of providing a path 
# for the python file that the command is going to execute, 
# it would look in the working directory 
# - sort of is like the home for the application

# copy all of the code that's in the current working directory
# into the working directory that we want
COPY . /usr/src/app/

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

# expose the port that we're running on
EXPOSE 4000

# in order to have python to install the required libraries, like Flask
RUN pip install -r requirements.txt
# RUN command is executing some command inside the image
    # pip is essentially the python manager 

# run the application using python
CMD ["python", "app.py"]

# in terminal: 
# docker build -t (t is for the tag, what we want the image to be named) flask-imagee . 
# . represents telling Docker to look for a Dockerfile with a command in the current directory

# can go ahead and start the image by using the docker run command
# what -p does is a port mapping
# first number is host port - whatever number you put into your browser
# second number is whatever port you need to have access to in the container
# docker run -p 4000:4000 flask-image

# when we did this initially, the URL did not work because container does not know to connect with that url 

# so we add a line in app.py in the if __name__ == '__main__' command, so now it looks like this:
# if __name__ == '__main__':
#    app.run(debug = True, host = '0.0.0.0',port = 4000)

