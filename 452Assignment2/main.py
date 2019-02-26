import csv
import pandas as pd
import numpy as np
from random import uniform
from random import randint

numInputNodes = 9
numOutputNodes = 6  # 6 types of glass
numHiddenLayers = 1
numHiddenNodes = 0

successCount = 0
totalCount = 0

# Object to store the max values from each column
class MaxValues(object):
    refractiveIndex = 0
    sodium = 0
    magnesium = 0
    aluminium = 0
    silicon = 0
    potassium = 0
    calcium = 0
    barium = 0
    iron = 0
    
# Normalizes the data by dividing each data point in each column by the columns max value
def normalizeData(maxVals, df):
    df['Refractive_Index']  = df['Refractive_Index'] / maxVals.refractiveIndex
    df['Sodium']            = df['Sodium'] / maxVals.sodium
    df['Magnesium']         = df['Magnesium'] / maxVals.magnesium
    df['Aluminium']         = df['Aluminium'] / maxVals.aluminium
    df['Silicon']           = df['Silicon'] / maxVals.silicon
    df['Potassium']         = df['Potassium'] / maxVals.potassium
    df['Calcium']           = df['Calcium'] / maxVals.calcium
    df['Barium']            = df['Barium'] / maxVals.barium
    df['Iron']              = df['Iron'] / maxVals.iron

    return df

# Used column headers to easily import the data in columns for more efficient normalizing
def importCSV(filename):
    df = pd.read_csv(filename)

    maxVals = MaxValues()
    maxVals.refractiveIndex = max(df['Refractive_Index'])
    maxVals.sodium          = max(df['Sodium'])
    maxVals.magnesium       = max(df['Magnesium'])
    maxVals.aluminium       = max(df['Aluminium'])
    maxVals.silicon         = max(df['Silicon'])
    maxVals.potassium       = max(df['Potassium'])
    maxVals.calcium         = max(df['Calcium'])
    maxVals.barium          = max(df['Barium'])
    maxVals.iron            = max(df['Iron'])

    return normalizeData(maxVals, df)

# Calculates the activation value for the neuron
def calculateActivationValue(values, weights):
    # Bias weight * bias value (1)
    # Loop over each row of weights (1 row is 1 node)
    activationValue = weights[0]

    for i in range(len(values)):
        activationValue += values[i] * weights[i + 1]

    return activationValue

# Calculating the new weights using the error correction learning technique
def calculateNewWeights(output, weights, values, expectedOutput):
    learningRate = 0.1
    outputDifference = int(expectedOutput) - int(output)

    # Calculates the new bias weight, with a bias value of 1 
    weights[0] = weights[0] + outputDifference * learningRate * 1

    # Caclulate the new weights for the other criteria
    for i in range(len(values)):
        weights[i + 1] = weights[i + 1] + outputDifference * learningRate * values[i]

    return weights

# Retrieves data from row
def parseRow(row):
    values = []
    # values.append(float(row[1][1]))
    # Skip row[1][1] since it's the ID
    values.append(float(row[1][2]))
    values.append(float(row[1][3]))
    values.append(float(row[1][4]))
    values.append(float(row[1][5]))
    values.append(float(row[1][6]))
    values.append(float(row[1][7]))
    values.append(float(row[1][8]))
    values.append(float(row[1][9]))
    values.append(int(row[1][10]))
    return values

# Calculates the output value for each neuron
def calculateOutput(activation):
    return 1 if activation > 0 else 0

def calcOutput(weights, values):
    # Initialize an empty list, the same size as the number of hidden nodes
    output = [0 for x in range(len(weights))]

    i, j = 0, 0
    print(len(weights))
    print(len(weights[i]))
    print(len(values))
    print("----------------")

    for i in range(len(weights)):
        sum = 0
        for j in range(len(weights[i])):
            sum += weights[i][j] * values[j]
        output[i] = sum

    print(output)
    return output

