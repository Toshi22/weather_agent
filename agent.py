from langchain_classic.agents import AgentType, initialize_agent
from langchain_classic.chat_models import ChatOpenAI
from tools import get_weather
from dotenv import load_dotenv

load_dotenv()


# 2. Setup the Tool 
tools = [get_weather]

# 3. Initialize LLM
llm = ChatOpenAI(temperature=0,model="gpt-4o-mini")

# 4. Initialize Agent (Classic) using ReAct-style agent to avoid callbacks bug
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

