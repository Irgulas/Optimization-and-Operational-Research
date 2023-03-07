import matplotlib.pyplot as plt
import timeit
 
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle

# JVF: maxsize not defined

    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path
 
L=[]
Time = []
for j in range (5):
    V = j


    start = timeit.default_timer()
    if __name__ == "__main__":
 
    # matrix representation of graph
        graph = [[0, 10, 15, 20], [10, 0, 35, 25],
                 [15, 35, 0, 30], [20, 25, 30, 0]]
        s = 0
        print(travellingSalesmanProblem(graph, s))
    end = timeit.default_timer()
    elapsed = end - start
    L.append(elapsed)
    Time.append(j)
plt.plot(Time,L)
plt.show
