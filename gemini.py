from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

def search_jobs_with_gemini(query):
    """
    Searches for job opportunities using the Gemini model based on the given query.

    Args:
        query (str): The job search query (e.g., "python developer jobs in Pune 8LPA").

    Returns:
        Tuple containing the text parts of the response and the grounding metadata.
    """
    client = genai.Client(api_key="AIzaSyCrdRrPmaguwcjvCbzwcMFbBHOV7F0B4Ss")
    model_id = "gemini-2.0-flash"

    google_search_tool = Tool(
        google_search=GoogleSearch()
    )

    response = client.models.generate_content(
        model=model_id,
        contents=query,
        config=GenerateContentConfig(
            system_instruction=(
                "You are a job search assistant specialized in finding live job openings. "
                "Your primary task is to search for job opportunities across various domains, "
                "summarize the results in a clear and concise manner, and provide actionable insights. "
                "Focus on delivering accurate, up-to-date job listings and highlight key details such as "
                "job title, company name, location, salary range, and application links. "
                "Ensure that you include direct links to the job postings for each position. "
                "Avoid discussing or including any unrelated topics; your sole focus should be on job postings."
            ),
            tools=[google_search_tool],
            response_modalities=["TEXT"],
        )
    )

    # Extract response text parts
    response_texts = [each.text for each in response.candidates[0].content.parts]

    # Extract grounding metadata
    grounding_metadata = response.candidates[0].grounding_metadata.search_entry_point.rendered_content
    print(grounding_metadata)
    return response_texts, grounding_metadata

# Example usage
if __name__ == "__main__":
    query = "looking for python developer jobs in Pune 8LPA"
    response_texts, grounding_metadata = search_jobs_with_gemini(query)

    # Print response texts
    for text in response_texts:
        print(text)

    # Print grounding metadata
    # print(grounding_metadata)