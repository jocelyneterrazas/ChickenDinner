

def evaluateNeuralNetwork(input1, weights):
    result = 0
    for i in range(len(input1)):
        hi = input1[i] * weights[i]
        #print(weights[i])
        result+=(hi)
    return round(result, 3)

def evaluateNeuralError(desired, actual):
    return round(desired - actual,3)

def learningFunc(input1, weights, learningRate):
    for i in range(len(input1)):
        if input1[i] > 0:
            weights[i]+= learningRate
            round(weights[i], 3)

def training(trials, input1, weights, learningRate):
    for i in range(trials):
        neuralNetResult = evaluateNeuralNetwork(input1, weights)
        learningFunc(input1, weights, learningRate)
        err = evaluateNeuralError(1, neuralNetResult)
        print("Error: ", err, "Result: ", neuralNetResult)
    round(weights[2], 3)
    print(weights)
    return neuralNetResult
        

if __name__=="__main__":
    input1 = [0,0,1,0]
    weights = [0,0,0,0]
    desiredResult = 1
    learningRate = 0.20
    trials = 6
    result = training(trials, input1, weights, learningRate)
    if (result >=1):
        print("WINNER WINNER, CHICKEN DINNER")
    #evaluateNeuralNetwork(input1, weights)
