class ObjectiveBalancer:

    def __init__(self):

        self.weights = {
            "distance": 5,
            "priority": 30,
            "rating": 2,
            "fairness": 10
        }

    def update_weights(self, new_weights):

        for key, value in new_weights.items():
            if key in self.weights:
                self.weights[key] = value

    def calculate_score(self, candidate, agent):

        score = 100

        # Distance penalty
        score -= candidate["distance"] * self.weights["distance"]

        # Priority boost
        if candidate["priority"] == "high":
            score += self.weights["priority"]

        elif candidate["priority"] == "normal":
            score += self.weights["priority"] / 2

        # Rating boost
        score += agent["rating"] * self.weights["rating"]

        # Fairness penalty
        score -= len(agent["active_orders"]) * self.weights["fairness"]

        return score


if __name__ == "__main__":

    balancer = ObjectiveBalancer()

    candidate = {
        "agent_id": "A001",
        "order_id": "0001",
        "distance": 4,
        "priority": "high"
    }

    agent = {
        "agent_id": "A001",
        "rating": 4.8,
        "active_orders": ["0007"]
    }

    score = balancer.calculate_score(candidate, agent)

    print("Calculated Score:")
    print(score)

    print("\nUpdating Weights...\n")

    balancer.update_weights({
        "distance": 3,
        "priority": 40
    })

    updated_score = balancer.calculate_score(candidate, agent)

    print("Updated Score:")
    print(updated_score)