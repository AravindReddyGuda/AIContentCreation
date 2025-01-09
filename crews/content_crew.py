import asyncio
from crewai import Crew
from agents.content_agent import ContentAgent
from utils.nlp_utils import refine_content
from utils.file_utils import save_to_csv

class ContentCrew(Crew):
    """
    A Crew orchestrates multiple Agents and Tasks to produce collective results.
    """
    def __init__(self):
        super().__init__()
        self.content_agent = ContentAgent()
        self.agents = [self.content_agent.agent]  # Register Agents in the Crew if needed.

    async def run(self, topics):
        """
        Orchestrate content generation for multiple topics, refining and saving.
        """
        results = []
        for topic in topics:
            raw_content = await self.content_agent.generate_content(topic)
            refined = await refine_content(raw_content)
            save_to_csv(topic, refined)
            results.append(refined)
        return results
