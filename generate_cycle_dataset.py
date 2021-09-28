import networkx as nx
import pickle as pkl
import matplotlib.pyplot as plt
from tqdm import tqdm
N = 1000    #Number of nodes
p = 0.001   #Probability to choose an edge
num_data_points = 1000

data_points = []
cycles_metadata = []

for i in tqdm(range(num_data_points)):
    graph = nx.gnp_random_graph(N,p)
    n_cycles = len(nx.algorithms.cycles.cycle_basis(graph))
    edge_list = [[int(i.split(" ")[0]),int(i.split(" ")[1])] for i in nx.readwrite.edgelist.generate_edgelist(graph,data=False)]
    data_points.append((edge_list,n_cycles))
    cycles_metadata.append(n_cycles)

plt.hist(cycles_metadata)
plt.show()

with open("temp/data_points.pkl","wb") as fp:
    pkl.dump(data_points,fp)
