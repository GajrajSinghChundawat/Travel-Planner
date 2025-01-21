# Travel-Planner
Trip Planner is a tool that creates custom travel itineraries based on your preferences. Whether you want adventure, relaxation, or culture, it suggests destinations and activities to help plan your perfect trip.

#Setup Instructions
1. Create a virtual environment to isolate your project's dependencies:
  a. Below mentioned virtual environment cmd for Windows(i), macOS{ii) and Linux(ii). 
      i. python -m venv venv
     ii. python3 -m venv venv

3. Activate the virtual environment to begin installing the required dependencies:
   a. Below mentioned activation cmd for Windows(i), macOS{ii) and Linux(ii).
      i. .\venv\Scripts\activate
     ii. source venv/bin/activate

5. Install the required dependencies by running:
   a. pip install -r requirements.txt
   
6. Create a .env file in the root directory of the project if it doesn't already exist.

7. Add the following lines to the .env file, replacing the placeholder values with your own credentials.
   MYSQL_DB_PASS=<your_mysql_database_password>
  MYSQL_DB_USER=<your_mysql_database_username>
  MYSQL_DB_HOST=<your_mysql_database_host>
  MYSQL_DB=<your_mysql_database_name>
  OPENAI_API_KEY=<your_openai_api_key>
  GPT_3_MODEL_NAME=gpt-3.5-turbo-0125

8. Finally, run the application using uvicorn:
   a. uvicorn main:app --reload 

