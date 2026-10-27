import os
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

class State(TypedDict):
    messages : Annotated[list, add_messages]
    summary : str
    missing_fields : list
    patientId : str
    intent : str
    preceding_team : str
    reviewId : str
    review_status : str
    question : str
    user_decision: str

load_dotenv(override=True)
llm = ChatOllama(model=os.environ["MODEL_LLAMA"])