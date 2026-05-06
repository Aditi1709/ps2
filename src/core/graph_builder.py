import pandas as pd
import networkx as nx
from math import isfinite

def build_graph_from_csv(file_path):
    """
    Reads a CSV file and builds a weighted graph.

    :param file_path: Path to the CSV file containing edges data.
    :return: A NetworkX graph object.
    """
    # Initialize an empty graph
    graph = nx.DiGraph()

    try:
        # Read the CSV file
        data = pd.read_csv(file_path)

        # Iterate through rows to add edges
        for _, row in data.iterrows():
            try:
                # Extract and validate required fields
                x1, y1 = row['from_x'], row['from_y']
                x2, y2 = row['to_x'], row['to_y']
                distance_minutes = row['distance_minutes']
                delay_multiplier = row['delay_multiplier']

                if not all(map(isfinite, [x1, y1, x2, y2, distance_minutes, delay_multiplier])):
                    continue

                # Calculate edge weight
                weight = distance_minutes * delay_multiplier

                # Add edge to the graph
                graph.add_edge((x1, y1), (x2, y2), weight=weight)

            except (KeyError, ValueError, TypeError):
                # Skip malformed rows
                continue

    except Exception as e:
        print(f"Error reading the file: {e}")

    return graph

# Example usage
if __name__ == "__main__":
    graph = build_graph_from_csv('data/raw/environment_edges.csv')
    print("Graph built with nodes:", graph.number_of_nodes(), "and edges:", graph.number_of_edges())
