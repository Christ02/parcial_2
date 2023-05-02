from BST_tree import BinarySearchTree
from AVL_tree import AVL_tree
import time
import random
import cProfile

def run_profiler():
    N = 10000000

    data_bst = random.sample(range(1, 10000001), N)
    data_avl = data_bst.copy()

    bst = BinarySearchTree()
    avl = AVL_tree()

    #inserts
    start_time = time.time()

    for data in data_bst:
        bst.insert(data)
    bst_insert_time = time.time() - start_time
    print("BST nodes: ", bst.count_nodes())

    start_time = time.time()

    for data in data_avl:
        avl.insert(data)
    avl_insert_time = time.time() - start_time
    print("AVL nodes: ", avl.count_nodes())

    #search

    search_numbers = random.sample(range(1, N+1), 1000)

    start_time = time.time()

    for number in search_numbers:
        bst.search(number)
    bst_search_time = time.time() - start_time

    start_time = time.time()

    for number in search_numbers:
        avl.search(number)
    avl_search_time = time.time() - start_time

    print("BST insert time: ", bst_insert_time)
    print("AVL insert time: ", avl_insert_time)
    print("BST search time: ", bst_search_time)
    print("AVL search time: ", avl_search_time)

cProfile.run('run_profiler()', sort='tottime')