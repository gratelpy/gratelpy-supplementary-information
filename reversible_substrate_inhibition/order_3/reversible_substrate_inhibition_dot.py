from stoich import get_graph_stoich
from parse_mechanism import get_network_from_mechanism
from drawing import gratelpy_draw, gratelpy_dot
from matplotlib import pyplot as plt
from fragments import get_sensible_fragments
from subgraphs import get_all_valid_subgraphs
import cPickle as pickle

mechanism_file = 'reversible_substrate_inhibition.txt'
results_file = 'reversible_substrate_inhibition.vsg'

alpha, beta, dict_complexes, dict_constants, dict_complexes_reverse, dict_constants_reverse = get_network_from_mechanism(mechanism_file, 4)

G, stoich, stoich_rank = get_graph_stoich(alpha, beta)

pos = {
    'w6': [0,0], 's4': [1,1], 's3': [3,0],
    'w5': [2,2], 'w4': [3,2],
    'w2': [0,4], 's1': [1,4], 'w3': [2,4], 's2': [3,4],
    'w1': [1,6]
    }

dot_graph = gratelpy_dot(G, positions=pos, dictionary_complexes=dict_complexes_reverse, dictionary_reactions=dict_constants_reverse,filename='reversible_substrate_inhibition.dot', filename_print='reversible_substrate_inhibition.pdf')

