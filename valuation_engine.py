import math

class ResilientAsset:
    def __init__(self, name, category, initial_cost, age, climate_risk=0.0):
        self.name = name
        self.category = category 
        self.initial_cost = initial_cost
        self.age = age
        # climate_risk: 0.0 (None) to 1.0 (Extreme)
        self.climate_risk = climate_risk
    
    def get_base_rate(self):
        rates = {
            'Luxury': 0.05, 
            'Tech': 0.25, 
            'Machinery': 0.15, 
            'Sustainable_Infrastructure': 0.025
        }
        return rates.get(self.category, 0.10)

    def calculate_valuation(self):
        # The 'PhD Logic': Climate risk accelerates the base depreciation rate
        base_rate = self.get_base_rate()
        adjusted_rate = base_rate + (self.climate_risk * 0.05) 
        
        value = self.initial_cost * (math.exp(-adjusted_rate * self.age))
        return value

# --- PROJECT SIMULATION ---
# A project similar to the Minagiotiko Dam you've managed [cite: 499]
dam = ResilientAsset("Minagiotiko Dam", "Sustainable_Infrastructure", 1_500_000, 5, climate_risk=0.8)

print(f"Asset: {dam.name}")
print(f"Risk-Adjusted Valuation: €{dam.calculate_valuation():.2f}")
