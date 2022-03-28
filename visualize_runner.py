from local_search import *
if __name__ == "__main__":
    # visualize solution
    n_queens_sol = (0,4,7,5,2,6,1,3)
    visualize_nqueens_solution(n_queens_sol, './nqueens1.png')
    plt.close()
    
    n_queens = (0,1,1,1,1,1,1,0)
    visualize_nqueens_solution(n_queens, './nqueens2.png')
    plt.close()