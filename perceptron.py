import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.data", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:500, 0:8]
Y = dataset[:500, 8]
answers = []
for y in Y:
    if y == 0:
        answers.append(-1)
    else:
        answers.append(1)

# data to test results with
x_test = dataset[500:, 0:8]
y_test = dataset[500:, 8]

params = [0]*8
c = 0

def try_params_on_row(row, existing_params):
    """ Pass the row of data you want to try this out on """
    result = c
    for i, param in enumerate(params):
        result += X[row, i]*param
    sign = numpy.sign(result)
    if sign != answers[row]:
        existing_params = update(row)

def update(row):
    new_params = []
    for i, param in enumerate(params):
        new_params[i] = param + answers[row]*X[row, i]
    return new_params

def learn()