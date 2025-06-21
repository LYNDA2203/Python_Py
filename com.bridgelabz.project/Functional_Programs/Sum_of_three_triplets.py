def find_zero_sum_triplets(arr):
    n=len(arr)
    triplets = set()
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(i+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet=tuple(sorted((arr[i],arr[j],arr[k])))
                    triplets.add(triplet)
    return triplets

def main():
    n=int(input("Enter the number of integers (N):"))
    print(f"Enter the {n} integers:")
    arr = [int(input()) for _ in range(n)]
    
    result=find_zero_sum_triplets(arr)
    
    print(f"\nNumber of distinct triplets:{len(result)}")
    print("Distinct triplets the sum of 0:")
    for triplet in sorted(result):
        print(triplet)
    
if __name__ == "__main__":
    main()