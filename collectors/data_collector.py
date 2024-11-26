from mesa.datacollection import DataCollector

def create_data_collector():
    """
    Create a DataCollector for the model.
    """
    return DataCollector(
        model_reporters={
            "Healthy": lambda m: sum([1 for a in m.schedule.agents if a.health_status == "healthy"]),
            "Infected": lambda m: sum([1 for a in m.schedule.agents if a.health_status == "infected"]),
            "Recovered": lambda m: sum([1 for a in m.schedule.agents if a.health_status == "recovered"]),
        },
        agent_reporters={"Health Status": "health_status"}
    )
