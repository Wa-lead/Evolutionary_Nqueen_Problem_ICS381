if __name__ == "__main__":
    import numpy as np
    from local_search import *
    
    # set random seed for reproducibility
    rand_seed=735122311
    np.random.seed(rand_seed)
    
    # helper function to generate random N-queens state
    def gen_rand_tuple(N=8):
        return tuple(np.random.randint(low=0, high=N, size=N))
        
    # tests 1
    rand_state = gen_rand_tuple()
    print(rand_state)
    print(fitness(rand_state))
    print(is_goal(rand_state))
    
    goal_state = (2,0,3,1)
    print(fitness(goal_state))
    print(is_goal(goal_state))
    print('_______________________________________________________________________')
    
    # tests 2
    population = [gen_rand_tuple() for _ in range(5)]
    pop_probs = fitness_probs(population)
    
    print(population)
    print([fitness(s) for s in population])
    print(pop_probs)
    print('_______________________________________________________________________')
    
    p1, p2 = select_parents(population, pop_probs)
    child = reproduce(p1, p2)
    mchild = mutate(child, m_rate=0.8)
    print(p1, p2)
    print(child)
    print(mchild)
    print('_______________________________________________________________________')
    
    # tests 3
    population = [gen_rand_tuple(N=8) for _ in range(20)]
    best_individual, num_iters = genetic_algorithm(population, m_rate=0.1, max_iters=10000)
    print('Best individual: {}'.format(best_individual))
    print('Best individual fitness: {}'.format(fitness(best_individual)))
    print('Best individual is_goal?: {}'.format(is_goal(best_individual)))
    print('# iterations: {}'.format(num_iters)) 