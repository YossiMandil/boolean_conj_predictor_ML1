import sys
import numpy as np

def print_result(h,path = "output.txt"):
    try:
        file = open(path, "w")
        exist_literals = [i for i in range(len(h)) if len(h[i]) > 0]
        for i in exist_literals[0:-1]:
            if 1 in h[i]:
                file.write("x{0},".format(i+1))
            if 0 in h[i]:
                file.write("not(x{0}),".format(i+1))
        last_exist_literal = exist_literals[-1]
        if 1 in h[last_exist_literal]:
            file.write("x{0}".format(last_exist_literal + 1))
        if 0 in h[last_exist_literal]:
            file.write("not(x{0})".format(last_exist_literal + 1))
        file.close()
    except IOError as e:
        print("error in writing to file {0} {1}".format(e.strerror, e.errno))

def check_hypothesis(h,x):
    try:
        for i in range(len(h)):
            check_false = (int(x[i]) + 1) % 2
            if check_false in h[i]:
                return 0
        return 1
    except Exception:
        return 1


def learn_boolean_conj(X, Y):
    h=[[1, 0] for i in range(len(X[0]))]
    for x, y in zip(X, Y):
        if y == 1 and check_hypothesis(h, x) == 0:
            for i in range(len(x)):
                if x[i] == 1:
                    if 0 in h[i]:
                        h[i].remove(0)

                else:
                    if 1 in h[i]:
                        h[i].remove(1)
    return h



def read_data_set (path= "example1"):
    try:
        training_examples = np.loadtxt(path)
    except Exception:
        e = sys.exc_info()[0]
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        raise
    X = [x[0:-1] for x in training_examples]
    Y = [y[-1] for y in training_examples]
    return np.array(X).astype(int), np.array(Y).astype(int)



def main():

    if len(sys.argv) < 2:
        raise Exception("need path argument")
    X, Y = read_data_set(sys.argv[1])
    print_result(learn_boolean_conj(X, Y))













if __name__=="__main__":
    main()