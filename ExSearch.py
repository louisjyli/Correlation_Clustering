__author__ = 'louisjyli'
from collections import Counter
n = 3
k_upper = 2
k_lower = 1
k = int(n/k_lower)
if n % k != 0:
    k = k + 1
else:
    a = 0

result = [0]*n
minCost = n**2+1
E = set()
E.add(str(1)+' '+str(0))
E.add(str(2)+' '+str(0))
E.add(str(2)+' '+str(1))

for i in range(k**n):
    if i >= 1:
        result[0] += 1
        for j in range(len(result)):
            if result[j] == k:
                result[j] = 0
                result[j+1] += 1
            else:
                a = 0
        counts = Counter(result)
        skip = 0
        for cluster in counts:
            if counts[cluster] > k_upper:
                skip = 1
            elif counts[cluster] < k_lower:
                skip = 1
            else:
                a = 0
        if skip == 0:
            cost = 0
            for source in range(n):
                for dest in range(source,n):
                    if str(source)+' '+str(dest) not in E and str(dest)+' '+str(source) not in E:
                        if source != dest and result[source] == result[dest]:
                            cost += 1
                        else:
                            a = 0
                    elif str(source)+' '+str(dest) in E or str(dest)+' '+str(source) in E:
                        if source != dest and result[source] != result[dest]:
                            cost += 1
                        else:
                            a=0
                    else:
                        a = 0
        else:
            cost = -1
        for p in result:
                print(p)
        print('C='+str(cost))
        input()
        if cost < minCost and cost >= 0:
            minCost = cost
        else:
            a = 0
    else:
        counts = Counter(result)
        skip=0
        for cluster in counts:
            if counts[cluster] > k_upper:
                skip = 1
            elif counts[cluster] < k_lower:
                skip = 1
            else:
                a = 0
        if skip == 0:
            cost = 0
            for source in range(n):
                for dest in range(source,n):
                    if str(source)+' '+str(dest) not in E and str(dest)+' '+str(source) not in E:
                        if source != dest and result[source] == result[dest]:
                            cost += 1
                        else:
                            a = 0
                    elif str(source)+' '+str(dest) in E or str(dest)+' '+str(source) in E:
                        if source != dest and result[source] != result[dest]:
                            cost += 1
                        else:
                            a = 0
                    else:
                        a = 0
        else:
            cost = -1
        for p in result:
                print(p)
        print('C='+str(cost))
        input()
        if cost < minCost and cost >= 0:
            minCost = cost
        else:
            a = 0
print(minCost)