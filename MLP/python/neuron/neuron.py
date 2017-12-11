import random
import math

class Neuron():
    learningRate = 0.1

    def __init__(self, nInputs):

        self.nInputs = nInputs

        self.weights = [None] * nInputs + 1
        self.inputs = [None] * nInputs

        self.output = None

        for i in range(nInputs):
            self.weights = random.random()

        print(round( self.weights,4))

    @staticmethod
    def setLearningRate(lr):
        Neuron.learningRate = lr

    @staticmethod
    def sigmoid(x):
       return (1/(1+math.exp(-x)))

    def getOutput(self):
        sum = self.weights[0] * 1

        for i in range(self.nInputs):
            sum += self.weights[i + 1] * self.inputs[i]

        self.output = Neuron.sigmoid(sum)
        return self.output

    def setInput(self, inputVector):
        if(len(inputVector) != self.nInputs ):
            raise Exception('Number of inputs doesnt correspond to ' + self.nInputs, inputVector )

        self.inputs = inputVector