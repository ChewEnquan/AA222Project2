
'''
Note: Do not import any other modules here.
        To import from another file xyz.py here, type
        import project1_py.xyz
        However, do not import any modules except numpy in those files.
        It's ok to import modules only in files that are
        not imported here (e.g. for your plotting code).
'''
import numpy as np
from convenience import plot_contour # Credit to Griffin
import matplotlib.pyplot as plt
from project2 import optimize
from helpers import Simple1 
from helpers import Simple2 
from helpers import Simple3 
    
def main():
    
    # Simple 1

    plot_contour(plt.figure(),Simple1ObjectiveFunction,[-2.2,2.2],[-2.2,2.2],0.1,0.1,10,0,1)   
    InitialValue = np.array([[-2,-2], [0.5,0.5], [2,2]])
    
    for initialx in InitialValue:
        p = Simple1()
        #xhistory = optimize(p.f, p.g, p.c, initialx , p.n, p.count, p.prob)
        xhistory = optimize(p.f, p.g, p.c, initialx , 2000 , p.count, p.prob)
        #print(xhistory)
        plt.plot(xhistory[:,0],xhistory[:,1],marker=".")
    
    x2constraint = np.linspace(((1/2)-np.sqrt(5)/2),((1/2)+np.sqrt(5)/2),100)
    x1constraint1 = 1 - x2constraint*x2constraint
    x1constraint2 = - x2constraint
    plt.plot(x1constraint1,x2constraint,color="r")
    plt.plot(x1constraint2,x2constraint,color="r")
    plt.plot((2/3),(1/np.sqrt(3)),marker='x')


    plt.legend(InitialValue,title = "Initial x0")    
    plt.title("Objective contour plot of Simple1 with feasible region contained within the red curves with path taken by algorithm from three different starting points")
    plt.show()

    #Simple 2

    plot_contour(plt.figure(),Simple2ObjectiveFunction,[-5.5,5.5],[-5.5,5.5],0.1,0.1,10,0,1)   
    InitialValue = np.array([[-5,-5], [5,0], [5,5]])
    
    for initialx in InitialValue:
        p = Simple2()
        #xhistory = optimize(p.f, p.g, p.c, initialx , p.n, p.count, p.prob)
        xhistory = optimize(p.f, p.g, p.c, initialx , 2000 , p.count, p.prob)
        #print(xhistory)
        plt.plot(xhistory[:,0],xhistory[:,1],marker=".")
    
    x1constraint = np.linspace(1,5.5,100)
    x2constraint1 = 1 + (x1constraint-1)**3
    x2constraint2 = 2 - x1constraint
    plt.xlim(-5.5,5.5)
    plt.ylim(-5.5,5.5)
    plt.plot(x1constraint,x2constraint1,color="r")
    plt.plot(x1constraint,x2constraint2,color="r")
    plt.plot((1),(1),marker='x')


    plt.legend(InitialValue,title = "Initial x0")    
    plt.title("Objective contour plot of Simple2 with feasible region (being to the left of the red curves) with path taken by algorithm from three different starting points")
    plt.show()

    #Convergence Plot (Simple2)

    InitialValue = np.array([[-5,-5], [5,0], [5,5]])
    
    for initialx in InitialValue:
        p = Simple2()
        xhistory = optimize(p.f, p.g, p.c, initialx ,160, p.count, p.prob)
        fhistory = np.zeros(len(xhistory))
        for x in range(len(xhistory)):
            fhistory[x] = p.f(xhistory[x])
        #print(fhistory)
        iteration_no = np.linspace(0,len(fhistory)-1,len(fhistory))
        plt.plot(iteration_no,fhistory)

    plt.xlabel("Iteration")
    plt.ylabel("Function Value")
    plt.legend(InitialValue,title = "Initial x0")    
    plt.title("Convergence Plot for Simple1")
    plt.show()

    #Violations Plot (Simple2)

    InitialValue = np.array([[-5,-5], [5,0], [5,5]])
    
    for initialx in InitialValue:
        p = Simple2()
        xhistory = optimize(p.f, p.g, p.c, initialx ,160, p.count, p.prob)
        violationhistory = np.zeros(len(xhistory))
        for x in range(len(xhistory)):
            C = p.c(xhistory[x])
            P = sum(C>0)
            violationhistory[x] = P
        #print(fhistory)
        iteration_no = np.linspace(0,len(violationhistory)-1,len(fhistory))
        plt.plot(iteration_no,violationhistory)

    plt.xlabel("Iteration")
    plt.ylabel("Number of Violations")
    plt.legend(InitialValue,title = "Initial x0")    
    plt.title("Violation Plot for Simple2")
    plt.show()

def Simple1ObjectiveFunction(x):
    return -x[0]*x[1]+(2/(3*np.sqrt(3)))

def Simple2ObjectiveFunction(x):
    return 100*(x[1]-x[0]**2)**2 + (1-x[0])**2
    
if __name__ == "__main__":
    main() 
## Need these 2 lines of code above main to run - Python Syntax