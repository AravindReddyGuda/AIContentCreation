import os
from crewai import Agent

class ContentAgent:
    """
    Agent responsible for generating engaging and simplified content on various topics.
    Utilizes CrewAI's Agent class to handle LLM calls and memory management.
    """
    def __init__(self):
        # Configure your LLM here (change function_calling_llm if you have a specific model).
        self.agent = Agent(
            role="Content Generator",
            goal="Generate engaging, easy-to-understand content on various topics.",
            backstory="An AI agent passionate about simplifying complex topics for broad audiences.",
            memory=True,
            respect_context_window=True,
            max_rpm=10,
            function_calling_llm="gpt-4"  # or "gpt-4o-mini", "gpt-3.5-turbo", etc.
        )

    async def generate_content(self, topic: str) -> str:
        """
        Asynchronously generates content for a given topic using the agent's LLM call.
        """
        # You could also create a custom prompt here if you prefer.
        prompt = f"Generate a concise, compelling article about the topic: {topic}"
        response = await self.agent.async_generate(prompt)
        return response
