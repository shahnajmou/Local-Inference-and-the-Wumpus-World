from KnowledgeBase import KnowledgeBase


class FOLReasoningSystem:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()  # Instantiate a knowledge base to store facts and rules

    def add_rule(self, rule):
        """Add an FOL rule to the knowledge base."""
        self.knowledge_base.add_rule(rule)

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.knowledge_base.add_fact(fact)

    def perform_resolution(self):
        """Perform resolution on the knowledge base and update it with inferred facts."""
        new_facts = self.knowledge_base.perform_resolution()
        return new_facts

    def explain_inference(self, query):
        """Explain how a specific query was inferred using resolution."""
        explanation = self.knowledge_base.explain_inference(query)
        return explanation

    def is_consistent(self):
        """Check if the current knowledge base is consistent."""
        return self.knowledge_base.is_consistent()

    def retract_rule(self, rule):
        """Retract a rule from the knowledge base."""
        self.knowledge_base.retract_rule(rule)

    def retract_fact(self, fact):
        """Retract a fact from the knowledge base."""
        self.knowledge_base.retract_fact(fact)

    def query(self, fact):
        return self.knowledge_base.query(fact)

