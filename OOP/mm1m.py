import math
from queue import QueueModel  # Assuming you have this class

class MM1m(QueueModel):
    """
    M/M/1/m Queue Model
    - 1 server
    - Finite source population: m sources
    - Arrival rate per source: λ
    - Service rate: μ
    """
    
    def __init__(self, arrival_rate_per_source, service_rate, population_size):
        self.arrival_rate_per_source = arrival_rate_per_source  # λ
        self.service_rate = service_rate  # μ
        self.population_size = population_size  # m
        
        # Call base constructor with max possible λ
        super().__init__(arrival_rate_per_source * population_size, service_rate)
        
        # Precompute P0 and related quantities
        self._precompute_metrics()

    def _precompute_metrics(self):
        λ = self.arrival_rate
        μ = self.service_rate
        m = self.population_size

        # Step 1: Calculate P0
        summation = 0.0
        for n in range(m + 1):
            term = (math.factorial(m) / math.factorial(m - n)) * ((λ / μ) ** n)
            summation += term
        self.P0 = 1.0 / summation

        # Step 2: Define Pn(n)
        def Pn(n):
            if 0 <= n <= m:
                return (math.factorial(m) / math.factorial(m - n)) * ((λ / μ) ** n) * self.P0
            return 0.0
        self.Pn = Pn

        # Step 3: Average number in system
        self.L = sum(n * self.Pn(n) for n in range(m + 1))

        # Step 4: Effective arrival rate
        self.lambda_eff = λ * (m - self.L)

        # Step 5: Mean time in system (W)
        self.W = self.L / self.lambda_eff if self.lambda_eff > 0 else 0.0

        # Step 6: Mean in service = 1 - P0
        self.Lq = self.L - (1 - self.P0)

        # Step 7: Mean waiting time in queue (Wq)
        self.Wq = self.Lq / self.lambda_eff if self.lambda_eff > 0 else 0.0

        # Step 8: Probability server is busy (Pw)
        self.Pw = 1 - self.P0

    # Accessor methods
    def probability_idle(self):
        return self.P0
    
    def probability_n_customers(self, n):
        return self.Pn(n)
    
    def average_customers_in_system(self):
        return self.L
    
    def average_customers_in_queue(self):
        return self.Lq
    
    def effective_arrival_rate(self):
        return self.lambda_eff
    
    def average_time_in_system(self):
        return self.W
    
    def average_time_in_queue(self):
        return self.Wq
    
    def probability_all_servers_busy(self):
        return self.Pw
