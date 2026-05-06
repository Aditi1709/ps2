from math import sqrt

def generate_candidates(order, agents):

    candidates = []

    for agent in agents:

        # Skip overloaded agents
        if len(agent["active_orders"]) >= 2:
            continue

        # Calculate distance
        distance = sqrt(
            (agent["current_x"] - order["location_x"]) ** 2 +
            (agent["current_y"] - order["location_y"]) ** 2
        )

        candidate = {
            "agent_id": agent["agent_id"],
            "order_id": order["order_id"],
            "distance": round(distance, 2),
            "priority": order["priority"],
            "agent_rating": agent["rating"]
        }

        candidates.append(candidate)

    return candidates


if __name__ == "__main__":

    sample_order = {
        "order_id": "0001",
        "location_x": 2,
        "location_y": 3,
        "priority": "high"
    }

    sample_agents = [
        {
            "agent_id": "A001",
            "current_x": 0,
            "current_y": 0,
            "rating": 4.8,
            "active_orders": []
        },
        {
            "agent_id": "A002",
            "current_x": 1,
            "current_y": 1,
            "rating": 4.5,
            "active_orders": []
        }
    ]

    candidates = generate_candidates(sample_order, sample_agents)

    print("Generated Candidates:\n")

    for candidate in candidates:
        print(candidate)