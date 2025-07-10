from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain_community.tools import Tool

from image_gen import generate_image
from unity_gen import generate_unity_script
from website_gen import generate_website

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(
        name="ImageGen",
        func=generate_image,
        description="Generate an image from text"
    ),
    Tool(
        name="UnityGen",
        func=generate_unity_script,
        description="Create Unity C# script for Beat Saber"
    ),
    Tool(
        name="SiteGen",
        func=lambda text: generate_website("My Site", text),
        description="Make a simple HTML website"
    ),
]

agent = initialize_agent(tools=tools, llm=llm, agent_type="zero-shot-react-description")

def handle_prompt(prompt):
    return agent.run(prompt)
