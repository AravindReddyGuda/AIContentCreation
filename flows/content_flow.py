import asyncio
from crews.content_crew import ContentCrew

async def execute_content_flow():
    """
    This flow demonstrates how to orchestrate a Crew for content generation.
    """
    topics = ["Nutrition", "Better daily habits", "Billionaire Mindset"]
    crew = ContentCrew()
    contents = await crew.run(topics)
    return contents  # If needed for further processing

if __name__ == "__main__":
    asyncio.run(execute_content_flow())
