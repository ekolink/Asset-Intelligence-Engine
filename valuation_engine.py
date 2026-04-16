import math

class Asset:
    def __init__(self, name, category, initial_cost, age):
        self.name = name
        self.category = category
        self.initial_cost = initial_cost
        self.age = age

    def get_depreciation_rate(self):
        # Updated with realistic infrastructure rates based on your MSc/PhD profile
        rates = {
            'Luxury': 0.05,
            'Tech': 0.25,
            'Machinery': 0.15,
            'Sustainable_Infrastructure': 0.025  # 2.5% reflecting long-term resilience
        }
        return rates.get(self.category, 0.10)

    def calculate_current_value(self):
        rate = self.get_depreciation_rate()        
        # Using continuous compounding formula: V = P * e^(-rt)
        return self.initial_cost * (math.exp(-rate * self.age))

# --- FOUNDER EXECUTION ---
# Testing your professional domain: A project you might audit
infrastructure_asset = Asset("Minagiotiko Dam", "Sustainable_Infrastructure", 1000000, 5)
print(f"Asset: {infrastructure_asset.name}")
print(f"Current Valuation: €{infrastructure_asset.calculate_current_value():.2f}")
