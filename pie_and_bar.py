import numpy as np
import matplotlib.pyplot as plt
import copy
import pandas as pd
import pickle


color_scheme = {0: '#09568d', 1: '#172035', 2: '#457725', 3: '#686b69', 4: '#ffbb00', 5: '#f8a300', 6: '#f0c282',
                7: '#ce3500', 8: '#901E1D', 9: '#421814', 10: '#a2a7ad', 11: '#47484a',
                12: '#7284b7', 13: '#acac9a', 14: '#874840', 15: '#987563'}

phases_interpretor = {0: 'Preparation and orientation at abdomen', 1: 'Dissection of lymphnodes and blood vessels',
          2: 'Retroperitoneal preparation to lower pancreatic border',
          3: 'Retroperitoneal preparation of duodenum and pancreatic head',
          4: 'Mobilizing the sigmoid and the descending colon', 5: 'Mobilizing the spenic flexure',
          6: 'Mobilizing the tranverse colon', 7: 'Mobilizing the ascending colon',
          8: 'Dissection and resection of rectum', 9: 'Preparing the anastomosis extraabdominally',
         10: 'Preparing the anastomosis intraabdominally', 11: 'Placing stoma', 12: 'Finishing the operation',
         13: 'Exception (will be ignored during evaluation)'}



def bar_plot(input_dict, plot_name='Chicken Bar Plot', save=False):
    N = len(input_dict)
    ind = np.arange(N)
    width = 0.35
    df = pd.DataFrame()
    for i in range(N):
        tmp_sub_list = []
        for j in range(N):
            tmp_sub_list.append(sum(input_dict[i][j]) / 25 / (len(input_dict[i][j]) if len(input_dict[i][j]) > 0 else 1))
        df['from %d to others' % i] = tmp_sub_list
        #plt.bar(ind, tmp_sub_list, width, bottom=tmp_sub_list)
    for i in range(N):
        vector = df.ix[i, :]
        plt.bar(ind, vector, width, bottom=vector)

    plt.ylabel('average seconds')
    plt.title(plot_name)
    plt.xticks(ind)
    plt.yticks()
    plt.legend(range(N))
    if save:
        plt.savefig(plot_save_folder + plot_name + '.png')
    else:
        plt.show()
    plt.close()
    return


def pie_chart(input_dict, plot_name='Chicken Pie Plot', save=False):
    N = len(input_dict)
    ind = np.arange(N)
    tmp_list = []
    for i in range(N):
        tmp_sub_list = []
        for j in range(N):
            tmp_sub_list.append(sum(input_dict[i][j]) / (len(input_dict[i][j]) if len(input_dict[i][j]) > 0 else 1))
        plt.pie(tmp_sub_list, labels=ind,
                autopct='%1.1f%%', shadow=True, startangle=140,)# colors=color_scheme[i])
        plt.axis('equal')
        plt.title(plot_name + ' trasition from {0}'.format(i))
        tmp_list.append(tmp_sub_list)
        if save:
            plt.savefig(plot_save_folder + plot_name + ' trasition from {0}'.format(i) + '.png')
        else:
            plt.show()
        plt.close()
    return

def save_dicts_as_file():
    with open('/home/zzhang/PycharmProjects/endovis/meta/phase_transition_all.pkl', 'wb') as f:
        pickle.dump(complete_dictionary(all_procedures), f, pickle.HIGHEST_PROTOCOL)
    i = 0
    for procedure in procedures:
        with open('/home/zzhang/PycharmProjects/endovis/meta/phase_transition_{0}.pkl'.format(procedure), 'wb') as f:
            pickle.dump(complete_dictionary(procedure_list[i]), f, pickle.HIGHEST_PROTOCOL)
            i += 1
    return

