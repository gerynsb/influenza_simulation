from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from models.influenza_model import InfluenzaModel
from visualization.portrayal import agent_portrayal

# Define grid visualization
grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

# Define chart visualization
chart = ChartModule(
    [
        {"Label": "Healthy", "Color": "Green"},
        {"Label": "Infected", "Color": "Red"},
        {"Label": "Recovered", "Color": "Blue"},
    ],
    data_collector_name="datacollector"
)

server = ModularServer(
    InfluenzaModel,
    [grid, chart],
    "Influenza Simulation",
    {
        "width": 20,
        "height": 20,
        "individual_data_path": "data/individual_data.csv",
        "env_factors_path": "data/environmental_factors.csv",
        "sim_params_path": "data/simulation_parameters.csv",
    }
)