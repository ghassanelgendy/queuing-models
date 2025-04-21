from queue import QueueModel

class MM1K(QueueModel):
    """
    M/M/1/K Queue Model
    - 1 server
    - K capacity (finite)
    - Infinite population
    - Finite buffer queue, customers blocked when full
    """
    
    def __init__(self, arrival_rate, service_rate, capacity):
        """
        Initialize the M/M/1/K queueing model.
        
        Args:
            arrival_rate (float): Average arrival rate (lambda)
            service_rate (float): Average service rate (mu)
            capacity (int): Maximum number of customers allowed in the system (K)
        """
        super().__init__(arrival_rate, service_rate)
        self.capacity = capacity
        
    def calculate_utilization(self):
        """Calculate and return the utilization factor (rho)."""
        # For M/M/1/K, we don't need to check stability condition as in M/M/1
        return self.arrival_rate / self.service_rate
        
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        if self.rho == 1:
            return 1 / (self.capacity + 1)
        else:
            return (1 - self.rho) / (1 - self.rho ** (self.capacity + 1))
    
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        if n < 0 or n > self.capacity:
            return 0
            
        if self.rho == 1:
            return 1 / (self.capacity + 1)
        else:
            return self.rho ** n * self.probability_idle()
    
    def probability_rejection(self):
        """Calculate and return the probability that an arriving customer is rejected."""
        if self.rho == 1:
            return 1 / (self.capacity + 1)
        else:
            return (self.rho ** self.capacity * (1 - self.rho)) / (1 - self.rho ** (self.capacity + 1))
    
    def effective_arrival_rate(self):
        """Calculate and return the effective arrival rate (lambda_eff)."""
        return self.arrival_rate * (1 - self.probability_rejection())
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        if self.rho == 1:
            return self.capacity / 2
        else:
            numerator = self.rho * (1 - (self.capacity + 1) * self.rho ** self.capacity + self.capacity * self.rho ** (self.capacity + 1))
            denominator = (1 - self.rho) * (1 - self.rho ** (self.capacity + 1))
            return numerator / denominator
    
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        return self.average_customers_in_system() - (1 - self.probability_idle())
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        return self.average_customers_in_system() / self.effective_arrival_rate()
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        return self.average_customers_in_queue() / self.effective_arrival_rate() 
        
    def probability_all_servers_busy(self):
        """Calculate and return the probability that all servers are busy (Pw)."""
        # For M/M/1/K, this is 1 - P0 since there's only one server
        return 1 - self.probability_idle() 