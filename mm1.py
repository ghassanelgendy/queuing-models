from queue import QueueModel

class MM1(QueueModel):
    """
    M/M/1 Queue Model
    - 1 server
    - Infinite capacity
    - Infinite population
    - Basic queue
    """
    
    def __init__(self, arrival_rate, service_rate):
        """
        Initialize the M/M/1 queueing model.
        
        Args:
            arrival_rate (float): Average arrival rate (lambda)
            service_rate (float): Average service rate (mu)
        """
        super().__init__(arrival_rate, service_rate)
        # Validate stability condition
        if self.rho >= 1:
            raise ValueError("System is unstable: arrival rate must be less than service rate")
            
    def probability_idle(self):
        """Calculate and return the probability that the system is idle (P0)."""
        return 1 - self.rho
    
    def probability_n_customers(self, n):
        """
        Calculate and return the probability of having n customers in the system.
        
        Args:
            n (int): Number of customers
        """
        if n < 0:
            return 0
        return (1 - self.rho) * (self.rho ** n)
    
    def average_customers_in_system(self):
        """Calculate and return the average number of customers in the system (L)."""
        return self.rho / (1 - self.rho)
    
    def average_customers_in_queue(self):
        """Calculate and return the average number of customers in the queue (Lq)."""
        return (self.rho ** 2) / (1 - self.rho)
    
    def average_time_in_system(self):
        """Calculate and return the average time spent in the system (W)."""
        return 1 / (self.service_rate - self.arrival_rate)
    
    def average_time_in_queue(self):
        """Calculate and return the average time spent in the queue (Wq)."""
        return self.rho / (self.service_rate - self.arrival_rate) 