import pandas as pd

def load_orders(file_path='data/raw/orders.csv'):
    """
    Load and validate orders from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of valid order dictionaries.
    """
    required_columns = {
    'order_id',
    'timestamp',
    'location_x',
    'location_y',
    'prep_time_minutes',
    'priority',
    'sla_minutes'
}
    valid_priorities = {'high', 'normal', 'low'}
    orders = []

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Validate required columns
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

        # Iterate through rows and validate each row
        for _, row in df.iterrows():
            try:
                # Check for missing values in required columns
                if row[list(required_columns)].isnull().any():
                    raise ValueError("Row contains missing values in required columns.")

                # Validate priority
                if row['priority'].lower() not in valid_priorities:
                    raise ValueError(f"Invalid priority: {row['priority']}")

                # Convert row to dictionary and append to orders list
                order = row.to_dict()
                order['priority'] = row['priority'].lower()  # Normalize priority
                orders.append(order)

            except Exception as e:
                # Handle malformed rows safely
                print(f"Skipping malformed row: {e}")

    except Exception as e:
        print(f"Error loading orders: {e}")

    return orders
orders = load_orders()
print(orders[:3])