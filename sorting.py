# General sorting functions
import pylab
import os



# Auxiliar Functions

def isSorted(data):
    """ Returns true if the data is sorted in increasing order. """
    return all( data[i] <= data[i+1] for i in range(len(data)-1) )    



def genData(length=100, maximum=100):
    """ Generates random data given length and maximum. """
    from random import randint
    data = [randint(0,maximum) for i in range(length)]
    return data



def testAlgorithm(algorithm, number=100, length=100, maximum=100):
    """ Tests an algorithm with a number of random inputs. """
    for i in range(number):
        original_data = genData(length,maximum)
        sorted_data = algorithm(original_data)
        if not isSorted(sorted_data):
            print "Error! A counterexample was found!"
            print sorted_data
            return False
    return True



# Plotting functions

class Plotter:
    """ Data visualizer. """

    def __init__(self, data, folder="./", step=0):
        self.folder = folder
        self.step = step
        self.data = data

    def snapshot(self):
        """ Plots the current data. """
        pylab.plot(range(len(self.data)),self.data,'k.',markersize=6)
        pylab.savefig(self.folder + "plot" + '%04d' % self.step + ".png")
        pylab.clf()
        self.step = self.step+1

    def end(self):
        """ Creates the video. """
        os.system("cd " + self.folder)
        os.system("avconv -qscale 5 -r 20 -b 9600 -i plot%04d.png movie.mp4")
        os.system("rm plot????.png")