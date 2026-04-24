import random
import pandas as pd

# Categories of products
categories = [
    'Electronics', 'Accessories', 'Wearables', 'Home Appliances',
    'Gaming', 'Fitness', 'Kitchen', 'Furniture', 'Fashion', 'Beauty'
]

# List of possible features
features = [
    'lightweight', 'portable', 'high-performance', 'OLED-display', '4K', 'Bluetooth',
    'wireless', 'rechargeable', 'noise-cancelling', 'long-battery-life', 'voice-control',
    'smart-features', 'heart-rate-monitor', 'water-resistant', 'ergonomic', 'fast-charging',
    'precision-control', 'compact', 'eco-friendly', 'energy-saving', 'sleek-design',
    'durable', 'multi-purpose', 'self-cleaning', 'remote-control', 'smart-app', 'wifi-enabled',
    'sleep-monitor', 'step-tracking', 'touch-screen', 'foldable', 'waterproof', 'reversible'
]

# Generate 120+ rows of product data
products = []

for i in range(1, 130):  # 130 products
    product = {
        'id': i,
        'name': f'Product {i}',
        'category': random.choice(categories),
        'features': ', '.join(random.sample(features, random.randint(3, 6)))  # 3 to 6 random features
    }
    products.append(product)

# Convert the list to a DataFrame for easier viewing
product_df = pd.DataFrame(products)

# Save the dataset to a CSV file (optional, if you want to use this data elsewhere)
product_df.to_csv('product_dataset.csv', index=False)

# Display the first few rows of the dataset
print(product_df.head(10))
