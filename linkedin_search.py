from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse
import os

load_dotenv()

tools = [TavilySearch(max_results=15)]
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# ottimizzo output 
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
format_instructions = output_parser.get_format_instructions()

# Recupero del prompt ReAct
# react_prompt = hub.pull("hwchase17/react")
react_prompt_with_instruction_ita = PromptTemplate(template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
                                input_variables=["input", "agent_scratchpad", "tool_names"],
                                partial_variables={"format_instructions": format_instructions}
                                )
# Agente React
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_instruction_ita)

#Agent Executor
agent_executor = AgentExecutor(agent=agent,
                tools=tools,
                max_iterations=5,
                verbose=True,
                handle_parsing_errors=True)


def main():
    result = agent_executor.invoke(
        input = {
            "input": "Cerca più di 5 offerte di lavoro che richiedano competenze almeno in uno tra LangChain e LangGraph. Vorrei che il tipo di lavoro fosse con sede a Milano basta che sia AI Agent magari Junior"
        }
    )

    saveresponse = result
    
    print("\n=== RISULTATO ===\n")
    print(result["output"])

if __name__ == "__main__":
    main()