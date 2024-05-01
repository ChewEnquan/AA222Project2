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
from scipy.stats import rv_continuous, multivariate_normal

def optimize(f, g, c, x0, n, count, prob):

    x_history = [] # For Plotting Purposes
    x_history.append(x0) # For Plotting Purposes
    
    methodused = "One"

    if methodused == "One":
        a = 1
        gamma = 0.5
        xlength = len(x0)
        rho = 10000
        currentx = x0
        currentC = c(currentx)
    
        '''
        #Version 1 of Penalty
        P = np.sum(currentC>0)
        currentf = f(currentx) + P*rho 
        '''

        # Version 2 of Penalty
        clength = len(currentC)
        P = 0
        for j in range(clength):
            if currentC[j]>0:
                P = P + currentC[j]
        currentf = f(currentx) + P*rho

        while count() < (n-xlength*4):
            improvement = False
            bestx = currentx
            bestf = currentf
            for i in range(xlength):
                    for sgn in [-1,1]:
                        xwithstep = currentx.copy()
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
                                Pwithstep = Pwithstep + Cwithstep[j]

                        fwithstep = f(xwithstep) + Pwithstep*rho
                        if fwithstep<bestf:
                            bestx = xwithstep
                            bestf = fwithstep
                            improvement = True
            currentx = bestx
            currentf = bestf
            x_history = np.append(x_history,[currentx],axis=0)
            if not improvement:
                    a = a*gamma

    if methodused == "Two":
        m = 101
        m_elite = 10
        def newf(x):
            rho = 10000
            return f(x)+rho*np.sum([max(0, _) for _ in c(x)]) #List comprehension _ is a dummy variable (only symbol that you can use as dummy variable)
        mean = x0
        cov = np.eye(len(x0))
        
        while count() < int((n//(2*m)))*(2*m):
            samples = np.random.multivariate_normal(mean,cov,m)
            order = np.argsort(np.apply_along_axis(newf, 1, samples))
            elitesamples = (samples[order[:m_elite]])
            mean = np.mean(elitesamples,axis=0)
            cov = np.cov(elitesamples,rowvar=False)
            x_history = np.append(x_history,[mean],axis=0)

        currentx = mean
    
    print(x_history)
    #return currentx
    return x_history


