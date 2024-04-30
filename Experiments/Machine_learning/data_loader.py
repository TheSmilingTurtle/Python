import numpy as np
import csv

def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def readCSV(filename, title_len=0):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        out = []
        for row in spamreader:
            out.append(row)
        return out[title_len:]


def re_load(filename, filename2):
    data = readCSV(filename, 2)
    v_data = readCSV(filename2, 2)

    ### INPUTS = TIME, ACCEL[x], ACCEL[y], ACCEL[z] V[abs]
    ### OUTPUTS = GPS[x], GPS[y], GPS[z], V[abs]

    # [self.times[i], a_x[i], a_y[i], a_z[i], self.velocity[i]]
    # [l_x[i], l_y[i], l_z[i], self.velocity[i]]

    td = []
    tl = []
    for i in data:
        td.append(np.array([
            [i[0]],
            [i[1]],
            [i[2]],
            [i[3]],
            [i[4]],
            [i[5]],
            [i[6]],
            [i[7]]
        ], dtype=np.float64))
        tl.append(np.array([
            [i[8]],
            [i[9]],
            [i[10]],
            [i[11]]
        ], dtype=np.float64))

    training = (td, tl)

    vd = []
    vl = []
    for i in v_data:
        vd.append(np.array([
            [i[0]],
            [i[1]],
            [i[2]],
            [i[3]],
            [i[4]],
            [i[5]],
            [i[6]],
            [i[7]]
        ], dtype=np.float64))
        vl.append(np.array([
            [i[8]],
            [i[9]],
            [i[10]],
            [i[11]]
        ], dtype=np.float64 ))

    print(len(vd))
    validation = (vd, vl)

    return (training, validation)


def wrap_data(filename, filename2):
    tr_d, va_d = re_load(filename, filename2)
    training_inputs = [np.reshape(x, (8, 1)) for x in tr_d[0]]
    training_labels = [np.reshape(x, (4, 1)) for x in tr_d[1]]
    training_data = zip(training_inputs, training_labels)
    validation_inputs = [np.reshape(x, (8, 1)) for x in va_d[0]]
    validation_labels = [np.reshape(x, (4, 1)) for x in va_d[1]]
    validation_data = zip( validation_inputs, validation_labels)

    return (training_data, validation_data)