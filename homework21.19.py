import statistics

def mean(data):
    return statistics.mean(data)

def median(data):
    return statistics.median(data)

def mode(data):
    return statistics.mode(data)

def standard_deviation(data):
    return statistics.stdev(data)

data_operations = {
    "mean": mean,
    "median": median,
    "mode": mode,
    "standard_deviation": standard_deviation
}


def analyze_data(data, operation):
    if operation in data_operations:
        return data_operations[operation](data)
    else:
        raise ValueError(f"Unsupported data analysis operation: {operation}")


data = [1, 2, 2, 3, 4, 4, 4, 5, 6]

print(analyze_data(data, "mean"))
print(analyze_data(data, "median"))
print(analyze_data(data, "mode"))
print(analyze_data(data, "standard_deviation")) 

