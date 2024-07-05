# Depth first search in a graph

class Node:
    visited = False
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def flag(self,flag):
        self.visited = flag

class Main:
    
    def dfs(n):  
        if n.visited :
            return
        print(n.name,'--' ,end = '' ,sep = '') # prints the Node n.
        n.visited = True
        for neighbour in n.neighbors:  # visits first neighbour of Node n followed by the next neighbour,if not visited.
            Main.dfs(neighbour)

    def main():
        nA = Node('A')
        nB = Node('B')
        nC = Node('C')
        nD = Node('D')
        nE = Node('E')
        nF = Node('F')
        nA.add_neighbor(nB)
        nA.add_neighbor(nC)
        nB.add_neighbor(nD)
        nC.add_neighbor(nD)
        nC.add_neighbor(nE)
        nD.add_neighbor(nF)
        Main.dfs(nA)
        # Depth first search in a graph
Main.main()
