



### code to print the array in correct formate 

    
def reverseArray (arr):
        left = 0                                             #initialize left to the beginning & right to the end
        right = len(arr)-1          

        while left < right:                                   #iterate till left is less than right
            arr[left], arr[right] = arr[right], arr[left]      #swap the  element at left to right
            left += 1                                         #increment the left pointer
            right -= 1                                        # decrement the right pointer

            if __name__ == "__main__":
                arr = [1,5,4,6,3,2]                            #sample array

                reverseArray(arr)                              #call the function to reverse the array

                # print the reversed array in correct format
                for i in range(len(arr)):
                    print(arr[i], end=" ")




                    print ("Hello there !!!")
                    



