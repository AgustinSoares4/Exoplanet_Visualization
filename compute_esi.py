import pandas as pd
import numpy as np

# Load the dataset (date: 2025.04.03_15.51.33)
df = pd.read_csv("nasa_all.csv", comment="#")

# Earth reference values and weights
earth = {
    'pl_rade': 1.0,
    'density': 5.51,
    'escape_velocity': 11.2,
    'pl_eqt': 288
}

weights = {
    'pl_rade': 0.57,
    'density': 1.07,
    'escape_velocity': 0.70,
    'pl_eqt': 5.58
}

# Function to calculate ESI safely, with internal missing-value checks
def calculate_esi(row):
    try:
        # Check for required inputs
        if pd.isna(row['pl_rade']) or pd.isna(row['pl_bmasse']) or pd.isna(row['pl_eqt']):
            return np.nan

        # Calculate derived properties
        radius = row['pl_rade']
        mass = row['pl_bmasse']
        temp = row['pl_eqt']

        density = (mass / radius**3) * 5.51
        escape_velocity = 11.2 * np.sqrt(mass / radius)

        # Combine into dictionary for easier handling
        values = {
            'pl_rade': radius,
            'density': density,
            'escape_velocity': escape_velocity,
            'pl_eqt': temp
        }

        # Compute ESI
        esi = 1.0
        for var in values:
            xi = values[var]
            xi_earth = earth[var]
            wi = weights[var]
            esi *= (1 - abs((xi - xi_earth) / (xi + xi_earth))) ** wi

        return esi

    except Exception:
        return np.nan

# Apply the ESI function across the entire dataset
df['ESI'] = df.apply(calculate_esi, axis=1)


# Save results to CSV
df.to_csv("all_exo.csv", index=False)

# Print count
print(f"🌍 Filtered {len(df)} Earth-like exoplanets with ESI ≥ 0.25")
