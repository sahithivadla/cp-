"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def q(array,low,high):
	if low < high:
		pi = partition(array,low,high)
		q(array, low, pi-1)
		q(array, pi+1, high)

def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if   array[j] < pivot:
            i = i+1
            array[i],array[j] = array[j],array[i]

    array[i+1],array[high] = array[high],array[i+1]
    return ( i+1 )

def quicksort(array):
	# Your code goes here
	a = q(array,0,len(array)-1)
	return (a)