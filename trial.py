from apscheduler.schedulers.blocking import BlockingScheduler
import time
from datetime import datetime

def my_job():
    print("Running my job...")




import schedule
import time

import requests
import pymongo
# import datetime
import time
import math

# Set the API endpoint URL
url = "https://api.core.ac.uk/v3/search/works"

# Set your API key
api_key = "UYTah1GlzsxcNkVgEvoMbXQmZwF0rRu2"

# MongoDB connection settings
mongodb_url = "mongodb+srv://weekenddiscoveries6:V62ejRjlVilThUGv@cluster0.dhpp5yh.mongodb.net/"
database_name = "test"
collection_name = "collections"

# Function to generate the research paper link
def generate_research_paper_link(title, authors):
    # Search the full research paper link using Serp Api for Google Scholar
    search_query = f"{title} {authors}"
    search_params = {
        "api_key": "2b84a5e797f705a6bbc79dd7255b01e1c17b81a8f581e2802bc6ded59fa4b9fb",
        "engine": "google_scholar",
        "q": search_query,
        "num": 1
    }
    search_url = "https://serpapi.com/search?engine=google_scholar"
    search_response = requests.get(search_url, params=search_params)

    # Check if the search request was successful (status code 200)
    if search_response.status_code == 200:
        search_data = search_response.json()
        # Extract the first search result
        search_result = search_data.get("organic_results")[0]
        # Extract the link to the full research paper
        research_paper_link = search_result.get("link")
        return research_paper_link
    else:
        # Print the error message if the search request was unsuccessful
        print("Search Error:", search_response.status_code, search_response.text)
        return None

# Connect to MongoDB
client = pymongo.MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

# Function to process user interests and generate links
def process_user_interests(user_interests):
    for user in user_interests:
        interests = user.get("interests")
        # Construct the query for combined keywords
        combined_query = " AND ".join([f"keyword:{interest}" for interest in interests])

        # Set the parameters for combined keyword search
        combined_params = {
            "apiKey": api_key,
            "query": combined_query,
            "page": 1,
            "pageSize": 1  # Fetch only 1 research paper
        }

        # Send the GET request for combined keyword search
        combined_response = requests.get(url, params=combined_params)

        # Check if the request was successful (status code 200)
        if combined_response.status_code == 200:
            combined_data = combined_response.json()
            # Extract the works from the combined keyword response
            combined_works = combined_data.get("results")

            # Process the combined keyword works
            print("User:", user.get("username"))
            print("Combined Keyword Results:")
            for work in combined_works:
                # Extract relevant information from the work
                title = work.get("title")
                authors = work.get("authors")
                abstract = work.get("abstract")
                doi = work.get("doi")

                # Print the information
                print("Title:", title)
                print("Authors:", authors)
                print("Abstract:", abstract)
                print("DOI:", doi)

                # Generate the research paper link
                research_paper_link = generate_research_paper_link(title, authors)
                if research_paper_link:
                    print("Research Paper Link:", research_paper_link)

                print()

        else:
            # Print the error message if the request was unsuccessful
            print("Error:", combined_response.status_code, combined_response.text)



# Function to fetch user interests from MongoDB
interests = []
def fetch_user_interests():
    user_interests = collection.find()
    for x in user_interests:
        interests.append(
            {
                "name":x['name'],
                "interests":x['interests']
            }
        )

    # print(interests)
    # total_users = user_interests.count()
    # execution_time = total_users * 10 * 60  # Total execution time in seconds

    # current_time = datetime.datetime.now()
    # start_time = current_time - datetime.timedelta(seconds=execution_time)

    # if current_time >= start_time:
    #     elapsed_time = (current_time - start_time).total_seconds()
    #     user_index = math.floor(elapsed_time / 600)  # 10 minutes = 600 seconds

    #     if user_index < total_users:
    #         user_interests.skip(user_index)
    #         process_user_interests(user_interests.limit(1))









# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the job to run every Monday at 8:00 AM
dy='fri'
hr=16
minu=25
scheduler.add_job(fetch_user_interests, 'cron', day_of_week=dy, hour=hr, minute=minu)

# Start the scheduler
while True:
    now = datetime.now()
    if now.hour >= hr or now.minute >= minu:
        fetch_user_interests()
    time.sleep(10)  # Sleep for 60 seconds before checking again