from loaders.load_orders import load_orders
from loaders.load_agents import load_agents
from core.dispatcher import Dispatcher


def run_simulation():

    orders = load_orders()
    agents = load_agents()

    dispatcher = Dispatcher()

    print("\n===== SMART DELIVERY SIMULATION =====\n")

    for order in orders[:10]:

        result = dispatcher.dispatch_order(order, agents)

        if result:

            print(
                f"Order {result['order_id']} "
                f"assigned to Agent {result['assigned_agent']} "
                f"(Score: {round(result['score'], 2)})"
            )

        else:
            print(f"Order {order['order_id']} could not be assigned")

    print("\n===== FINAL AGENT STATES =====\n")

    for agent in agents[:5]:
        print(agent)


if __name__ == "__main__":
    run_simulation()