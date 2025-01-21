from json import dumps
from llm import tp_llm
from db import travel_planner
from api_common import tp_vector_create, tp_vector_similarity_search


def create_travel_planner_vector():
    try:
        travel_planner_conn = travel_planner.cursor()
        travel_planner_conn.execute("select id, details from travel_kb")
        tp_response = travel_planner_conn.fetchall()

        for data in tp_response:
            vector_response = tp_vector_create(data[1])
            serialized_vector = dumps(vector_response)
            update_tp_query = "UPDATE travel_kb SET desc_vectors = %s WHERE id = %s"
            travel_planner_conn.execute()
            update_tp_query, (
                serialized_vector, data[0]
            )
            travel_planner.commit()

        return f"Successfully Created Vector {travel_planner_conn.rowcount}"

    except Exception as e:
        return f"Error: {e}"

    finally:
        travel_planner_conn.close()


def generate_travel_planner_itinerary(location):
    try:
        tp_similar_response = tp_vector_similarity_search(
            location,
            travel_planner
        )
        kb_data = None
        for tp_kb in tp_similar_response:
            if tp_kb[-1] > .60:
                kb_data = tp_kb[0]

        if kb_data is not None:
            destination = kb_data[1]
            description = kb_data[2]
            details = kb_data[3]
            metadata = kb_data[4]
        else:
            destination = None
            description = None
            details = None
            metadata = None

        llm_response = tp_llm(
            location,
            destination,
            description,
            details,
            metadata
        )

        return llm_response 

    except Exception as e:
        return f"Error: {e}"
