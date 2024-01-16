# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Main ----------
_, HIDDEN, how_many_cal = map(int, input().split())

# Initialization
hidden_layer = [list(map(int, input().split())) for _ in range(HIDDEN)]
output_layer = list(map(int, input().split()))

# Preprocessing
input_coef = dict()
total_bias = 0

for idx, (_, *data_and_weight, bias) in enumerate(hidden_layer):
    output_weight = output_layer[idx]
    half = len(data_and_weight) // 2
    
    # Save each input node weight by dictionary
    for i in range(0, half):
        data   = data_and_weight[i]
        weight = data_and_weight[i+half]
        key    = data - 1
        
        # Input node's weight
        input_coef[key] = input_coef.get(key, 0) + (weight * output_weight)
        
    # Each hidden node's bias
    total_bias += bias * output_weight
    
# Output layer's bias
total_bias += output_layer[-1]

# Answer calculating
for _ in range(how_many_cal):
    answer = total_bias
    
    for key, value in enumerate(map(int, input().split())):
        answer += input_coef[key] * value
        
    print(answer)