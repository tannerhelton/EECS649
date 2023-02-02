from agents import *
from notebook import psource

class TrivialVacuumEnvironment(Environment):

    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()
        self.status = {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty'])}

    def thing_classes(self):
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent,
                TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            agent.location = loc_B
            agent.performance -= 1
        elif action == 'Left':
            agent.location = loc_A
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B])
    
# loc_A, loc_B = (0, 0), (1, 0)

# # Initialize the two-state environment
trivial_vacuum_env = TrivialVacuumEnvironment()

# # Check the initial state of the environment
# print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# random_agent = Agent(program=RandomAgentProgram(['Right', 'Left', 'Suck', 'NoOp']))

# trivial_vacuum_env.add_thing(random_agent)

# # Running the environment
# trivial_vacuum_env.step()

# # Check the current state of the environment
# print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# print("RandomVacuumAgent is located at {}.".format(random_agent.location))

# table = {((loc_A, 'Clean'),): 'Right',
#              ((loc_A, 'Dirty'),): 'Suck',
#              ((loc_B, 'Clean'),): 'Left',
#              ((loc_B, 'Dirty'),): 'Suck',
#              ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
#              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
#              ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
#              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
#              ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
#              ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'
#         }

# # Create a table-driven agent
# table_driven_agent = Agent(program=TableDrivenAgentProgram(table=table))

# # trivial_vacuum_env.delete_thing(random_agent)

# # Add the table-driven agent to the environment
# trivial_vacuum_env.add_thing(table_driven_agent)

# print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))

# # Run the environment
# trivial_vacuum_env.step()

# # Check the current state of the environment
# print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# print("TableDrivenVacuumAgent is located at {}.".format(table_driven_agent.location))

def update_state(state, action, percept, model):
    pass

# Create a model-based reflex agent
model_based_reflex_agent = ModelBasedVacuumAgent()

# Add the agent to the environment
trivial_vacuum_env.add_thing(model_based_reflex_agent)

print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))

# Run the environment
trivial_vacuum_env.step()

# Check the current state of the environment
print("State of the Environment: {}.".format(trivial_vacuum_env.status))

print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))