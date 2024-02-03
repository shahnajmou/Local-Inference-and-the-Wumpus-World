from FOLReasoningSystem import FOLReasoningSystem
from WumpusWorldAgent import WumpusWorldAgent
from WumpusWorldEnvironment import WumpusWorldEnvironment


class MainApplication:
    def __init__(self):
        self.environment = None  # Initialize the Wumpus World environment
        self.agent = None  # Initialize the Wumpus World agent
        self.reasoning_system = None  # Initialize the FOL reasoning system

    def setup_environment(self):
        """Create and configure the Wumpus World environment."""
        self.environment = WumpusWorldEnvironment()

    def setup_reasoning_system(self):
        """Create and configure the FOL reasoning system."""
        self.reasoning_system = FOLReasoningSystem()

        # Toy Problem
        self.reasoning_system.add_fact('Animal(F(x)) ∨ Loves(G(x), x)')
        self.reasoning_system.add_fact('¬Loves(x, F(x)) ∨ Loves(G(x), x)')
        self.reasoning_system.add_fact('¬Loves(y, x) ∨ ¬Animal(z) ∨ ¬Kills(x, z)')
        self.reasoning_system.add_fact('¬Animal(x) ∨ Loves(Jack, x)')
        self.reasoning_system.add_fact('Kills(Jack, Tuna) ∨ Kills(Curiosity, Tuna)')
        self.reasoning_system.add_fact('Cat(Tuna)')
        self.reasoning_system.add_fact('¬Cat(x) ∨ Animal(x)')

        # Add the new rule
        self.reasoning_system.add_fact('¬Kills(Curiosity, Tuna)')

        # Query for the contradiction
        contradiction = self.reasoning_system.query('Kills(Jack, Tuna)')

        if contradiction:
            print("The knowledge base contains a logical contradiction.")
        else:
            print("The knowledge base is consistent with ¬Kills(Jack, Tuna).")

        # Add the "Wumpus Rule" facts
        self.reasoning_system.add_fact('(¬StenchInCell(A) ∨ WumpusInCell(B))')
        self.reasoning_system.add_fact('(¬StenchInCell(A) ∨ Adjacent(A, B))')
        self.reasoning_system.add_fact('(¬WumpusInCell(n) ∨ ¬Adjacent(n, c) ∨ StenchInCell(c))')

        # Add the "Pit Rule" facts
        self.reasoning_system.add_fact('(¬BreezeInCell(A) ∨ PitInCell(B))')
        self.reasoning_system.add_fact('(¬BreezeInCell(A) ∨ Adjacent(A, B))')
        self.reasoning_system.add_fact('(¬PitInCell(n) ∨ ¬Adjacent(n, c) ∨ BreezeInCell(c))')

    def setup_agent(self):
        """Create and configure the Wumpus World agent."""
        self.agent = WumpusWorldAgent(self.reasoning_system, self.environment)

    def start_exploration(self):
        """Initiate the exploration of the Wumpus World."""
        if self.agent is None or self.environment is None or self.reasoning_system is None:
            print("Error: Environment, agent, or reasoning system not properly configured.")
            return
        # Implement logic to start the exploration process
        self.agent.explore()

    def report_statistics(self):
        """Generate and display exploration statistics."""
        if self.agent is None:
            print("Error: Agent not initialized.")
            return
        # Implement logic to gather and report exploration statistics
        self.agent.report_statistics()

    def run(self):
        """Main entry point to run the Wumpus World Explorer application."""
        print("Wumpus World Explorer")
        self.setup_environment()
        self.setup_reasoning_system()
        self.setup_agent()
        self.start_exploration()
        self.report_statistics()


# Entry point to run the application
if __name__ == "__main__":
    app = MainApplication()
    app.run()
