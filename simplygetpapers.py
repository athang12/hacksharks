import requests
import pymongo 
import schedule
import time

#bas ata ha code 10 - 10 mintat challa pahije 

mongodb_url = "mongodb+srv://weekenddiscoveries6:V62ejRjlVilThUGv@cluster0.dhpp5yh.mongodb.net/"
database_name = "test"
collection_name = "collections"

client = pymongo.MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

names = []
interests = []
already = []

def getdata():
    user_interests = collection.find()
    for x in user_interests:
        names.append(x['name'])
        interests.append(x['interests'])
        already.append(x['already'])
    print("fetched")

     


# print(names)
# Set the API endpoint URL
url = "https://api.core.ac.uk/v3/search/works"

# Set your API key
api_key = "UYTah1GlzsxcNkVgEvoMbXQmZwF0rRu2"





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




# tms = len(interests)
# tm = 0

# def torun():


def process_user_interests():
    while(len(interests)>0):
        # interests = user.get("interests")
        # Construct the query for combined keywords
        combined_query = " AND ".join(interests[0]) 

        # Set the parameters for combined keyword search
        combined_params = {
            "apiKey": api_key,
            "query": combined_query,
            "page": 1,
            "pageSize": 50  # Fetch only 1 research paper
        }

        # Send the GET request for combined keyword search
        combined_response = requests.get(url, params=combined_params)

        # Check if the request was successful (status code 200)
        if combined_response.status_code == 200:
            combined_data = combined_response.json()
            # Extract the works from the combined keyword response
            combined_works = combined_data.get("results")

            # Process the combined keyword works
            # print("User:", user.get("username"))
            # print("Combined Keyword Results:")
            print(names)
            print(already)
            for work in combined_works:
                # Extract relevant information from the work
                title = work.get("title")
                authors = work.get("authors")
                abstract = work.get("abstract")
                doi = work.get("doi")

                # Print the information
                # print("Title:", title)
                # print("Authors:", authors)
                # print("Abstract:", abstract)
                # print("DOI:", doi)


                if (len(already[0])==0):
                    # Generate the research paper link
                    research_paper_link = generate_research_paper_link(title, authors)
                    if research_paper_link:
                        myquery = { "name": names[0] }
                        newvalues = { "$set": { "tosend": [
                            abstract,
                            title,
                            authors,
                            research_paper_link,
                        ] } }
                        collection.update_one(myquery, newvalues)
                        names.pop(0)
                        interests.pop(0)
                        already.pop(0)
                        break
            
                    else :
                        print("no paper")
                        break 
                elif  title not in already[0]:
                    research_paper_link = generate_research_paper_link(title, authors)
                    if research_paper_link:
                        myquery = { "name": names[0] }
                        newvalues = { "$set": { "tosend": [
                            abstract,
                            title,
                            authors,
                            research_paper_link,
                        ] } }
                        collection.update_one(myquery, newvalues)
                        names.pop(0)
                        interests.pop(0)
                        already.pop(0)
                        break
            
                    else :
                        print("no paper")
                        break       
                    
        else:
            # Print the error message if the request was unsuccessful
            print("Error:", combined_response.status_code, combined_response.text)

        print("updated")
        time.sleep(30)





# Schedule function1 to run every Monday at 9:00 AM
schedule.every().saturday.at("15:49").do(getdata)

# Schedule function2 to run every Wednesday at 2:30 PM
schedule.every().saturday.at("15:50").do(process_user_interests)

while True:
    schedule.run_pending()
    # if not schedule.jobs:  # Check if there are any scheduled jobs
    #     break  # Exit the loop if no more jobs are scheduled
    time.sleep(1)

# getdata()
# print(names)
# print(already)