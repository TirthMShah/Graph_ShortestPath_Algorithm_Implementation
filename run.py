import BFS_directed,BFS_undirected,Dijkstra
def main():
    print(f'\x1b\n[1m {" "*10}Shortest Path Algorithms.')
    while True:
        print('''
              
1.Find shortest path using BFS(unweighted graph).
2.Find shortest path using Dijkstra's Algorithm(weighted graph).
3.Exit.
              
''')
        choice = input("Enter your choice : ")

        if choice == '1':
            print('''
                
1.Directed graph.
2.Undirected graph.
                
''')
            choice = input("Enter your choice : ")
            
            if choice == '1':
                BFS_directed.main()
            elif choice == '2':
                BFS_undirected.main()
            else:
                print("Invalid choice.")
                continue

        elif choice == '2':
            Dijkstra.main()
        elif choice == '3':
            print("Thank You!!\n")
            return
        else:
            print("Enter a valid choice.")

main()