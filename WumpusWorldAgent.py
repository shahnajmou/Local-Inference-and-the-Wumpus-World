import random


class WumpusWorldAgent:
    def __init__(self, reasoning_system, environment):
        self.reasoning_system = reasoning_system  # FOL reasoning system
        self.environment = environment  # Wumpus World environment
        self.current_position = (4, 0)  # Agent's current position in the grid
        self.num_wumpus = self.environment.get_wumpus_length()
        self.arrows = self.num_wumpus  # Number of arrows available to the agent
        self.score = 0
        self.num_gold_found = 0
        self.num_wumpus_died = 0
        self.num_agent_died = 0
        self.num_falls_into_pit = 0
        self.visited = []
        self.riskyCell = []
        self.prev_safe = []
        self.knowledge_base = self.reasoning_system.knowledge_base  # Reference to the reasoning system's knowledge base

    def perceive_environment(self):
        """Perceive the Wumpus World environment and update knowledge."""
        # Implement perception logic here
        perceptions = self.environment.perceive(self.current_position)
        for perception in perceptions:
            self.knowledge_base.add_fact(perception + str(self.current_position))

        return perceptions

    def is_valid(self, x, y):
        return 0 <= x < 4 and 0 <= y < 4

    def make_decision(self, perceptions):
        """Make a decision based on FOL-based reasoning."""
        # Implement decision-making logic using FOL reasoning
        # Example: Ask the reasoning system about the next action based on the current state
        new_position = (4, 0)

        if 'stench' not in perceptions and 'breeze' not in perceptions:
            self.prev_safe.append(self.current_position)
            actions = ['up', 'down', 'left', 'right']

            while True:
                if not actions:
                    break
                action = random.choice(actions)
                new_position = self.move(action)
                actions.remove(action)

                if new_position not in self.visited:
                    break
        else:
            self.riskyCell.append(self.current_position)
            new_position = self.prev_safe.pop()

        self.score -= 1
        self.current_position = new_position

    def move(self, action):
        """Move the agent to a new position in the grid."""
        # Implement movement logic
        new_position = self.current_position
        x, y = self.current_position

        if action == 'up' and self.is_valid(x - 1, y):
            new_position = (x - 1, y)
        elif action == 'down' and self.is_valid(x + 1, y):
            new_position = (x + 1, y)
        elif action == 'left' and self.is_valid(x, y - 1):
            new_position = (x, y - 1)
        elif action == 'right' and self.is_valid(x, y + 1):
            new_position = (x, y + 1)
        # Update the current position and perception after moving
        return new_position

    def shoot_arrow(self, direction):
        """Shoot an arrow in a specified direction."""
        # Implement arrow shooting logic
        # Update perceptions and knowledge based on the result
        arrow_hit = self.environment.shoot_arrow(self.current_position, direction)
        if arrow_hit:
            self.knowledge_base.add_fact("ArrowHit")

    def has_adjacent_not_in_list(self, position, my_list):
        x, y = position
        adjacent_positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for adj_position in adjacent_positions:
            if adj_position not in my_list:
                return True

        return False

    def explore(self):
        """Explore the Wumpus World environment."""
        while not self.environment.is_game_over(self.current_position):
            perceptions = self.perceive_environment()
            if 'gold' in perceptions:
                self.score += 1000
                break
            if self.current_position not in self.visited or self.has_adjacent_not_in_list(self.current_position,
                                                                                      self.visited):
                if self.current_position not in self.riskyCell:
                    self.visited.append(self.current_position)
                    self.make_decision(perceptions)
                else:
                    break
            else:
                self.current_position = self.prev_safe.pop()
        print(self.score)
    def report_statistics(self):
        """Report statistics after exploring the environment."""
        # Implement statistics tracking and reporting logic

    def backtrack(self):
        """Backtrack to a previous position."""
        # Implement backtracking logic if needed
