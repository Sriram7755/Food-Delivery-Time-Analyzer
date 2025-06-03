import pandas as pd
import random
import numpy as np

# Sample values
locations = ['Location A', 'Location B', 'Location C', 'Location D']
regions = ['North', 'South', 'East', 'West']
hours = list(range(24))

# Generate synthetic data
data = []
for i in range(1000):  # 1000 orders
    location = random.choice(locations)
    region = random.choice(regions)
    order_hour = random.choice(hours)
    order_size = random.randint(1, 5)

    # Simulate delivery time
    base_time = random.randint(20, 40)
    traffic_delay = random.randint(0, 20) if order_hour in range(11, 15) else random.randint(0, 10)
    delivery_time = base_time + traffic_delay
    delay = traffic_delay

    data.append({
        'order_id': 1000 + i,
        'delivery_time': delivery_time,
        'location': location,
        'order_size': order_size,
        'order_hour': order_hour,
        'region': region,
        'delay': delay
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('delivery_data.csv', index=False)
print("✅ delivery_data.csv generated.")