# Split data 70, 15, 15
def train():
    df = importCSV('GlassData.csv')

    global totalCount
    global successCount
    global numInputNodes
    global numOutputNodes
    global numHiddenLayers
    global numHiddenNodes

    numHiddenNodes = randint(numOutputNodes, numInputNodes)

    # Creates two 2D arrays with floating point numbers between -1 and 1.
    # The first is for the weights between the input nodes and the hidden nodes
    # The second is for the weights between the hidden nodes and the output nodes
    numHiddenNodes = 7
    inputHiddenWeights = [[uniform(-1, 1) for x in range(numInputNodes)] for y in range(numHiddenNodes)]
    hiddenOutputWeights = [[uniform(-1, 1) for x in range(numHiddenNodes)] for y in range(numOutputNodes)]
    # print(inputHiddenWeights)
    weights1 = [uniform(-1, 1) for _ in range(8)]
    weights2 = [uniform(-1, 1) for _ in range(8)]
    # Initializes array full of zeros. This will store the values of the hidden nodes
    values = [0 for x in range(numHiddenNodes)]
    
    # Wipes the existing file first
    open('output.txt', 'w')
    # Appends to new file
    with open('output.txt', 'a') as outputFile:
        outputFile.write("Initial weights input -> hidden: ")
        outputFile.write(str(inputHiddenWeights))
        outputFile.write("\nInitial weights hidden -> output: ")
        outputFile.write(str(hiddenOutputWeights))
        
    iterations = 2000
    trainThreshold = 25

    with open('output.txt', 'a') as outputFile:
        outputFile.write("\nIterations: ")
        outputFile.write(str(iterations))
        termCriteria = "\nTermination criteria: The termination criteria used is the program will run for the number of iterations specified"
        termCriteria += ", or until the success rate is above 90%% for %d runthroughs of the data." % trainThreshold
        outputFile.write(termCriteria)

    successRate = 0
    trained = 0

    for i in range(0, iterations):

        # If the successRate is greater than 90% 15 times, the NN is considered to be trained, and
        # the training will stop to prevent overtraining.
        if successRate > 0.9:
            trained += 1
            if (trained == trainThreshold):
                print("Trained:", trained)
                break

        errorCount = 0
        totalCount = 0
        successCount = 0
        successRate = 0

        # Lists to store activation value, output, and expected output 
        errorNeuron1 = []
        errorNeuron2 = []
        
        # Iterate over dataframe row
        for row in df.iterrows():
            values = parseRow(row)

            # Compute activation
            # Compute output from hidden node
            # Compute activation at output nodes
            # Compute output
            # Modify weights between hidden and output
            # Modify weights between input and hidden

            # For each node in hidden layer
                # For each weight in input layer
            hiddenResult = calcOutput(inputHiddenWeights, values)
            outputResult = calcOutput(hiddenOutputWeights, hiddenResult)

            # outputHiddenLayer = 
            activation1 = calculateActivationValue(values, weights1)
            activation2 = calculateActivationValue(values, weights2)

            output1 = calculateOutput(activation1)
            output2 = calculateOutput(activation2)

            # values[-1] contains the expected result
            expectedOutputBinary = format(int(values[-1]), '02b')
 
            # If the expectedOutput first bit is equal to the output of the first node
            if int(expectedOutputBinary[0]) != output1:
                weights1copy = weights1
                valuesCopy = values                
                errorNeuron1.append((activation1, output1, weights1copy, valuesCopy, int(expectedOutputBinary[0])))

            # If the expectedOutput second bit is equal to the output of the second node
            if int(expectedOutputBinary[1]) != output2:
                weights2copy = weights2
                valuesCopy = values
                errorNeuron2.append((activation2, output2, weights2copy, valuesCopy, int(expectedOutputBinary[1])))

            # If either of the outputs match their corresponding bit in the expected output,
            # increase the success count.
            if int(expectedOutputBinary[0]) == output1 and int(expectedOutputBinary[1]) == output2:
                successCount += 1

            totalCount += 1

        # print(successCount)
        # print(totalCount - successCount)
        # print(totalCount)
        successRate = float(successCount) / float(totalCount)
        print("Success rate: ", successRate)

        # List not empty
        if len(errorNeuron1) != 0:
            # Sorts to get the closest possible value to 0 as the first element, then use that to adjust the weights            
            errorNeuron1.sort(key=lambda tup: abs(tup[0]))  # sorts in place
            weights1 = calculateNewWeights(errorNeuron1[0][1], errorNeuron1[0][2], errorNeuron1[0][3], errorNeuron1[0][4])

        # List not empty
        if len(errorNeuron2) != 0:
            # Sorts to get the closest possible value to 0 as the first element, then use that to adjust the weights
            errorNeuron2.sort(key=lambda tup: abs(tup[0]))  # sorts in place
            weights2 = calculateNewWeights(errorNeuron2[0][1], errorNeuron2[0][2], errorNeuron2[0][3], errorNeuron2[0][4])

        print("--------------------------------------------")

    return (weights1, weights2)

