def allseq( inseq, a ) : 
  final_seq = [] 
  n = len(inseq[0])+1
  # This does a loop over all the lists in inseq.
  for seq in inseq : 
    # Within here you now need to generate all the possible lists 
    # that can be created from the list of length n-1 called seq by inserting 
    # the symbol a into the n possible positions it can be inserted in this list.
    # Each of these new sequences needs to be appended to final_seq.
  
  return final_seq
  

# This tests the code that you have written by printing out the sequences that 
# you have generated as discussed in the description on the right
print( allseq( [[1,2],[2,1]], 3 ) )
