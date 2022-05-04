
def cityprint():
    for arr in cities:
        for wt in arr:
            print("%4d"%wt, end = "")
        print("\n")

def routeprint():
    for i in range(len(route)-1):
        print(route[i],end = " -> ")
    print(route[i+1])
        
n = int(input("Enter number of cities: "))
cities = [[-1 for i in range(n)] for j in range(n)]
route = []
leastcost = 9999

print("\n** enter -1 for no direct route between the cities **\n")
for i in range(n):
    for j in range(i+1,n):
        dist = int(input("Enter distance from city #%d to city #%d : "%(i,j)))
        if dist != -1:
            cities[i][j] = cities[j][i] = dist
    print("\n")


for curr in range (n):
    visited = []
    cost = 0
    visited.append(curr)
    while(len(visited) < n):
        shortest_route = 999
        shortest_route_index = -999
        for i in range(n):
            if i not in visited:
                if cities[curr][i] < shortest_route:
                    shortest_route = cities[curr][i]
                    cost = cost + shortest_route
                    shortest_route_index = i
        curr = shortest_route_index
        visited.append(curr)

    if cities[curr][visited[0]] <= cost:
        visited.append(visited[0])
        cost = cost + cities[curr][visited[0]]
    else:
        for i in range(len(visited)-2,-1,-1):
            visited.append(visited[i])
            cost = 2*cost

    if cost < leastcost:
        route = visited.copy()
        leastcost = cost


routeprint()
print("Total cost: ",leastcost)
print("\nCity matrix:\n")
cityprint()
