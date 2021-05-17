from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figureCanvas
from graphviz import Digraph

def makeFigure(layout):
    fig = Figure()
    canvas = figureCanvas(fig)
    layout.addWidget(canvas)
    canvas.draw()
    return fig
def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):
    """In-place bubble sort."""

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def insertionSort(A):
    # Traverse through 1 to len(arr)
    for i in range(1, len(A)):

        key = A[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        yield A


def mergesort(A, start, end):
    """Merge sort."""

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


def merge(A, start, mid, end):
    """Helper function for merge sort."""

    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A



def quicksort(A, start, end):
    """In-place quicksort."""

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


def selectionsort(A):
    """In-place selection sort."""
    if len(A) == 1:
        return

    for i in range(len(A)):
        # Find minimum unsorted value.
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A

def bubblesortNoAnim(A):
    if len(A) == 1:
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
    return (A)


def insertionSortNoAnim(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSortNoAnime(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSortNoAnime(L)  # Sorting the first half
        mergeSortNoAnime(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSortNoAnime(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSortNoAnime(arr, low, pi - 1)
        quickSortNoAnime(arr, pi + 1, high)
    return arr

def selectionSortNoAnime(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


class node():
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inorder(root, res, tr):
    # Recursive travesal
    if root:
        tr[root.val] = []
        if (root.left):
            tr[root.val].append(root.left.val)
        else:
            tr[root.val].append("None")
        if (root.right):
            tr[root.val].append(root.right.val)
        else:
            tr[root.val].append("None")
        inorder(root.left, res, tr)
        res.append(root.val)
        inorder(root.right, res, tr)


def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []

    tr = dict()
    inorder(root, res, tr)
    f = open("test.txt", "w")
    for i in tr:
        for j in tr[i]:
            f.write("{} {}".format(i, j))
            f.write("\n")
    return (res, tr)


def createGraph(tr):
    g = Digraph("Graph", format='png')
    for i in tr:
        if (tr[i][0] != "None"):
            g.edge(str(i), str(tr[i][0]), label="Left", color="blue")

        if (tr[i][1] != "None"):
            g.edge(str(i), str(tr[i][1]), label="Right", color="red")

    g.render()