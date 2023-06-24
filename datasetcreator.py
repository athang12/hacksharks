import numpy as np
import pandas as pd

# Generate synthetic data
np.random.seed(42)
num_users = 20000

interests = {
     'socail_science_and_humanities  :  ' : [
  "Psychology and Behavioral Sciences",
  "Cognitive Psychology",
  "Social Psychology",
  "Clinical Psychology",
  "Psychological Disorders",
  "Economics and Finance",
  "Behavioral Economics",
  "Macroeconomics",
  "Financial Markets",
  "Economic Policy",
  "International Trade",
  "Sociology and Anthropology",
  "Social Movements",
  "Cultural Anthropology",
  "Social Inequality",
  "Urban Sociology",
  "Gender Studies",
  "History and Cultural Studies",
  "World History",
  "Ancient Civilizations",
  "Art History",
  "Literary Studies",
  "Poetry and Poetics"
],

    'science_and_technology  :  ': [
  "Artificial Intelligence and Machine Learning",
  "Natural Language Processing",
  "Computer Vision",
  "Deep Learning",
  "Reinforcement Learning",
  "Robotics",
  "Data Science and Analytics",
  "Big Data Analysis",
  "Predictive Analytics",
  "Data Visualization",
  "Machine Learning Algorithms",
  "Data Mining",
  "Biotechnology and Genetics",
  "Gene Editing",
  "Genetic Engineering",
  "Biomedical Research",
  "Cloning",
  "Stem Cell Research",
  "Environmental Science and Sustainability",
  "Climate Change Mitigation"
],

    'health_and_medicine  :  ':[
  "Public Health and Epidemiology",
  "Disease Prevention",
  "Health Promotion",
  "Global Health",
  "Infectious Disease Control",
  "Biomedical Research and Pharmacology",
  "Drug Discovery and Development",
  "Molecular Biology",
  "Immunology",
  "Cancer Research",
  "Neuropharmacology",
  "Mental Health and Psychiatry",
  "Depression and Anxiety Disorders",
  "Addiction Studies",
  "Psychopharmacology",
  "Psychotherapy Approaches",
  "Mental Health Stigma",
  "Nutrition and Dietetics",
  "Obesity and Weight Management",
  "Nutritional Deficiencies",
  "Cardiology",
  "Diabetes Research",
  "Respiratory Medicine",
  "Orthopedics"
],

    'business_and_management  :  ':[
  "Marketing and Consumer Behavior",
  "Branding and Advertising",
  "Consumer Psychology",
  "Digital Marketing",
  "Market Research",
  "Entrepreneurship and Innovation",
  "Startup Ecosystems",
  "Business Model Innovation",
  "Technology Entrepreneurship",
  "Social Entrepreneurship",
  "Venture Capital and Funding",
  "Organizational Behavior and Leadership",
  "Team Dynamics",
  "Employee Motivation",
  "Leadership Styles",
  "Organizational Culture",
  "Change Management",
  "Finance and Accounting",
  "Corporate Finance",
  "Financial Risk Management",
  "Investment Analysis",
  "Supply Chain Management",
  "Operations Management",
  "Project Management",
  "Business Analytics"
],

   
}

data = pd.DataFrame(columns=['user_id', 'interest', 'rating'])  # Include 'rating' column

for user_id in range(num_users):
    user_interests = set()  # Use a set to store unique interests
    while len(user_interests) < 5:
        interest = np.random.choice(list(interests.keys()))
        sub_interest = np.random.choice(interests[interest])
        user_interests.add(f'{interest}_{sub_interest}')
    
    user_interests = list(user_interests)  # Convert set back to a list
    
    # Generate a random rating for the user
    rating = np.random.randint(1, 6)  # Random rating between 1 and 5
    
    print(f"User ID: {user_id}, Interests: {user_interests}, Rating: {rating}")  # Print user interests and rating
    
    user_data = pd.DataFrame({
        'user_id': [user_id],
        'interest': [', '.join(user_interests)],
        'rating': [rating]  # Add rating column
    })
    data = pd.concat([data, user_data], ignore_index=True)

# Save the synthetic dataset to a CSV file
data.to_csv('interest_data.csv', index=False)


