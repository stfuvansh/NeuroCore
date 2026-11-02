import math

inputs = [0.1, 0.2, 0.3]
weights = [0.5, -0.6, 0.8]
bias = 0.4

tmp = 0

for i in range(len(inputs)):
    tmp = tmp + (inputs[i] * weights[i])

z = tmp + bias

def sigmoid(z):
    return 1 / (1 + math.e ** (-z))

y = sigmoid(z)

print(y)