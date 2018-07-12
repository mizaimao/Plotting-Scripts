import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2

root = '/home/zzhang/Downloads/endov/DeviceData/'
procedures = ('Prokto', 'Rektum','Sigma')
procedure_count = 8
color_map = {'Prokto': '#0084a1', 'Rektum': '#ff5958','Sigma': '#6aa758'}

def get_csv_data(i, j):
    test_file = root + str(i) + str(j) +'_Device.csv'
    return pd.read_csv(test_file, header=None, index_col=False)


def plot():
    for procedure in procedures:
        for j in range(1, procedure_count + 1):
            df = get_csv_data(procedure, j)
            _, len = df.shape
            f, axarr = plt.subplots(len, sharex=True, figsize=(30, 50))
            for i in range(len):
                axarr[i].plot(df[0], df[i], color=color_map[procedure])
                axarr[i].set(ylabel='col %d' % i)
            plt.savefig('/tmp/{0}{1}.png'.format(procedure, j))

        # plt.show()

def concatenate():
    image = None
    for procedure in procedures:
        for j in range(1, procedure_count + 1):
            sub_image = cv2.imread('/tmp/{0}{1}.png'.format(procedure, j))
            if image is None:
                image = sub_image
            else:
                image = np.concatenate((image, sub_image), axis=1)
    cv2.imwrite('/tmp/chicken.png', image)
    return

#plot()
concatenate()
