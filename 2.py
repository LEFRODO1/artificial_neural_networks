import random

class Neuron:
    def __init__(self, n):
        self.n_inputs = n
        self.weights = [random.uniform(0.001, 0.2) for _ in range(n)]
        self.bias = random.uniform(0.001, 0.2)

    def predict(self, x):
        if len(x) != self.n_inputs:
            raise ValueError(f"Input vector size must be {self.n_inputs}, but got {len(x)}")
        
        weighted_sum = sum(w * xi for w, xi in zip(self.weights, x)) + self.bias
        return weighted_sum

class NeuralNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.neurons = [Neuron(n_inputs) for n_inputs in n_neurons]

    def predict(self, x):
        if len(x) != self.n_neurons[0].n_inputs:
            raise ValueError(f"Input vector size must be {self.n_neurons[0].n_inputs}, but got {len(x)}")
        
        outputs = [neuron.predict(x) for neuron in self.neurons]
        return outputs

    def fit(self, x, y):
        # Implement training logic here
        pass
    

    def fit_1(self, x, y, learning_rate):
        n = len(x)
        for i in range(n):
            y_pred = self.predict(x[i])
            error = y_pred - y[i]
            for j in range(len(self.weights)):
                self.weights[j] -= learning_rate * error * x[i][j]
            self.bias -= learning_rate * error
