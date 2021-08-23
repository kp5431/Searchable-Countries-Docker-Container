#!/bin/bash
#create a file to see the command line output
touch output.txt

#run the python file to create the db,json
python3 main.py 2>&1 | tee output.txt

#start the json-server (use & to run in the background)
cd react
touch output2.txt
npx json-server -p 3001 --watch db.json --host 0.0.0.0 2>&1 | tee output2.txt &

#start the react app
npm start