import blackjack
from pylab import *
import random

numEpisodes = 2000

returnSum = 0.0
for episodeNum in range(numEpisodes):
    G =0
    black = blackjack.init()
    action =[0,1]
    num=0
    while black!=-1:
    	n,black = blackjack.sample(black,action[num])
    	num = random.randint(0,1)
    	G+=n

    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes