import csv
from pprint import pprint as pprint
import pandas as pd
from random import uniform

errorCount = 0
successCount = 0
totalCount = 0

class MaxValues(object):
    area = 0
    perimeter = 0
    compactness = 0
    length = 0
    width = 0
    asymmetryCoefficient = 0
    lengthGroove = 0

# Normalizes the data by dividing each data point in each column by the columns max value
def normalizeData(maxVals, df):
    df['Area']                  = df['Area'] / maxVals.area
    df['Perimeter']             = df['Perimeter'] / maxVals.perimeter
    df['Compactness']           = df['Compactness'] / maxVals.compactness
    df['Length']                = df['Length'] / maxVals.length
    df['Width']                 = df['Width'] / maxVals.width
    df['AsymmetryCoefficient']  = df['AsymmetryCoefficient'] / maxVals.asymmetryCoefficient
    df['LengthGroove']          = df['LengthGroove'] / maxVals.lengthGroove
    return df

def importCSV(filename):
    df = pd.read_csv(filename)
    maxVals = MaxValues()
    maxVals.area                    = max(df['Area'])
    maxVals.perimeter               = max(df['Perimeter'])
    maxVals.compactness             = max(df['Compactness'])
    maxVals.length                  = max(df['Length'])
    maxVals.width                   = max(df['Width'])
    maxVals.asymmetryCoefficient    = max(df['AsymmetryCoefficient'])
    maxVals.lengthGroove            = max(df['LengthGroove'])

    return normalizeData(maxVals, df)

# Calculates the activation value for the neuron
def calculateActivationValue(values, weights):
    activationValue = 0
    for i in range(len(values)):
        activationValue += values[i] * weights[i]

    return activationValue


def calculateNewWeights(neuron, expectedOutput):
    learningRate = 0.5
    outputDifference = int(expectedOutput) - int(neuron.output)
    neuron.weightBias                   = neuron.weightBias + outputDifference * learningRate * neuron.bias
    neuron.weightArea                   = neuron.weightArea + outputDifference * learningRate * neuron.area
    neuron.weightPerimeter              = neuron.weightPerimeter + outputDifference * learningRate * neuron.perimeter
    neuron.weightCompactness            = neuron.weightCompactness + outputDifference * learningRate * neuron.compactness
    neuron.weightLength                 = neuron.weightLength + outputDifference * learningRate * neuron.length
    neuron.weightWidth                  = neuron.weightWidth + outputDifference * learningRate * neuron.width
    neuron.weightAsymmetryCoefficient   = neuron.weightAsymmetryCoefficient + outputDifference * learningRate * neuron.asymmetryCoefficient
    neuron.weightLengthGroove           = neuron.weightLengthGroove + outputDifference * learningRate * neuron.lengthGroove

    return neuron

# Retrieves data from row
def parseRow(row):
    values = []
    values.append(float(row[1][1]))
    values.append(float(row[1][2]))
    values.append(float(row[1][3]))
    values.append(float(row[1][4]))
    values.append(float(row[1][5]))
    values.append(float(row[1][6]))
    values.append(float(row[1][7]))

    return values

def main():
    df = importCSV('trainSeeds.csv')

    weights1 = []
    weights2 = []
    weights1 = [uniform(-1, 1) for _ in range(8)]
    weights2 = [uniform(-1, 1) for _ in range(8)]
    
    for i in range(0, 1):    
        # Iterate over dataframe row
        for row in df.iterrows():

            values = parseRow(row)
            act1 = calculateActivationValue(values, weights1)
            act2 = calculateActivationValue(values, weights2)

            # expectedOutputBinary = format(int(expectedOutput), '02b')
            
            # If the expectedOutput first bit is equal to the output of the first node
            # if int(expectedOutputBinary[0]) != neuron1.output:
                # errorNeuron1.append((neuron1.activationValue, int(expectedOutputBinary[0]), row))
            
            # If the expectedOutput second bit is equal to the output of the second node
            # if int(expectedOutputBinary[1]) != neuron2.output:
            #     errorNeuron2.append((neuron2.activationValue, int(expectedOutputBinary[1]), row))

            # if int(expectedOutputBinary[0]) != neuron1.output or int(expectedOutputBinary[1]) != neuron2.output:
            #     errorCount += 1

            # totalCount += 1

        # print("Success rate: ", (float(totalCount) - float(errorCount)) / float(totalCount))
        # List not empty
        # if errorNeuron1:
        #     errorNeuron1.sort(key=lambda tup: abs(tup[0]))  # sorts in place
        #     print(neuron1.area)
        #     neuron1 = parseRow(neuron1, errorNeuron1[0][2])
        #     print(neuron1.area)
        #     print("----------------------")
        #     neuron1 = calculateNewWeights(neuron1, errorNeuron1[0][1])

        # if errorNeuron2:
        #     errorNeuron2.sort(key=lambda tup: abs(tup[0]))  # sorts in place
        #     neuron2 = parseRow(neuron2, errorNeuron2[0][2])
        #     neuron2 = calculateNewWeights(neuron2, errorNeuron2[0][1])

        # errorNeuron1 = []
        # errorNeuron2 = []

    df = importCSV('testSeeds.csv')

    # successTestCount = 0
    # errorTestCount = 0

    # countZeroOne = 0
    # countOneZero = 0
    # countOneOne = 0

    # for row in df.iterrows():
    #     neuron1.area = row[1][0]
    #     neuron1.perimeter = row[1][1]
    #     neuron1.compactness = row[1][2]
    #     neuron1.length = row[1][3]
    #     neuron1.width = row[1][4]
    #     neuron1.asymmetryCoefficient = row[1][5]
    #     neuron1.lengthGroove = row[1][6]
    #     expectedOutput = int(row[1][7])

    #     neuron1.output = calculateOutput(neuron1)

    #     if neuron1.output > 0:
    #         neuron1.output = "1"
    #     else:
    #         neuron1.output = "0"

    #     neuron2.area = row[1][0]
    #     neuron2.perimeter = row[1][1]
    #     neuron2.compactness = row[1][2]
    #     neuron2.length = row[1][3]
    #     neuron2.width = row[1][4]
    #     neuron2.asymmetryCoefficient = row[1][5]
    #     neuron2.lengthGroove = row[1][6]

    #     neuron2.output = calculateOutput(neuron2)

    #     if neuron2.output > 0:
    #         neuron2.output = "1"
    #     else:
    #         neuron2.output = "0"

    #     combinedOutputBinary = neuron1.output + neuron2.output    
    #     # print(combinedOutputBinary)
    #     combinedOutput = 0
    #     if combinedOutputBinary == "01":
    #         countZeroOne += 1
    #         # print("in 01")
    #         combinedOutput = 1
    #     elif combinedOutputBinary == "10":
    #         countOneZero += 1
    #         # print("in 10")
    #         combinedOutput = 2
    #     elif combinedOutputBinary == "11":
    #         countOneOne += 1
    #         # print("in 11")
    #         combinedOutput = 3
        
    #     if expectedOutput == combinedOutput:
    #         successTestCount += 1
    #     else:
    #         errorTestCount += 1
    # print("===================================================")
    # print("Success: ", successTestCount)
    # print("Error: ", errorTestCount)
    # print("01: ", countZeroOne)
    # print("10: ", countOneZero)
    # print("11: ", countOneOne)
    # print("Success rate: ", float(successTestCount) / (successTestCount + errorTestCount))
    # print("Success Rate: ", successRate)
main()