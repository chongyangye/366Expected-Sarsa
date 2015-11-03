import blackjack
from pylab import *
from random import *

numEpisodes = 2000

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G =0
    black = blackjack.init()
    action =[0,1]
    while black!=-1:
        num = randint(0,1)
        n,black = blackjack.sample(black,action[num])
        
        G+=n

    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes