import asyncio
from flows.content_flow import execute_content_flow

if __name__ == "__main__":
    # Run the main content flow manually.
    asyncio.run(execute_content_flow())
