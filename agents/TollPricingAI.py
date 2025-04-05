class TollPricingAI:
    def __init__(self):
        self.base_toll = 10  # Base toll price

    def calculate_toll(self, route, congestion_level):
        # Higher toll during congestion, lower when clear
        return self.base_toll + congestion_level * 2  # Arbitrary logic for toll increase
