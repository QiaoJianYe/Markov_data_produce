# __author__ = "Kai Qi (QiaoJianYe)"
# __email___ = "upcqikai@hotmail.com"
# __time____ = "2020.09.15"

#This code simulate markov switching on a state space S, using initial distribution mu, sojourn parameters lam, and jump matrix Q.

#It can simulate a Stochastic Differnetial Equcations with markov switching

#Change the jump matrix Q and state space S to generate different kinds of data

import random  
import numpy as np
import math
import matplotlib.pyplot as plt

def rand_from_a_dis(p):
    '''given a distribution p, generates a random variable in 1, 2, ..., n given a distribution'''  

    u = random.uniform(0,1)
    i = 0
    s = p[0]

    while ((u>s) and (i<len(p))):
        i += 1
        s = s+p[i]

    return i

def Markov_generate():

    S=[1, 2, 3]    #state space
    T_max=1000    #maximum time

    mu = [0,0,1]    #initial distribution
    lam = [0.1, 0.1, 0.1]   #sojourn parameters 
    Q = np.array([[2/3,1/6,1/6], [1/4,1/2,1/4], [1/4,1/4,1/2]])     #jump matrix

    h = 0.002     #time step
    N = math.ceil( T_max/h )     #number of steps to take
    t = [0]
    y = np.zeros(N+1)

    T= [0]    #start times at 0

    x = [rand_from_a_dis(mu)]     #generate first x value (time 0, not time 1)
    i = 0
    k = 0 

    while (T[i] < T_max):

        T.append  (T[i]-(math.log(random.uniform(0,1))/lam[x[i]]) )    #generate exponential rv
        q = Q[x[i],:]
        q = q.reshape(-1)
        x.append(rand_from_a_dis(q))     #use Q to make state transitions
        i += 1
        k+=1


    for i in range(0,N):
        for j in range(0,k+1):
             if ((T[j]<=t[i])  and (t[i]<=T[j+1])):
              y[i] = S[x[j]]
        t.append(t[i]+h)

    y[N]=S[x[k]]

    plt.plot(t,  y )
    plt.ylim(-1, 5)
    plt.show()



if __name__ == '__main__':
    Markov_generate()

  