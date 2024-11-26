from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
import pandas as pd
from agents.human_agent import HumanAgent
from collectors.data_collector import create_data_collector


class InfluenzaModel(Model):
    def __init__(self, width, height, individual_data_path, env_factors_path, sim_params_path):
        super().__init__()
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Load data from CSV files
        individual_data = pd.read_csv(individual_data_path)
        env_factors = pd.read_csv(env_factors_path)
        sim_params = pd.read_csv(sim_params_path)

        # Simulation parameters
        self.infection_rate = sim_params['probabilitas_infeksi'].iloc[0]
        self.recovery_rate = sim_params['probabilitas_pemulihan'].iloc[0]
        self.recovery_time = sim_params['infection_duration'].iloc[0]

        # Ensure at least one infected agent
        has_infected_agent = False

        # Create agents
        for _, row in individual_data.iterrows():
            agent = HumanAgent(
                unique_id=row['id'],
                model=self,
                health_status=row['status'],
                immunity=row['resistensi'],
                mobility=row['mobilitas'],
                vaccinated=row['vaccinated']
            )
            if row['status'] == 'infected':
                has_infected_agent = True

            # Place agent on the grid
            x, y = self.random.randint(0, width - 1), self.random.randint(0, height - 1)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

        # If no infected agents, assign one randomly
        if not has_infected_agent:
            random_agent = self.random.choice(self.schedule.agents)
            random_agent.health_status = 'infected'

        # Initialize DataCollector
        self.datacollector = create_data_collector()

    def step(self):
        """
        Run one step of the simulation.
        """
        self.schedule.step()  # Update all agents
        self.datacollector.collect(self)  # Collect data for this step

        # Debugging: Print data collected in the last 5 steps
        model_data = self.datacollector.get_model_vars_dataframe()
        print(model_data.tail())  # Display recent data in the terminal
