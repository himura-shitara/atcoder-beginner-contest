N, Q = map(int, input().split())
X = list(map(int, input().split()))
AB_list = []
VK_list = []


for _ in range(N - 1):
    A, B = map(int, input().split())
    AB_list.append((A, B))


for _ in range(Q):
    V, K = map(int, input().split())
    VK_list.append((V, K))


print(N, Q, X, AB_list, VK_list)
