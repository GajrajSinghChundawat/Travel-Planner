<h1>Travel-Planner</h1>

<p>Trip Planner is a tool that creates custom travel itineraries based on your preferences. Whether you want adventure, relaxation, or culture, it suggests destinations and activities to help plan your perfect trip.</p>

<h2>Setup Instructions</h2>

1. Create a virtual environment to isolate your project's dependencies:</br>
   a. Below mentioned virtual environment cmd for Windows(i), macOS{ii) and Linux(ii).</br>
      i. <code>python -m venv venv</code></br>
      ii. <code>python3 -m venv venv</code></br>

2. Activate the virtual environment to begin installing the required dependencies:</br>
   a. Below mentioned activation cmd for Windows(i), macOS{ii) and Linux(ii).</br>
      i. <code>.\venv\Scripts\activate</code></br>
      ii. <code>source venv/bin/activate</code></br>

3. Install the required dependencies by running:</br>
   i. <code>pip install -r requirements.txt</code>

4. Create a .env file in the root directory of the project if it doesn't already exist.

5. Add the following lines to the .env file, replacing the placeholder values with your own credentials.

   <code>MYSQL_DB_PASS=<your_mysql_database_password></code></br>
   <code>MYSQL_DB_USER=<your_mysql_database_username></code></br>
   <code>MYSQL_DB_HOST=<your_mysql_database_host></code></br>
   <code>MYSQL_DB=<your_mysql_database_name></code></br>
   <code>OPENAI_API_KEY=<your_openai_api_key></code></br>
   <code>GPT_3_MODEL_NAME=gpt-3.5-turbo-0125</code></br>

6. Finally, run the application using uvicorn:
   a. uvicorn main:app --reload
