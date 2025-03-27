from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv(override=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="あなたは優秀なAIアシスタントです。",
    markdown=True,
)
agent.print_response("こんにちは！", stream=True)
