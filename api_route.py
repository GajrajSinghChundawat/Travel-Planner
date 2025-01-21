from fastapi import APIRouter
from api_service import (
    create_travel_planner_vector,
    generate_travel_planner_itinerary
)

travel_planner_router = APIRouter()


@travel_planner_router.get("/travel-planner-vector")
def get_travel_planner_vector():
    return create_travel_planner_vector()


@travel_planner_router.post("/generate-travel-itinerary")
def generate_travel_itinerary(
    location: str
):
    return generate_travel_planner_itinerary(location)
