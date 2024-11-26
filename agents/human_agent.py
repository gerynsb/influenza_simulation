from mesa import Agent

class HumanAgent(Agent):
    def __init__(self, unique_id, model, health_status, immunity, mobility, vaccinated):
        super().__init__(unique_id, model)
        self.health_status = health_status  # 'healthy', 'infected', 'recovered'
        self.immunity = immunity
        self.mobility = mobility
        self.vaccinated = vaccinated
        self.days_infected = 0  # Counter for infection duration

    def step(self):
        if self.health_status == 'infected':
            # Spread infection to neighbors
            self.spread_infection()

            # Recover after a certain duration
            self.days_infected += 1
            if self.days_infected > self.model.recovery_time:
                self.health_status = 'recovered'

        # Move agent if mobility > 0
        if self.mobility > 0:
            self.move()

    def spread_infection(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True, include_center=False)
        for neighbor in neighbors:
            if neighbor.health_status == 'healthy':
                infection_chance = self.model.infection_rate
                if neighbor.vaccinated:
                    infection_chance *= 0.5  # Reduce infection chance if vaccinated
                if self.random.random() < infection_chance:
                    neighbor.health_status = 'infected'

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)