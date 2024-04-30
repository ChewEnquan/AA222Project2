#
# File: project2.py
#

## top-level submission file

'''
Note: Do not import any other modules here.
        To import from another file xyz.py here, type
        import project2_py.xyz
        However, do not import any modules except numpy in those files.
        It's ok to import modules only in files that are
        not imported here (e.g. for your plotting code).
'''
import numpy as np


def optimize(f, g, c, x0, n, count, prob):

    a_original = 0.5
    a = a_original # Stepsize
    # epsilon = 0.01
    gamma = 0.5
    xlength = len(x0)
    rho = 10000
    currentx = x0
    currentC = c(currentx)
    
   
    # Version 2 of Penalty
    clength = len(currentC)
    P = 0
    for j in range(clength):
        if currentC[j]>0:
             P = P + currentC[j]**2
    currentf = f(currentx) + P*rho
    '''
    #Version 1 of Penalty
    P = np.sum(currentC>0)
    print(currentC>0)
    print(P)
    currentf = f(currentx) + P*rho 
     '''
    #if P == 0:
    #   return currentx
    

    while (count() < (n-xlength*4)):
      improvement = False
      bestx = currentx
      bestf = currentf
      for i in range(xlength):
            for sgn in [-1,1]:
                 xwithstep = currentx
                 xwithstep[i] = xwithstep[i] + sgn*a
                 Cwithstep = c(xwithstep)
                 
                 '''  
                 #Version 1
                 Pwithstep = np.sum(Cwithstep>0)
                 
                 '''
                 #Version 2
                 Pwithstep = 0
                 for j in range(clength):
                      if Cwithstep[j]>0:
                           Pwithstep = Pwithstep + Cwithstep[j]**2
                    

                 #if Pwithstep == 0: # x is Feasible
                 #     currentx = xwithstep
                 #     return currentx
                 fwithstep = f(xwithstep) + Pwithstep*rho
                 if fwithstep<bestf:
                      bestx = xwithstep
                      bestf = fwithstep
                      improvement = True
      currentx = bestx
      currentf = bestf
      if not improvement:
            a = a*gamma
      #else:
      #     a = a_original
      
    return currentx


    """
    Args:
        f (function): Function to be optimized
        g (function): Gradient function for `f`
        c (function): Function evaluating constraints
        x0 (np.array): Initial position to start from
        n (int): Number of evaluations allowed. Remember `f` and `c` cost 1 and `g` costs 2
        count (function): takes no arguments are reutrns current count
        prob (str): Name of the problem. So you can use a different strategy 
                 for each problem. `prob` can be `simple1`,`simple2`,`simple3`,
                 `secret1` or `secret2`
    Returns:
        x_best (np.array): best selection of variables found
    """