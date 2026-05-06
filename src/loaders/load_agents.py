import pandas as pd

def load_agents(file_path='data/raw/agents.csv'):
    """
    Load agents from a CSV file, validate required columns, and return a list of agent dictionaries.

    Args:
        file_path (str): Path to the CSV file containing agent data.

    Returns:
        list: A list of dictionaries representing agents.
    """
    required_columns = {
    'agent_id',
    'current_x',
    'current_y',
    'rating'
}
    agents = []

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Validate required columns
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

        # Process rows into dictionaries
        for _, row in df.iterrows():
            try:
                agent = {
                 'agent_id': row['agent_id'],
                 'current_x': row['current_x'],
                 'current_y': row['current_y'],
                 'rating': row['rating'],
                 'active_orders': [],
                 'cumulative_assignments': 0
                }
                agents.append(agent)
            except KeyError as e:
                print(f"Skipping malformed row due to missing key: {e}")

    except Exception as e:
        print(f"Error loading agents: {e}")

    return agents
agents = load_agents()
print(agents[:3])