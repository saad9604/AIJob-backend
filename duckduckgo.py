from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults


from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch


def generate_three_queries(query):
    client = genai.Client(api_key="AIzaSyCrdRrPmaguwcjvCbzwcMFbBHOV7F0B4Ss")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works in a few words",
        config=GenerateContentConfig(
             
            system_instruction=(
                f"Given the input query: {query}, generate three different search queries for DuckDuckGo. "
                "Return only a valid Python list of three strings, e.g. ['query1', 'query2', 'query3']. "
                "Do not include any explanation or extra text."
            )
        )
    )
    print(response.text)

    return response.text


def format_duckduckgo_response(query_results):
    client = genai.Client(api_key="AIzaSyCrdRrPmaguwcjvCbzwcMFbBHOV7F0B4Ss")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Given the following search results: {query_results}\n\n",
        config=GenerateContentConfig(
            system_instruction=(
                "You are an expert job search assistant. "
                "Sort the job search results so that links to direct job application pages or official open positions are at the top. "
                "Links that redirect to job aggregators, review sites, or do not lead directly to a job application (such as Turing, Glassdoor, or general listings) should be placed at the end. "
                "Return the sorted results as a JSON array, where each object has the following fields: "
                "\"job description\", \"company\", and \"salary range\". "
                "For each job, extract and fill these fields as accurately as possible from the search results. "
                "If any field is missing, leave it as an empty string. "
                "Do not add any extra commentary or explanation. "
                "Example output:\n"
                "[{\"job description\": \"xxx\", \"company\": \"xxx\", \"salary range\": \"xxx\",\"Location\": \"xxx\", \"Apply link\": \"xxx\"}]"
            )
        )
    )
    print(response.text)

    return response.text

def test_duckduckgo_search(query):
    print("Searching query....." , query)
    search = DuckDuckGoSearchResults(output_format="list")

    data = search.invoke(f"{query}")

    print(data)
    return data