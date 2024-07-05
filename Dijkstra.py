# {'0':{'1':4,'7':8},'1':{'0':4,'7':11,'2':8},'2':{'1':8,'8':2,'5':4,'3':7},'3':{'2':7,'5':14,'4':9},'4':{'3':9,'5':10},'5':{'6':2,'2':4,'3':14,'4':10},'6':{'8':6,'7':1,'5':2},'7':{'6':1,'8':7,'0':8,'1':11},'8':{'7':7,'6':6,'2':2}}

import networkx as nx
import matplotlib.pyplot as plt
import time

def main():
	print("\n1.Directed\n2.Undirected\n3.Exit\n")
	choice=int(input("Enter Your Choice : "))
	if choice==1:
		spots,graph=input_data()
		directed(spots,graph)
	elif choice==2:
		spots,graph=input_data()
		undirected(spots,graph)
	elif choice==3:
		print("Thank You")

def input_data():
	print("\nEnter The data and to stop write 'Quit'.\n")
	graph={}
	while True:
		data=input("Enter The Value:")
		if data.upper()=="QUIT":
			break
		else:
			graph[data]=0
	spots=list(graph.keys())

	return spots,graph

def undirected(spots,graph):
	G = nx.Graph() #For undirected graph.
	
	for i in graph:
		path={}
		print("\nTo stop write 'Quit'.\n")
		
		while True:
			print(f"Enter The Spot you want to connect for {i}:")
			data=input("Enter The Value:")
			if data.upper()=="QUIT":
				break
			else:
				G.add_node(data)
				if data in spots and i!=data:
					value=int(input("Enter the Weight:"))
					path[data]=value
					if graph[data] == 0:
						graph[data] = {i:value}
						G.add_edge(data, i, weight=value)
						G.add_edge(i, data, weight=value)
					else:
						graph[data][i]=value
				else:
					print("No spot of this Name")
					continue
		graph[i]=path
	labels = {node: node for node in G.nodes()}
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels=False, node_color='b', font_color='white', font_weight='bold')
	nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_weight='bold')
	nx.draw_networkx_edges(G, pos, alpha=0.5)
	nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()}, font_color='red', font_size=10)
	plt.show()
	finding_spot(graph)


def directed(spots,graph):
	G = nx.DiGraph() #For undirected graph.
	for i in graph:
		path={}
		print("\nTo stop write 'Quit'.\n")
		while True:
			print(f"Enter The Spot you want to connect for {i} : ")
			data=input("Enter The Spot:")
			if data.upper()=="QUIT":
				break
			else:
				G.add_node(i)
				if data in spots:
					value=int(input("Enter the Weight:"))
					path[data] = value
					G.add_edge(i, data, weight=value)
				else:
					print("No spot of this Name")
					continue
		graph[i]=path
	labels = {node: node for node in G.nodes()}
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels=False, node_color='b', font_color='white', font_weight='bold')
	nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_weight='bold')
	nx.draw_networkx_edges(G, pos, alpha=0.5,arrows=True)
	nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()}, font_color='red', font_size=10)
	plt.show()
	finding_spot(graph)

# graph1={'0':{'1':4,'7':8},'1':{'0':4,'7':11,'2':8},'2':{'1':8,'8':2,'5':4,'3':7},'3':{'2':7,'5':14,'4':9},'4':{'3':9,'5':10},'5':{'6':2,'2':4,'3':14,'4':10},'6':{'8':6,'7':1,'5':2},'7':{'6':1,'8':7,'0':8,'1':11},'8':{'7':7,'6':6,'2':2}}

def finding_spot(graph):
	while True:
		data=input("Name of the Spot for the Shortest Path:")
		if data in graph:
			shortest_path={}
			shortest_path[data]=graph[data]
			x=graph[data]
			for i in list(graph.keys()):
				if i not in shortest_path[data] and i!=data:
					x[i]=0
			shortest_path[data]=x
			start_time = time.time()

			# Execute your method
			find_dist(data,shortest_path,graph)

			# Calculate the runtime
			end_time = time.time()
			runtime = end_time - start_time
			print("\nRuntime(0.01 sec pause after each iteration in BFS) : ", runtime, "seconds\n")

			break
		else:
			print("No spot of this name.")

def find_dist(data,shortest_path,graph):
	
	check=[]
	
	y=shortest_path[data]

	for i in range(len(shortest_path[data])+1):
		min = 0
		for key,value in shortest_path[data].items():
			time.sleep(0.01)
			if ((value<=min and value != 0) or (min == 0)) and(key not in check):
				min=value
				min_spot=key
		
		check.append(min_spot)
		spots_data=graph[min_spot]
		
		if min!=0:
			for key,value in spots_data.items():
				if key!=data:
					if y[key]>value+min or y[key]==0:
						y[key]=value+min

			shortest_path[data]=y
	print(shortest_path)

# finding_spot(graph1)