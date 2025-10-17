REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question and must be in ITALIAN and formatted according to format_instructions: {format_instructions}

Important instructions:
- Always try to find an answer, even if it is partial or approximate.
- If you are unable to find a definitive answer, explain clearly why.
- Include in the ReAct output anything similar or related that you could find.
- Evaluate carefully which tool to use and answer the question logically.
- Think step-by-step with interleaving THOUGHT, ACTION, and OBSERVATION.
- Stop only if you have a correct answer or if you conclude after reasoning that the question is unanswerable, explaining why.

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""
