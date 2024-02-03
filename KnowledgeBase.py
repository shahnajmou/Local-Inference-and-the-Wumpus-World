class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Set to store known facts
        self.rules = []  # List to store FOL rules

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def retract_fact(self, fact):
        """Retract a fact from the knowledge base."""
        if fact in self.facts:
            self.facts.remove(fact)

    def add_rule(self, rule):
        """Add an FOL rule to the knowledge base."""
        self.rules.append(rule)

    def retract_rule(self, rule):
        """Retract an FOL rule from the knowledge base."""
        if rule in self.rules:
            self.rules.remove(rule)

    def perform_resolution(self):
        """Perform resolution on the knowledge base and update it with inferred facts."""
        new_facts = set()

        # Iterate through all pairs of rules and facts to perform resolution
        for rule in self.rules:
            for fact in self.facts:
                # Apply resolution to the current rule and fact
                resolution_result = self.resolve(rule, fact)

                # Check if resolution resulted in new facts
                if resolution_result:
                    # Add the new facts to the set of inferred facts
                    new_facts.update(resolution_result)

        # Update the knowledge base with the newly inferred facts
        self.facts.update(new_facts)

        return new_facts

    def explain_inference(self, query):
        """Explain how a specific query was inferred using resolution."""
        explanation = "Explanation of how query '{}' was inferred.".format(query)
        # Implement logic to provide an explanation of the inference
        return explanation

    def is_consistent(self):
        """Check if the current knowledge base is consistent."""
        # Implement consistency checking logic
        return True  # Placeholder; actual logic depends on implementation

    def get_facts(self):
        """Retrieve all known facts from the knowledge base."""
        return list(self.facts)

    def get_rules(self):
        """Retrieve all FOL rules from the knowledge base."""
        return self.rules

    def query(self, fact):
        return fact in self.facts
