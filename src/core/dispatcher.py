from core.candidate_generator import generate_candidates
from core.scoring_engine import score_candidate
from core.agent_registry import assign_order

def get_best_candidate(candidates):

    if not candidates:
        return None

    best_candidate = max(candidates, key=lambda x: x["score"])

    return best_candidate
class Dispatcher:

    def dispatch_order(self, order, agents):

        candidates = generate_candidates(order, agents)

        scored_candidates = []

        for candidate in candidates:
            scored = score_candidate(candidate)
            scored_candidates.append(scored)

        best_candidate = get_best_candidate(scored_candidates)

        if not best_candidate:
            return None

        selected_agent_id = best_candidate["agent_id"]

        for agent in agents:

            if agent["agent_id"] == selected_agent_id:

                agent["active_orders"].append(order["order_id"])
                agent["cumulative_assignments"] += 1

                return {
                    "assigned_agent": selected_agent_id,
                    "order_id": order["order_id"],
                    "score": best_candidate["score"]
                }

        return None


if __name__ == "__main__":

    order = {
        "order_id": "0001",
        "location_x": 2,
        "location_y": 3,
        "priority": "high"
    }

    agents = [
        {
            "agent_id": "A001",
            "current_x": 0,
            "current_y": 0,
            "rating": 4.8,
            "active_orders": [],
            "cumulative_assignments": 0
        },
        {
            "agent_id": "A002",
            "current_x": 1,
            "current_y": 1,
            "rating": 4.2,
            "active_orders": ["0009"],
            "cumulative_assignments": 2
        }
    ]

    dispatcher = Dispatcher()

    result = dispatcher.dispatch_order(order, agents)

    print("Dispatch Result:\n")
    print(result)

    print("\nUpdated Agents:\n")
    print(agents)