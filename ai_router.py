from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from image_gen import generate_image
from unity_gen import generate_unity_script
from website_gen import generate_website

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(name="ImageGen", func=generate_image, description="Generate an image."),
    Tool(name="UnityGen", func=generate_unity_script, description="Unity script generator."),
    Tool(name="SiteGen", func=lambda text: generate_website("My Site", text), description="Website creator.")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

def handle_prompt(prompt):
    return agent.run(prompt)
