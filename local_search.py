import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def fitness(state):
    handshake = (len(state)*(len(state)-1))/2
    count = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                count += 1
            elif abs(i-j) == abs(state[i] - state[j]):
                count += 1
    return handshake - count


def is_goal(state):
    handshake = (len(state)*(len(state)-1))/2
    if(fitness(state) == handshake):
        return True
    else:
        return False


def fitness_probs(population):
    sumFit = 0
    fitnessScores = []
    probabilities = []
    for parent in population:
        fitnessValue = fitness(parent)
        fitnessScores.append(fitnessValue)
        sumFit += fitnessValue

    for value in fitnessScores:
        probabilities.append(value/sumFit)

    return probabilities


def select_parents(population, probs):
    selectedParentIndeces = np.random.choice(len(population), 2, p=probs)
    return (population[selectedParentIndeces[0]],population[selectedParentIndeces[1]])


def reproduce(parent1, parent2):
    n = len(parent1)
    c = np.random.randint(0,n,dtype=int)
    return (parent1[0:c]+parent2[c:n])


def mutate (state,m_rate=0.1):
    sampledFloat = np.random.uniform(0,1)
    if sampledFloat > m_rate:
        return state
    else:
        first_sample= np.random.randint(0,len(state)) #big brain
        second_sample= np.random.randint(0,len(state))
        return tuple([second_sample if i== first_sample else j for i,j in enumerate(state)])
    
def genetic_algorithm(population, m_rate=0.1, max_iters=5000): 
    reachedGoal = False
    iterations = 0
    while iterations<max_iters and not reachedGoal:
        probs = fitness_probs(population)
        newPop = []
        for i in range(len(population)):
            parent1,parent2 = select_parents(population,probs)
            child = reproduce(parent1,parent2)
            child = mutate(child,m_rate)
            newPop.append(child)
        
        for child in newPop:
            if is_goal(child):
                reachedGoal = True

        population = newPop
        iterations+=1

    best_individual = population[0]
    for value in population:
        if(fitness(value) > fitness(best_individual)):
            best_individual = value
            
    return best_individual, iterations



def visualize_nqueens_solution( n_queens, file_name):
    N = len(n_queens)
    array = [[1 if j==n_queens[i] else 0 for i in range(len(n_queens))] for j in range(len(n_queens))]
    plt.figure(figsize=(N, N))
    ax = sns.heatmap(array,cmap='Purples', linewidths=1.5, linecolor='k', cbar=False)
    plt.savefig(file_name)
    plt.show()