def test(weights1, weights2):

    # TODO: output initial weights, node output function used
    # learning rate, termination criteria & proper explanations for the choice

    # Output types:
    # 1 = building_windows_float_processed
    # 2 = building_windows_non_float_processed
    # 3 = vehicle_windows_float_processed
    # 5 = containers
    # 6 = tableware
    # 7 = headlamp

    df = importCSV('testSeeds.csv')

    successTestCount = 0
    totalCount = 0

    with open('output.txt', 'a') as outputFile:
        outputFile.write("\n\nOriginal\tPredicted\n")

    # Lists to hold the expected and actual output.
    # Used when calculating percision and recall.
    expectedOutputList = []
    actualOutputList = []

    # Iterate over dataframe row
    for row in df.iterrows():

        values = parseRow(row)
        activation1 = calculateActivationValue(values, weights1)
        activation2 = calculateActivationValue(values, weights2)

        output1 = calculateOutput(activation1)
        output2 = calculateOutput(activation2)

        # values[-1] contains the expected result
        expectedOutputBinary = format(int(values[-1]), '02b')

        # If either of the outputs did not match their corresponding bit in the expected output,
        # increase the error.
        if int(expectedOutputBinary[0]) == output1 and int(expectedOutputBinary[1]) == output2:
            successTestCount += 1

        # Convert 2 outputs to decimal value
        if output1 == 0 and output2 == 1:
            expectedOutputList.append(1)
        elif output1 == 1 and output2 == 0:
            expectedOutputList.append(2)
        elif output1 == 1 and output2 == 1:
            expectedOutputList.append(3)
        else:
            expectedOutputList.append(0)
        
        actualOutputList.append(int(values[-1]))

        with open('output.txt', 'a') as outputFile:
            output = output1 + output2
            outputFile.write("%d" % int(values[-1]))
            outputFile.write("\t\t\t%s\n" % output)

        totalCount += 1
    
    print("============================")
    print("Testing")
    print("============================")

    print("Success Count: ", successTestCount)
    print("Total Count: ", totalCount)
    successRate = float(successTestCount) / float(totalCount)
    print("Success Rate: %.2f", successRate)

    return (expectedOutputList, actualOutputList)

# Training perceptron using Scikit
def externalToolTraining(percision, recall):
    # Added skip rows due to the addition of headers in the csvs.
    trainingData = np.loadtxt('trainSeeds.csv', delimiter=',', skiprows=1)
    testData = np.loadtxt('testSeeds.csv', delimiter=',', skiprows=1)

    # Removing last column
    trainingInputData = trainingData[:, :-1]
    # Removing all columns except last column
    trainingDesiredOutput = trainingData[:, -1]

    # Removing last column
    testInputData = testData[:, :-1]
    # Removing all columns except last column
    testDesiredOutput = testData[:, -1]

    # Using scikit learn
    ss = StandardScaler()
    ss.fit(trainingInputData)
    train = ss.transform(trainingInputData)
    test = ss.transform(testInputData)
    perceptron = Perceptron(n_iter=40, eta0=0.1, random_state=0)
    perceptron.fit(train, trainingDesiredOutput)

    prediction = perceptron.predict(test)

    open('toolBasedOutput.txt', 'w')
    with open('toolBasedOutput.txt', 'a') as outputFile:
        outputFile.write("Percision\n")
        outputFile.write("--------------------------\n")
        outputFile.write("Scikit Learn: %.2f\n" % precision_score(testDesiredOutput, prediction, average='weighted'))
        outputFile.write("My code: %.2f\n" % percision)
        outputFile.write("--------------------------\n")
        outputFile.write("Recall\n")
        outputFile.write("--------------------------\n")
        outputFile.write("Scikit Learn: %.2f\n" % recall_score(testDesiredOutput, prediction, average='weighted'))
        outputFile.write("My code: %.2f\n" % recall)

def main():
    (weights1, weights2) = train()
    # (expectedOutputList, actualOutputList) = test(weights1, weights2)
    
    # percision = precision_score(expectedOutputList, actualOutputList, average='weighted')
    # recall = recall_score(expectedOutputList, actualOutputList, average='weighted')
    # 
    # with open('output.txt', 'a') as outputFile:
        # outputFile.write("\nFinal weight 1: %s" % str(weights1))
        # outputFile.write("\nFinal weight 2: %s\n" % str(weights2))
        # outputFile.write("Percision score: %.2f\n" % percision)
        # outputFile.write("Recall score: %.2f\n" % recall)
        # outputFile.write("\nConfusion matrix: \n%s" % confusion_matrix(expectedOutputList, actualOutputList))
# 
    # externalToolTraining(percision, recall)

main()