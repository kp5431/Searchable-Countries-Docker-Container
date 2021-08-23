#need node for create-react-app (general npm stuff)
FROM node:16-slim

#setup the working directory and copy everything into it
WORKDIR /app
COPY . .

#install required npm dependency
RUN npm install json-server --save-dev
RUN npm install axios

#install python3
RUN apt-get update 
RUN apt-get install python3 -y 
RUN apt-get install python3-pip -y 

#install required python lib
RUN pip3 install requests

CMD ["sh", "run.sh"]





