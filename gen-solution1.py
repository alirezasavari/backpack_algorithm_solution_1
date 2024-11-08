import random 
 
weight = [55, 67, 87, 29, 67, 32, 7, 14, 52, 33, 72, 51, 94, 102, 21, 28, 8, 58, 9, 46, 23, 13, 19, 19, 70, 42, 60, 37, 22] 
size = [0.03, 0.12, 0.34, 0.38, 0.21, 0.16, 0.25, 0.32, 0.86, 0.30, 0.72, 0.93, 1.1, 0.35, 0.58, 0.46, 0.15, 0.32, 0.29, 0.03, 0.01, 0.76, 0.54, 0.72, 0.26, 0.11, 0.30, 0.65, 0.43] 
value = [11, 97, 34, 30, 47, 31, 12, 9, 98, 54, 59, 71, 43, 28, 56, 87, 21, 16, 30, 5, 11, 39, 75, 31, 19, 53, 70, 45, 69] 
n = len(weight) 
W = 220 
S = 2 
 
pop_size = 100 
max_gen = 300 
cx_prob = 0.8 
mut_prob = 0.2 
 
def create_solution(): 
    solution = [] 
    for i in range(n): 
        solution.append(random.randint(0, 1)) 
    return solution 
 
def fitness(solution): 
    total_weight = 0 
    total_size = 0 
    total_value = 0 
    for i in range(n): 
        if solution[i] == 1: 
            total_weight += weight[i] 
            total_size += size[i] 
            total_value += value[i] 
    if total_weight > W or total_size > S: 
        return 0 
    else: 
        return total_value 
 
def selection(population): 
    total_fitness = 0 
    for solution in population: 
        total_fitness += fitness(solution) 
    r = random.uniform(0, total_fitness) 
    partial_sum = 0 
    for solution in population: 
        partial_sum += fitness(solution) 
        if partial_sum >= r: 
            return solution 
 
def crossover(parent1, parent2): 
    point = random.randint(1, n-1) 
    offspring1 = [] 
    offspring2 = [] 
    for i in range(n): 
        if i < point: 
            offspring1.append(parent1[i]) 
            offspring2.append(parent2[i]) 
        else: 
            offspring1.append(parent2[i]) 
            offspring2.append(parent1[i]) 
    return offspring1, offspring2 
 
def mutation(solution): 
    for i in range(n): 
        r = random.random() 
        if r < mut_prob: 
            solution[i] = 1 - solution[i] 
    return solution 
 
population = [] 
for i in range(pop_size): 
    population.append(create_solution()) 
 
best_solution = None 
best_fitness = 0 
 
for gen in range(max_gen): 
    offspring_population = [] 
 
    for _ in range(pop_size // 2): 
        parent1 = selection(population) 
        parent2 = selection(population) 
        offspring1, offspring2 = crossover(parent1, parent2) 
        offspring1 = mutation(offspring1) 
        offspring2 = mutation(offspring2) 
        offspring_population.append(offspring1) 
        offspring_population.append(offspring2) 
 
    population = offspring_population 
 
    for solution in population: 
        current_fitness = fitness(solution) 
        if current_fitness > best_fitness: 
            best_fitness = current_fitness 
            best_solution = solution 
 
print("Best solution:", best_solution) 
print("Best fitness:", best_fitness)
