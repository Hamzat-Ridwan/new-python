kanto = [73, 67, 43]
weights = [0.3, 0.2, 0.5]

def product_sum(region, weights):
    result = 0
    for w, x in zip(region, weights):
        result += w*x
    print(result)

product_sum(kanto, weights)