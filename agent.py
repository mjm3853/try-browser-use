from langchain_anthropic import ChatAnthropic
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()



async def main():
    # Initialize the model
    llm = ChatAnthropic(
        model_name="claude-3-5-sonnet-20240620",
        temperature=0.0,
        timeout=100, # Increase for complex tasks
    )

    # Create agent with the model
    agent = Agent(
        task="Tell me what tee times are available at lake of isles golf club at Foxwoods",
        llm=llm
    )
    await agent.run()

asyncio.run(main())