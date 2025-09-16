import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create 'images' folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load your dataset
df = pd.read_csv('data.csv')  # Adjust path if necessary

# Clean the dataset
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
df['price'] = df['price'].replace('[^0-9.]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Set Seaborn style
sns.set(style="darkgrid", context="talk")

# Plot with shaded price segments and median line
plt.figure(figsize=(13, 8))
sns.histplot(df['price'].dropna(), kde=True, bins=40, color='#2C7BB6', edgecolor='white', linewidth=1, alpha=0.85)

median_price = df['price'].median()
plt.axvline(median_price, color='#D62728', linestyle='--', linewidth=2, label=f"Median = {int(median_price):,} INR")

# Add shaded regions indicating price segments
plt.axvspan(0, 15000, color='green', alpha=0.1)
plt.axvspan(15000, 40000, color='yellow', alpha=0.1)
plt.axvspan(40000, df['price'].max(), color='red', alpha=0.1)

# Add labels for each segment
plt.text(7000, plt.ylim()[1]*0.9, 'Budget', fontsize=14, color='green')
plt.text(27000, plt.ylim()[1]*0.9, 'Mid-range', fontsize=14, color='orange')
plt.text(70000, plt.ylim()[1]*0.9, 'Premium', fontsize=14, color='red')

# Titles and labels
plt.title('Smartphone Price Distribution', fontsize=24, fontweight='bold', pad=20)
plt.suptitle('Most smartphones are budget or mid-range; few are premium.', fontsize=16, style='italic', y=0.93)
plt.xlabel('Price (INR)', fontsize=16)
plt.ylabel('Number of Phones', fontsize=16)

plt.legend(fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save and show plot
plt.savefig('images/price_distribution_enhanced.png', dpi=300)
plt.show()
