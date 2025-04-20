from queue import QueueModel
import math

class MM1m(QueueModel):
    """
    M/M/1/m Queue Model
    - 1 server
    - Up to m in system (capacity)
    - Finite population (m)
    - Finite source queue, arrival rate depends on how many are already in system
    """
    
    def __init__(self, arrival_rate_per_source, service_rate, population_size):
        """
        Initialize the M/M/1/m queueing model.
        
        Args:
            arrival_rate_per_source (float): Average arrival rate per source (lambda)
            service_rate (float): Average service rate (mu)
            population_size (int): Size of the finite population (m)
        """
        # For the base class, we pass the maximum possible arrival rate
        # Store values before calling super() to make them available in calculate_utilization
        self.arrival_rate_per_source = arrival_rate_per_source
        self.population_size = population_size
        
        super().__init__(arrival_rate_per_source * population_size, service_rate)
        
        # Override the utilization factor for this model
        self.rho = self.arrival_rate_per_source / self.service_rate
        
    def calculate_utilization(self):
        """Calculate and return the utilization factor (rho)."""
        # Check if arrival_rate_per_source is already defined
        if hasattr(self, 'arrival_rate_per_source'):
            return self.arrival_rate_per_source / self.service_rate
        else:
            # During initial parent constructor call, use arrival_rate instead
            # (which is lambda_per_source * population at this point)
            return self.arrival_rate / (self.population_size * self.service_rate) if hasattr(self, 'population_size') else self.arrival_rate / self.service_rate
        
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        sum_term = 0
        for n in range(self.population_size + 1):
            sum_term += math.comb(self.population_size, n) * (self.rho ** n)
        return 1 / sum_term
    
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        if n < 0 or n > self.population_size:
            return 0
            
        return math.comb(self.population_size, n) * (self.rho ** n) * self.probability_idle()
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        result = 0
        for n in range(1, self.population_size + 1):
            result += n * self.probability_n_customers(n)
        return result
    
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        result = 0
        for n in range(2, self.population_size + 1):
            result += (n - 1) * self.probability_n_customers(n)
        return result
    
    def effective_arrival_rate(self):
        """Calculate and return the effective arrival rate (lambda_eff)."""
        return self.arrival_rate_per_source * (self.population_size - self.average_customers_in_system())
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        return self.average_customers_in_system() / self.effective_arrival_rate()
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        return self.average_customers_in_queue() / self.effective_arrival_rate() 