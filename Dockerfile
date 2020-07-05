
FROM python:3.6

# Create app directory
WORKDIR /
COPY requirements.txt  . 
# Install app dependencies

RUN pip  install  -r requirements.txt

COPY ./ ./ 

EXPOSE 80
CMD [ "python", "server.py" ]
