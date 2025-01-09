import asyncio
from crewai import Task
from agents.content_agent import ContentAgent
from utils.file_utils import save_to_csv
from utils.nlp_utils import refine_content

async def generate_content_for_topics():
    """
    High-level function that orchestrates generating content for topics 
    and saves them into a CSV file.
    """
    # You can adjust your topics here or make it dynamic
    topics = ["Nutrition", "Better daily habits", "Billionaire Mindset"]

    content_agent = ContentAgent()

    # Define a CrewAI Task for generating refined content for each topic.
    # We'll do it in a single loop rather than multiple Task objects for brevity,
    # but you can create multiple if you prefer.
    content_generation_task = Task(
        description="""
            Generate a piece of content for each topic and refine it to be 
            friendly for non-native English speakers.
        """,
        expected_output="""
            For each topic, one refined piece of text that is clear, easy to understand, 
            and engaging. 
        """,
        agent=content_agent.agent  # The underlying Agent object from our ContentAgent wrapper
    )

    # Collect tasks (futures) to be executed asynchronously
    tasks = []
    for topic in topics:
        # We define what each async call will do
        async def generate_and_refine(topic=topic):
            raw_content = await content_agent.generate_content(topic)
            refined = await refine_content(raw_content)
            save_to_csv(topic, refined)
        tasks.append(generate_and_refine(topic))

    # Run them concurrently
    await asyncio.gather(*tasks)
