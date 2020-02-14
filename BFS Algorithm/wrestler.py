from collections import defaultdict

# User can change this field
filename = 'wrestler1.txt'


def readInFile(filename):
    d = defaultdict(set)
    key = []
    inFile = open(filename, "r")
    n = int(inFile.readline())
    for i, line in enumerate(inFile):
        if i < n:
            key.append(line.strip())
        elif i == n:
            j = int(line) + i
        elif i > n and i <= j:
            arr = line.strip().split(" ")
            d[arr[0]].add(arr[1])
            d[arr[1]].add(arr[0])
    return d, key


def bfs(graph, start, B, H, NoSol):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            i = j = 0
            if len(B) == 0:
                B.append(vertex)
            else:
                for v in B:
                    if vertex in graph[v]:
                        i = 1
                        break
                if i == 0:
                    B.append(vertex)
                else:
                    if len(H) == 0:
                        H.append(vertex)
                    else:
                        for v in H:
                            if vertex in graph[v]:
                                j = 1
                                break
                        if j == 0:
                            H.append(vertex)
                        else:
                            NoSol.append(vertex)
    return visited


if __name__ == '__main__':
    d, key = readInFile(filename)
    B = []
    H = []
    NoSol = []
    visited = bfs(d, key[0], B, H, NoSol) # {'B', 'C', 'A', 'F', 'D', 'E'}

    if len(NoSol) != 0:
        print("No Solution")

    else:
        for item in key:
            if item not in visited:
                visited = visited.union(bfs(d, item, B, H, NoSol))
        if len(NoSol) != 0:
            print("No Solution")
        else:
            print("Yes it is Possible")
            print("Babyfaces: "),
            for b in B:
                print(b),
            print(" ")
            print("Heelers: "),
            for h in H:
                print(h),
            print(" ")


