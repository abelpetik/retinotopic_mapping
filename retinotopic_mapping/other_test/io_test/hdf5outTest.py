import matplotlib.pyplot as plt
from visexpa.engine.datahandlers.hdf5io import Hdf5io



with Hdf5io(filename="/home/abel/data/widefield1575879163.hdf5", filelocking=False) as in_file:
    print(type(in_file.h5f))
    print(in_file.h5fpath)
    print(in_file.h5f)
    print(f"Ez a root: {in_file.h5f.root}")


    array = in_file.hdf2ndarray(group=in_file.h5f.root) # in_file.h5f.root cut out

    print(type(array))
    print(array.shape)
    print(array[:10])

    plt.plot(array)
    plt.savefig("output.png")
    plt.show()