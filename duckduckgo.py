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
        contents="Explain how AI works in a few words",
        config=GenerateContentConfig(
             
            system_instruction=(
        f"Given the input query: {query_results}, generate three different search queries for DuckDuckGo. "
        "Return the response as a JSON object in the following format: "
        "{ 'queries': ['query1', 'query2', 'query3'] }. "
        "Format the response to exclude any objects that contain unrelated links, such as blogs, news articles, or promotional content. "
        "Only include objects that have direct links to job postings, career pages, or recruitment platforms."
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