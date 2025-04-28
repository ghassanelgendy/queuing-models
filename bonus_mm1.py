#bonus (Phase II)
import random

def exponential(rate):
    return random.expovariate(rate)

def mm1_simulation(lambda_, mu, num_customers):
    current_time = 0
    queue = []
    next_arrival = exponential(lambda_)
    next_departure = float('inf')

    total_wait_time = 0
    total_system_time = 0
    total_idle_time = 0
    last_event_time = 0

    num_in_queue = 0
    num_departed = 0

    server_busy = False

    arrival_times = []
    #elloop elasaseya
    while num_departed < num_customers:
        # benshof elevent elgy eh departure wla arrival
        if next_arrival < next_departure:
            #tel3 arrival bazawed elcurrent time 
            current_time = next_arrival
            if not server_busy:
                # lw kdakda idle, start service immediately
                server_busy = True
                service_time = exponential(mu)
                next_departure = current_time + service_time
                # lw elsrvr kan idle, zawed idle time
                total_idle_time += current_time - last_event_time
                total_system_time += service_time
            else:
                # lw msh fady elcst beyo2af felqueue
                queue.append(current_time)
                num_in_queue += 1
            # ELBA3DOOOOOOOOOOO
            next_arrival = current_time + exponential(lambda_)
        else:
            # Lw el event elgy departure
            current_time = next_departure
            num_departed += 1

            if queue:
                # lw feh had felqueue babda2 ashaghal elcx el3aleh eldor
                arrival_time = queue.pop(0)
                wait_time = current_time - arrival_time
                service_time = exponential(mu)
                total_wait_time += wait_time
                total_system_time += wait_time + service_time
                next_departure = current_time + service_time
                num_in_queue -= 1
            else:
                # lw mafesh had mnestany , haybaa idle
                server_busy = False
                next_departure = float('inf')
                last_event_time = current_time


    # elarkam mn elsimulation
    W = total_system_time / num_customers  # Average time in system
    Wq = total_wait_time / num_customers   # Average time in queue
    L = lambda_ * W                        # Average number in system (Little's Law)
    Lq = lambda_ * Wq                      # Average number in queue (Little's Law)
    P0 = total_idle_time / current_time    # Proportion of time server is idle
    Pw = 1 - P0                            # Proportion of time server is busy
    rho = lambda_ / mu                     # Server utilization
    # Benraga3 el simulated w theoretical results

    return {
        "Simulated W (avg time in system)": W,
        "Simulated Wq (avg time in queue)": Wq,
        "Simulated L (avg number in system)": L,
        "Simulated Lq (avg number in queue)": Lq,
        "Simulated P0 (idle probability)": P0,
        "Simulated Pw (server busy)": Pw,
        "Theoretical W": 1 / (mu - lambda_),
        "Theoretical Wq": lambda_ / (mu * (mu - lambda_)),
        "Theoretical L": lambda_ / (mu - lambda_),
        "Theoretical Lq": (lambda_**2) / (mu * (mu - lambda_)),
        "Theoretical P0": 1 - (lambda_ / mu),
        "Theoretical Pw": lambda_ / mu,
        "Utilization ρ": rho
    }


random.seed(8)  # PRN 
results = mm1_simulation(lambda_=5, mu=7.5, num_customers=9999) #elexample ely felktab

#printing el results 
for k, v in results.items():
    print(f"{k}: {v:.3f}")
