class AgentRegistry:
    def __init__(self):
        self.agents = {}
        self.max_active_orders = 2

    def add_agent(self, agent):
        self.agents[agent["agent_id"]] = agent

    def get_agent(self, agent_id):
        return self.agents.get(agent_id)

    def get_available_agents(self):
        available = []

        for agent in self.agents.values():
            if len(agent["active_orders"]) < self.max_active_orders:
                available.append(agent)

        return available

    def assign_order(self, agent_id, order_id):
        agent = self.get_agent(agent_id)

        if not agent:
            return False

        if len(agent["active_orders"]) >= self.max_active_orders:
            return False

        agent["active_orders"].append(order_id)
        agent["cumulative_assignments"] += 1

        return True

    def complete_order(self, agent_id, order_id):
        agent = self.get_agent(agent_id)

        if not agent:
            return False

        if order_id in agent["active_orders"]:
            agent["active_orders"].remove(order_id)
            return True

        return False


if __name__ == "__main__":
    registry = AgentRegistry()

    registry.add_agent({
        "agent_id": "A001",
        "current_x": 0,
        "current_y": 0,
        "rating": 4.8,
        "active_orders": [],
        "cumulative_assignments": 0
    })

    registry.add_agent({
        "agent_id": "A002",
        "current_x": 1,
        "current_y": 1,
        "rating": 4.5,
        "active_orders": [],
        "cumulative_assignments": 0
    })

    print("Available Agents:")
    print(registry.get_available_agents())

    registry.assign_order("A001", "0001")

    print("\nAfter Assigning Order:")
    print(registry.get_agent("A001"))

    registry.complete_order("A001", "0001")

    print("\nAfter Completing Order:")
    print(registry.get_agent("A001"))
    
def assign_order(agent, order_id):

    if len(agent["active_orders"]) >= 2:
        return False

    agent["active_orders"].append(order_id)
    agent["cumulative_assignments"] += 1

    return True