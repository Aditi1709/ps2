def score_candidate(candidate):

    priority_weights = {
        "high": 100,
        "normal": 70,
        "low": 40
    }

    priority_score = priority_weights.get(candidate["priority"], 0)

    distance_penalty = candidate["distance"] * 2

    rating_bonus = candidate["agent_rating"] * 5

    final_score = priority_score + rating_bonus - distance_penalty

    candidate["score"] = round(final_score, 2)

    return candidate


if __name__ == "__main__":

    sample_candidate = {
        "agent_id": "A001",
        "order_id": "0001",
        "distance": 5,
        "priority": "high",
        "agent_rating": 4.8
    }

    scored_candidate = score_candidate(sample_candidate)

    print(scored_candidate)