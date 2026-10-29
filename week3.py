graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
#DLS
def dls(graph, node, goal, limit, path=None, depth=0):
    if path is None:
        path = []
    if node == goal:
        return "FOUND", path + [node]
    if node in path:
        return "FAILURE", None
    path = path + [node]
    if depth == limit:
        for child in graph[node]:
            if child not in path:
                return "CUTOFF", None
        return "FAILURE", None

    cutoff_found = False

    for child in graph[node]:
        status, result = dls(
            graph, child, goal, limit, path, depth + 1
        )
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff_found = True
    if cutoff_found:
        return "CUTOFF", None
    return "FAILURE", None
#IDDF
def iddf(start, goal, maximum):
    attempts = []

    for limit in range(maximum + 1):
        status, path = dls(graph, start, goal, limit)
        attempts.append(limit)

        if status == "FOUND":
            return status, path, attempts

        if status == "FAILURE":
            return status, None, attempts

    return "CUTOFF", None, attempts
print("\n_____DFS TEST_____")
for limit in [1, 2, 3, 4]:
    status, path = dls(graph, "A", "G", limit)
    print(f"LIMIT: {limit}: {status}, Path: {path}")
    
    print("\n ______IDDF Test_____")
for maximum in[1,2,3,4]:
    print(f"\nmaximum depth:{maximum}")
    status,path,attempts = iddf("A","G",maximum)
    print("Final result:", status)
    print("Final path:", path)
    print("Limits attempted:", attempts)

        


