from mm1 import MM1
from mm1k import MM1K
from mm1m import MM1m
from mmk import MMk
from mminf import MMInf

def print_model_results(model):
    """Print the results for a queueing model."""
    print(f"\nResults for {model.__class__.__name__} Model:")
    print("-" * 50)
    print(f"Arrival rate (λ): {model.arrival_rate:.4f}")
    print(f"Service rate (μ): {model.service_rate:.4f}")
    
    print("\nMetrics:")
    print(f"System idle probability (P0): {model.probability_idle():.4f}")
    print(f"Customers in system (L): {model.average_customers_in_system():.4f}")
    print(f"Customers in queue (Lq): {model.average_customers_in_queue():.4f}")
    print(f"Time in system (W): {model.average_time_in_system():.4f}")
    print(f"Time in queue (Wq): {model.average_time_in_queue():.4f}")
    print(f"Server utilization (ρ): {model.rho:.4f}")
    print("\nProbability Distribution:")
    for n in range(5):
        print(f"P({n}): {model.probability_n_customers(n):.4f}")

def get_model(arrival_rate, service_rate, servers=1, capacity=0, population=0):
    """Return appropriate queueing model based on parameters."""
    if population > 0:
        return MM1m(arrival_rate/population, service_rate, population)
    
    elif capacity > 0:
        return MM1K(arrival_rate, service_rate, capacity)
    elif servers > 1:
        if servers == float('inf'):
            return MMInf(arrival_rate, service_rate)
        return MMk(arrival_rate, service_rate, servers)
    return MM1(arrival_rate, service_rate)

def main():
    print("\nQueueing System Analysis Tool")
    print("-" * 30)
    
    # Get basic parameters
    arrival_rate = float(input("Arrival rate (customers/hour): "))
    service_rate = float(input("Service rate (customers/hour): "))
    servers = int(input("Number of servers (1 or more): "))
    capacity = int(input("System capacity (0 for infinite): "))
    population = int(input("Population size (0 for infinite): "))
    
    try:
        # Create and analyze model
        model = get_model(arrival_rate, service_rate, servers, capacity, population)
        
        # Print special metrics for specific models
        if isinstance(model, MM1m):
            print(f"\nEffective arrival rate: {model.effective_arrival_rate():.4f}")
        elif isinstance(model, MM1K):
            print(f"\nRejection probability: {model.probability_rejection():.4f}")
        elif isinstance(model, MMInf):
            print(f"\nCustomers variance: {model.variance_customers():.4f}")
            
        print_model_results(model)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()