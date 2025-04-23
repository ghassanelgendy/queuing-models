import math

def mm1(lambda_rate, mu_rate):
    rho = lambda_rate / mu_rate
    P0 = 1 - rho
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_rate - lambda_rate)
    Wq = rho / (mu_rate - lambda_rate)
    Pw = rho  # For M/M/1, Pw = ρ
    # Calculate P1 through P4
    Pn = [(1 - rho) * (rho**n) for n in range(1,5)]
    return {'ρ': rho, 'P0': P0, 'P1': Pn[0], 'P2': Pn[1], 'P3': Pn[2], 'P4': Pn[3], 
            'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq, 'Pw': Pw}

def mmk(lambda_rate, mu_rate, k):
    a = lambda_rate / mu_rate
    rho = a / k
    sum_terms = sum(a**n / math.factorial(n) for n in range(k))
    P0 = 1 / (sum_terms + a**k / (math.factorial(k) * (1 - rho)))
    # Calculate P1 through P4
    Pn = []
    for n in range(1,5):
        if n < k:
            Pn.append(P0 * (a**n) / math.factorial(n))
        else:
            Pn.append(P0 * (a**n) / (math.factorial(k) * k**(n-k)))
    Lq = (P0 * a**k * rho) / (math.factorial(k) * (1 - rho)**2)
    L = Lq + a
    Wq = Lq / lambda_rate
    W = Wq + 1 / mu_rate
    # Probability all servers are busy
    Pw = sum(P0 * (a**n) / (math.factorial(k) * k**(n-k)) for n in range(k, k+1))
    return {'ρ': rho, 'P0': P0, 'P1': Pn[0], 'P2': Pn[1], 'P3': Pn[2], 'P4': Pn[3],
            'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq, 'Pw': Pw}

def mm1k(lambda_rate, mu_rate, K):
    rho = lambda_rate / mu_rate
    if abs(rho - 1) < 1e-12:
        P0 = 1 / (K + 1)
    else:
        P0 = (1 - rho) / (1 - rho**(K + 1))
    Pn = [P0 * rho**n for n in range(K+1)]
    PK = Pn[K]
    L = sum(n * Pn[n] for n in range(K+1))
    lambda_eff = lambda_rate * (1 - PK)
    W = L / lambda_eff if lambda_eff else float('inf')
    Wq = W - 1/mu_rate
    Lq = lambda_eff * Wq
    Pw = 1 - P0  # Probability server is busy
    return {'ρ': rho, 'P0': P0, 'P1': Pn[1], 'P2': Pn[2], 'P3': Pn[3], 'P4': Pn[4] if K >= 4 else 0,
            'PK': PK, 'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq, 'Pw': Pw}

def mm1m(lambda_rate, mu_rate, m):
    # Finite-source M/M/1/m model
    a = lambda_rate / mu_rate
    # P0 normalization
    denom = sum(math.factorial(m) / math.factorial(m-n) * a**n for n in range(m+1))
    P0 = 1 / denom
    Pn = [P0 * (math.factorial(m) / math.factorial(m-n)) * a**n for n in range(m+1)]
    L = sum(n * Pn[n] for n in range(m+1))
    lambda_eff = lambda_rate * sum((m-n) * Pn[n] for n in range(m+1))
    W = L / lambda_eff if lambda_eff else float('inf')
    Wq = W - 1/mu_rate
    Lq = lambda_eff * Wq
    rho = lambda_eff / mu_rate  # Effective utilization
    Pw = 1 - P0  # Probability server is busy
    return {'ρ': rho, 'P0': P0, 'P1': Pn[1], 'P2': Pn[2], 'P3': Pn[3], 'P4': Pn[4] if m >= 4 else 0,
            'L': L, 'Lq': Lq, 'W': W, 'Wq': Wq, 'λ_eff': lambda_eff, 'Pw': Pw}

def mminf(lambda_rate, mu_rate, Nmax):
    a = lambda_rate / mu_rate
    P0 = math.exp(-a)
    Pn = [P0 * a**n / math.factorial(n) for n in range(Nmax+1)]
    rho = lambda_rate / (mu_rate * float('inf'))  # Approaches 0
    Pw = 1 - P0  # Probability at least one server is busy
    return {'ρ': rho, 'a': a, 'P0': P0, 'P1': Pn[1], 'P2': Pn[2], 'P3': Pn[3], 'P4': Pn[4],
            'L': a, 'Lq': 0.0, 'W': 1/mu_rate, 'Wq': 0.0, 'Pw': Pw}

def print_dict(d):
    for k, v in d.items():
        if isinstance(v, list):
            print(f"{k}:")
            for i, val in enumerate(v):
                print(f"  {i}: {val:.6f}")
        else:
            print(f"{k} = {v:.6f}")
    print()

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
        # Determine which model to use and calculate results
        if population > 0:
            res = mm1m(arrival_rate, service_rate, population)
            print("\nM/M/1/m (finite source) results:")
        elif capacity > 0:
            res = mm1k(arrival_rate, service_rate, capacity)
            print(f"\nM/M/1/{capacity} results:")
        elif servers > 1:
            if servers == int(99):
                res = mminf(arrival_rate, service_rate, 5)  # Show first 5 probabilities
                print("\nM/M/∞ results:")
            else:
                res = mmk(arrival_rate, service_rate, servers)
                print(f"\nM/M/{servers} results:")
        else:
            res = mm1(arrival_rate, service_rate)
            print("\nM/M/1 results:")
            
        print_dict(res)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()