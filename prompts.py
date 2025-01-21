from langchain.prompts import ChatPromptTemplate


TP_ITINERARY_TEMPLATE = """Your task is create trip itinerary.

-LOCATION: {location}
-DESTINATION: {destination}
-DESCRIPTION: {description}
-DETAILS: {details}
-METADATA: {metadata}

-GUIDELINES:
1. If DESTINATION is not proivded then create 5 day itinerary for LOCATION.
2. If DESTINATION is proivded create 5 day trip itinerary for DESTINATION using DESCRIPTION, DETAILS, METADATA.
"""

TP_ITINERARY_PROMPT = ChatPromptTemplate.from_template(TP_ITINERARY_TEMPLATE)
