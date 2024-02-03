import sys, getopt, random


class WumpusWorldEnvironment:
    def __init__(self):
        self.grid = []
        self.pits = []
        self.breeze = []
        self.gold = []
        self.glitter = []
        self.wumpus = []
        self.stench = []
        self.cave = self.generate_grid()  # Generate the Wumpus World grid

    def generate_grid(self):
        """Generate the initial Wumpus World grid."""
        # Implement logic to create a random grid with Wumpus, pits, gold, and empty cells
        # Ensure that the generated grid is solvable and meets the specified constraints
        self.grid = [['safe'], ['gold', 'glitter'], ['stench'], ['wumpus'], ['stench']], [['safe'], ['safe'], ['safe'], ['stench'],
                                                                               ['safe']], [['safe'], ['safe'], ['safe'],
                                                                                           ['safe'],
                                                                                           ['safe', 'breeze']], [
            ['safe'], ['safe'], ['safe'], ['safe', 'breeze'], ['pit']], [['safe'], ['safe'], ['safe', 'breeze'],
                                                                         ['pit'], ['breeze']]

        # Populate the lists based on the grid
        for row_index, row in enumerate(self.grid):
            for col_index, cell_contents in enumerate(row):
                cell_coordinates = (row_index, col_index)
                for content in cell_contents:
                    if content == 'pit':
                        self.pits.append(cell_coordinates)
                    elif content == 'breeze':
                        self.breeze.append(cell_coordinates)
                    elif content == 'gold':
                        self.gold.append(cell_coordinates)
                    elif content == 'glitter':
                        self.glitter.append(cell_coordinates)
                    elif content == 'wumpus':
                        self.wumpus.append(cell_coordinates)
                    elif content == 'stench':
                        self.stench.append(cell_coordinates)

        return self.grid

    def is_game_over(self, current_position):
        """Check if the game is over (agent won or lost)."""
        if current_position in self.pits or current_position in self.wumpus:
            return True
        else:
            return False

    def perceive(self, position):
        """Provide sensory information to the agent based on its position."""
        row = position[0]
        col = position[1]
        perceptions = self.grid[row][col]
        return perceptions

    def move_agent(self, new_position):
        """Move the agent to a new position in the grid."""
        # Implement logic to move the agent and update its position
        self.agent_position = new_position

    def shoot_arrow(self, position, direction):
        """Handle the agent's arrow shot in a specified direction."""
        # Implement logic to handle arrow shooting and its effects (e.g., killing a nearby Wumpus)
        arrow_hit = False  # Placeholder; actual logic depends on implementation
        return arrow_hit

    def get_wumpus_length(self):
        return len(self.wumpus)


