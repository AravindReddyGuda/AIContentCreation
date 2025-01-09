import asyncio
import os
from crewai import Agent

def refine_content(content: str) -> str:
    """
    Refine content by ensuring it is friendly and easy to understand 
    for non-native English speakers.
    """
    # This could be optimized by creating a single simplifier Agent at module-level,
    # but for clarity, we'll create it here.
    simplifier = Agent(
        role="Simplifier",
        goal="Rewrite content to be easily understood by non-native English speakers.",
        backstory="Specialized in language simplification and clarity.",
        memory=True,
        respect_context_window=True,
        max_rpm=10,
        function_calling_llm="gpt-3.5-turbo"  # Choose an appropriate model for cost/performance
    )

    async def simplify_content(text):
        prompt = (
            "Simplify the following content for a non-native English speaker:\n\n"
            f"{text}"
        )
        response = await simplifier.async_generate(prompt)
        return response.strip()

    return asyncio.run(simplify_content(content))
