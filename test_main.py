import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sequence(self) :
        inseq = [[1]]
        for i in range(1,5) : 
          newseq = allseq( inseq, i+1 )
          self.assertTrue( len(newseq)==np.math.factorial(i+1), "Your code is not generating all the lists it should" )
          for seq in newseq : self.assertTrue( len(seq)==i+1, "Your code is not generating all the lists it should" )
          for seq in inseq :
              n = len(seq)+1
              for j in range(n) :
                 nseq = n*[0] 
                 nseq[j] = i+1
                 for k in range(n-1) : 
                     if k>=j : nseq[k+1] = seq[k] 
                     else : nseq[k] = seq[k]
                 found=False
                 for oseq in newseq : 
                   isseq=True 
                   for k in range(len(oseq)) : 
                     if oseq[k]!=nseq[k] : isseq=False
                   if isseq : 
                      found=True
                      break
                   self.assertTrue( found, "Your code is not generating all the lists it should" )
          inseq = newseq 
