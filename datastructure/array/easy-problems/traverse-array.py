#creat an array havingg number 1 to 5 and then print it by using for-loop 



def main():
    # Create an array with numbers 1 to 5
    numbers = [1, 2, 3, 4, 5]

    # Print each number using a for-loop
    for number in numbers:
        print(number)

# Call the main function
main()


### code to print the array in correct formate 

def main():
    
    def reverseArray (arr):
        left = 0                                             #initialize left to the beginning & right to the end
        right = len(arr)-1          

        while left < right:                                   #iterate till left is less than right
            arr[left], arr[right] = arr[right], arr[left]      #swap the  element at left to right
            left += 1                                         #increment the left pointer
            right -= 1                                        # decrement the right pointer
            if __name__ == "__main__":
                arr = [1,5,4,6,3,2]
                reverseArray(arr)
                for i in range(len(arr)):
                    print (arr[i], end="")

                    






