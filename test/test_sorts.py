count = 0

def bubbleSort(A, l, r):
    for i in range(l,r):
        for j in range(r-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

def insertionSort(A, l, r):
    for i in range(l+1,r):
        j = i-1
        while j >= 0 and A[j] > A[j+1]:
            swap(A, j, j+1)
            j -= 1

def swap(A, i, j):
  """Exchange the elements of A at positions i and j."""
  global count
  count += 1
  A[i], A[j] = A[j], A[i]

if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #bubbleSort(arr, 0, len(arr))
    insertionSort(arr, 0, len(arr))
    
    print(count)