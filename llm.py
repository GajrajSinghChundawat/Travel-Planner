from os import getenv
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from prompts import TP_ITINERARY_PROMPT

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
GPT_3_MODEL_NAME = getenv("GPT_3_MODEL_NAME")


def tp_llm(
        location,
        destination,
        description,
        details,
        metadata
):
    llm = ChatOpenAI(model=GPT_3_MODEL_NAME)

    prompt = TP_ITINERARY_PROMPT.partial(
        destination=destination,
        description=description,
        details=details,
        metadata=metadata
    )

    generate_itinerary_response = (prompt | llm).invoke(
        location
    )

    return generate_itinerary_response.content
