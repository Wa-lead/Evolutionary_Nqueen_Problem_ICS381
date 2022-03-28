if __name__ == "__main__":
    import numpy as np
    from local_search import *
    
    # set random seed for reproducibility
    rand_seed=2145113219
    np.random.seed(rand_seed)
    population= [(4, 5, 1, 4, 4, 3, 2, 3), (4, 1, 3, 2, 2, 7, 4, 0), (7, 6, 2, 7, 7, 2, 7, 4), (1, 3, 3, 6, 4, 0, 2, 3), 
                  (5, 1, 2, 3, 6, 7, 2, 3), (2, 1, 0, 0, 1, 4, 5, 2), (0, 4, 0, 3, 0, 4, 1, 0), (2, 7, 3, 2, 0, 2, 3, 2), 
                  (4, 7, 4, 6, 2, 1, 0, 2), (2, 4, 7, 1, 1, 7, 6, 6), (3, 2, 2, 3, 4, 1, 7, 0), (4, 7, 7, 0, 3, 2, 4, 3), 
                  (4, 6, 6, 3, 2, 1, 1, 2), (1, 3, 2, 7, 6, 3, 3, 0), (4, 7, 6, 3, 2, 2, 7, 5), (3, 0, 1, 1, 6, 5, 2, 5), 
                  (2, 3, 1, 7, 6, 4, 4, 6), (3, 5, 3, 2, 5, 6, 2, 6), (1, 5, 4, 4, 0, 0, 4, 7), (5, 5, 7, 1, 3, 3, 0, 7), 
                  (6, 1, 6, 6, 2, 4, 1, 5), (3, 3, 3, 1, 1, 6, 0, 1), (6, 7, 5, 3, 0, 1, 1, 5), (4, 4, 2, 5, 2, 3, 4, 4), 
                  (6, 7, 6, 7, 3, 7, 2, 4), (0, 6, 0, 6, 4, 4, 1, 1), (4, 5, 4, 1, 1, 2, 0, 3), (4, 0, 3, 0, 1, 5, 1, 5), 
                  (6, 1, 0, 4, 6, 4, 1, 6), (4, 2, 4, 2, 5, 1, 6, 7)] 
    m_rate = 0.9943
    best_individual, num_iters = genetic_algorithm(population, m_rate=m_rate, max_iters=3000)
    print('Best individual: {}'.format(best_individual))
    print('Best individual fitness: {}'.format(fitness(best_individual)))
    print('Best individual is_goal?: {}'.format(is_goal(best_individual)))
    print('# iterations: {}'.format(num_iters)) 
    print('______________________________________________________________') 
    
    ####
    rand_seed=2141111
    np.random.seed(rand_seed)
    population= [(4, 5, 1, 4, 4, 3, 2, 3), (4, 1, 3, 2, 2, 7, 4, 0), (7, 6, 2, 7, 7, 2, 7, 4), (1, 3, 3, 6, 4, 0, 2, 3), 
                  (5, 1, 2, 3, 6, 7, 2, 3), (2, 1, 0, 0, 1, 4, 5, 2), (0, 4, 0, 3, 0, 4, 1, 0), (2, 7, 3, 2, 0, 2, 3, 2), 
                  (4, 7, 4, 6, 2, 1, 0, 2), (2, 4, 7, 1, 1, 7, 6, 6), (3, 2, 2, 3, 4, 1, 7, 0), (4, 7, 7, 0, 3, 2, 4, 3), 
                  (4, 6, 6, 3, 2, 1, 1, 2), (1, 3, 2, 7, 6, 3, 3, 0), (4, 7, 6, 3, 2, 2, 7, 5), (3, 0, 1, 1, 6, 5, 2, 5), 
                  (2, 3, 1, 7, 6, 4, 4, 6), (3, 5, 3, 2, 5, 6, 2, 6), (1, 5, 4, 4, 0, 0, 4, 7), (5, 5, 7, 1, 3, 3, 0, 7), 
                  (6, 1, 6, 6, 2, 4, 1, 5), (3, 3, 3, 1, 1, 6, 0, 1), (6, 7, 5, 3, 0, 1, 1, 5), (4, 4, 2, 5, 2, 3, 4, 4), 
                  (6, 7, 6, 7, 3, 7, 2, 4), (0, 6, 0, 6, 4, 4, 1, 1), (4, 5, 4, 1, 1, 2, 0, 3), (4, 0, 3, 0, 1, 5, 1, 5), 
                  (6, 1, 0, 4, 6, 4, 1, 6), (4, 2, 4, 2, 5, 1, 6, 7)] 
    m_rate = 0.9943
    best_individual, num_iters = genetic_algorithm(population, m_rate=m_rate, max_iters=3000)
    print('Best individual: {}'.format(best_individual))
    print('Best individual fitness: {}'.format(fitness(best_individual)))
    print('Best individual is_goal?: {}'.format(is_goal(best_individual)))
    print('# iterations: {}'.format(num_iters)) 