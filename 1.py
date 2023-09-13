class Neuron:
    def __init__(self,w1,w2,b) -> None:
        self.w1 = w1
        self.w2 = w2
        self.b = b

    def activasion_function(self, x1, x2):
        output = self.w1*x1 + self.w2*x2 + self.b
        if output >= 0:
            return 1
        else:
            return 0 
        
neuron = Neuron(1,1,-1.5)

input_data = [(0,0),(0,1),(1,0),(1,1)]

for x1,x2 in input_data:
    result=neuron.activasion_function(x1,x2)
    print(f"{x1}  {x2}|{result}")

        