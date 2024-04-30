def rearrange_list(lst, start_index):
    n = len(lst)
    rearranged_list = [lst[(start_index + i) % n] for i in range(0, n)]
    return rearranged_list


N = int(input())
A = list(map(int, input().split()))
angles = [360]
for i in range(N):
    current_angle = 0
    for j in range(i + 1):
        current_angle += angles[j]
        if current_angle > A[i]:
            angles[j] = current_angle - A[i]
            angles = rearrange_list(angles, j)
            angles.append(360 - sum(angles))
            break
print(max(angles))
