import pickle


def save_data(fname, data):
    f = open(fname, 'wb')
    pickle.dump(data, f)
    f.close()


def read_data(fname):
    f = open(fname, 'rb')
    temp = pickle.load(f)
    f.close()
    return temp
