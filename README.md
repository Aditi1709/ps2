# Smart Delivery Dispatch System

## Team Information
- **Team Name**: [CodeRot]
- **Year**: [2nd Year]
- **All-Female Team**: [Yes]

## Architecture Overview

#### Describe your approach here. Keep it short and clear.

    - What is your dispatch strategy?
    The system uses a score-driven dispatch strategy where each incoming order is matched with the most suitable delivery agent. Candidate agents are generated and evaluated before assigning the best-performing agent.
    - How do you score agents for incoming orders?
      Agents are scored based on multiple factors including delivery distance, agent rating, order priority, SLA urgency, and current workload. Higher scores are given to agents who can complete deliveries faster and more efficiently.

    - How do you manage SLA deadlines, priority orders, and agent capacity?
      High-priority orders receive additional scoring weight to ensure faster assignment. SLA deadlines are considered to reduce delivery delays. Agent capacity is managed using active order count and cumulative assignments to prevent overloading and maintain fair distribution.

    - What are the main steps in your pipeline?
    1. Load orders, agents, and environment data from CSV files.
    2. Build the delivery graph and initialize order queues.
    3. Generate candidate agents for each order.
    4. Score candidates using the scoring engine.
    5. Select the highest-scoring candidate.
    6. Dispatch the order and update agent states.
    7. Visualize outputs through simulation logs and the Streamlit dashboard.


**Note:** Please do not change the format or spelling of anything in this README. The fields are extracted using a script, so any changes to the structure or formatting may break the extraction process.
