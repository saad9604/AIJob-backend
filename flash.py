from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCrdRrPmaguwcjvCbzwcMFbBHOV7F0B4Ss")

response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents="looking for python developer jobs in Pune 8LPA",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a job search assistant specialized in finding live job openings. "
            "Your primary task is to search for job opportunities across various domains, "
            "summarize the results in a clear and concise manner, and provide actionable insights. "
            "Focus on delivering accurate, up-to-date job listings and highlight key details such as "
            "job title, company name, location, salary range, and application links."
        ),
        tools=[types.Tool(
            google_search_retrieval=types.GoogleSearchRetrieval()
        )]
    )
)
print(response)