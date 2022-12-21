# -*- coding: utf-8 -*-
import numpy as np
# function to extract matrix from path

def read_input(path):
    with open(path) as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(x) for x in line.split()[0]])
    return np.array(matrix)
# calculate dim of matrix
def calculate_dim(matrix):
    return len(matrix), len(matrix[0])

# function to calculate if a tree is visible
def calculate_if_tree_is_visible(matrix):
    # a tree is visible from a position if there is no tree tallest in the same row or column
    # return a matrix with 1 if the tree is visible and 0 if not
    X,Y = calculate_dim(matrix)
    matrix_visible = np.zeros((X,Y))

    for i in range(X):
        for j in range(Y):
            # contorno allways visible
            if i == 0 or i == X-1 or j == 0 or j == Y-1:
                matrix_visible[i][j] = 1
            else:
                # check if there from right all trees are lower
                if all(matrix[i][j] > matrix[i][k] for k in range(j+1,Y)):
                    matrix_visible[i][j] = 1
                # check if there from left all trees are lower
                elif all(matrix[i][j] > matrix[i][k] for k in range(0,j)):
                    matrix_visible[i][j] = 1
                # check if there from down all trees are lower
                elif all(matrix[i][j] > matrix[k][j] for k in range(i+1,X)):
                    matrix_visible[i][j] = 1
                # check if there from up all trees are lower
                elif all(matrix[i][j] > matrix[k][j] for k in range(0,i)):
                    matrix_visible[i][j] = 1
    return matrix_visible
                
def calculate_number_of_visible_trees_from_tree(matrix):
    X,Y = calculate_dim(matrix)
    matrix_visible_from_tree = np.zeros((X,Y))
    for i in range(X):
        for j in range(Y):
            # if i==3 and j== 2:
            #     print('hola')
            # contorno allways visible
            if i == 0 or i == X-1 or j == 0 or j == Y-1:
                matrix_visible_from_tree[i][j] = 0
            else:
                number_of_trees_visible_from_right=0
                for k in range(j+1,Y):
                    number_of_trees_visible_from_right += 1
                    if matrix[i][j] <= matrix[i][k]:
                        break
                number_of_trees_visible_from_left=0
                for k in range(j-1,-1, -1):
                    number_of_trees_visible_from_left += 1
                    if matrix[i][j] <= matrix[i][k]:
                        break
                number_of_trees_visible_from_down=0
                for k in range(i+1,X):
                    number_of_trees_visible_from_down += 1
                    if matrix[i][j] <= matrix[k][j]:
                        break
                number_of_trees_visible_from_up=0
                for k in range(i-1,-1,-1):
                    number_of_trees_visible_from_up += 1
                    if matrix[i][j] <= matrix[k][j]:
                        break
                matrix_visible_from_tree[i][j] = number_of_trees_visible_from_right * \
                    number_of_trees_visible_from_left * number_of_trees_visible_from_down * \
                    number_of_trees_visible_from_up
    return matrix_visible_from_tree
                



def main():

    matrix = read_input('2022-08/input.txt')
    matrix_visible = calculate_if_tree_is_visible(matrix)
    print(f'visible tree: {np.sum(matrix_visible)}')
    matrix_visible_from_tree = calculate_number_of_visible_trees_from_tree(matrix)
    print(f'max number visible tree are: {np.max(matrix_visible_from_tree)}')
if __name__ == '__main__':
    main()