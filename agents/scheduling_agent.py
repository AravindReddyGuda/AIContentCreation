import asyncio
import schedule
import time

from tasks.content_tasks import generate_content_for_topics
from crewai import Agent

class SchedulingAgent:
    """
    Agent responsible for scheduling content generation tasks at regular intervals.
    """
    def __init__(self, interval_minutes: int = 60):
        # Optional: define any special role for the scheduling agent if needed
        self.agent = Agent(
            role="Scheduler",
            goal="Automate content generation on a fixed schedule.",
            backstory="Ensures content is generated consistently over time."
        )
        self.interval_minutes = interval_minutes

    def job(self):
        """
        The job to run at each scheduled interval.
        """
        # Wrap in asyncio to ensure we can run async tasks.
        asyncio.run(generate_content_for_topics())

    def start(self):
        """
        Start the scheduling loop.
        """
        schedule.every(self.interval_minutes).minutes.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    # Run daily by default (1440 minutes = 24h)
    scheduler = SchedulingAgent(interval_minutes=1440)
    scheduler.start()
