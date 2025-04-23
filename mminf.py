from queue import QueueModel
import math

class MMInf(QueueModel):
    """
    M/M/∞ Queue Model
    - Infinite servers
    - Arrival rate: λ
    - Service rate per server: μ
    """
    
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate  # λ
        self.service_rate = service_rate  # μ
        
        # Call base constructor
        super().__init__(arrival_rate, service_rate)
        
        # Precompute metrics
        self._precompute_metrics()

    def _precompute_metrics(self):
        λ = self.arrival_rate
        μ = self.service_rate
        a = λ / μ  # Traffic intensity
        
        # P0 and other probabilities
        self.P0 = math.exp(-a)
        self.a = a
        
        # Define Pn function
        def Pn(n):
            if n >= 0:
                return self.P0 * (a**n) / math.factorial(n)
            return 0.0
        self.Pn = Pn
        
        # Key metrics for M/M/∞
        self.L = a  # Average number in system
        self.Lq = 0.0  # No queue in infinite server model
        self.W = 1/μ  # Time in system
        self.Wq = 0.0  # No waiting in queue
        self.rho = 0.0  # Utilization approaches 0 with infinite servers
        self.Pw = 1 - self.P0  # Probability at least one server is busy
    
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
        return self.arrival_rate  # Effective arrival rate is same as arrival rate
    
    def average_time_in_system(self):
        return self.W
    
    def average_time_in_queue(self):
        return self.Wq
    
    def probability_all_servers_busy(self):
        # With infinite servers, this is always 0
        return 0.0

    def calculate_utilization(self):
        """
        Calculate and return the utilization factor.
        For M/M/∞, this doesn't have the same meaning as in other models
        but we return arrival_rate/service_rate for consistency.
        """
        return self.arrival_rate / self.service_rate
        
    def variance_customers(self):
        """Calculate and return the variance of the number of customers in the system."""
        # For Poisson distribution, variance equals mean
        return self.average_customers_in_system() 