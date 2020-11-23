# Generating new sequences

Within the proof for the expression for the number of permutations that was explained in the video the procedure that you just performed needed to be completed for multiple lists.  In this exercise, the function `allseq` thus takes a list of lists of distinguishable symbols of length `n-1` in input called `inseq`.  Your task is to use what you have learned to generate all the lists of length `n` that can be constructed by inserting the new symbol a into each of the input lists.  To get you started I have written a loop over all the input lists in this line:

````
for seq in inseq
```` 
 
Within this loop, you can treat the variable `seq`  as a list of `n-1` distinguishable symbols just as you did in the previous exercise.  You can thus write code within the loop to append all the various possible sequences into the list of lists that is returned, which is called `final_seq`.

Notice that if your code is working correctly the final print command:

````
print( allseq( [[1,2],[2,1]], 3 ) )
````

should output the following:

````
[ [3,1,2], [1,3,2], [1,2,3], [3,2,1], [2,3,1], [2,1,3] ]
````
