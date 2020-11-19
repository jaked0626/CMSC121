'''
Linear regression

Jake Underland

Main file for linear regression and model selection.
'''

import numpy as np
from sklearn.model_selection import train_test_split
import util


class DataSet(object):
    '''
    Class for representing a data set.
    '''

    def __init__(self, dir_path):
        '''
        Class for representing a dataset, performs train/test
        splitting.

        Inputs:
            dir_path: (string) path to the directory that contains the
              file
        '''

        parameters_dict = util.load_json_file(dir_path, "parameters.json")
        self.pred_vars = parameters_dict["predictor_vars"]
        self.name = parameters_dict["name"]
        self.dependent_var = parameters_dict["dependent_var"]
        self.training_fraction = parameters_dict["training_fraction"]
        self.seed = parameters_dict["seed"]
        self.labels, data = util.load_numpy_array(dir_path, "data.csv")
        self.training_data, self.testing_data = train_test_split(data,
            train_size=self.training_fraction, test_size=None,
            random_state=self.seed)

class Model(object):
    '''
    Class for representing a model.
    '''

    def __init__(self, dataset, pred_vars):
        '''
        Construct a data structure to hold the model.
        Inputs:
            dataset: an dataset instance
            pred_vars: a list of the indices for the columns (of the
              original data array) used in the model.
        '''
        
        self.dep_var = dataset.dependent_var
        self.pred_vars = pred_vars
        self.names = dataset.labels
        self.training_data = dataset.training_data
        self.beta = self.create_beta()
        self.R2 = self.find_R2(self.training_data)  # default w/ training_data
    
    def __repr__(self):
        '''
        Format model as a string.
        '''
        s = "{} ~ {:.6f}".format(self.names[self.dep_var], self.beta[0])
        for i, index in enumerate(self.pred_vars):
            s += " + {:.6f} * {}".format(self.beta[i+1], self.names[index])

        return s
    
    def create_x(self, data):
        '''
        Creates a matrix of observations where each row is a sample and 
        each column is a predictor variable from the list pred_vars, excluding
        the first column which is all ones.
        
        Input: 
            data(np.array): data used to construct x.
        Returns:
            x: np.array
        '''
        x = data[:, self.pred_vars]
        x = util.prepend_ones_column(x)

        return x
    
    def create_y(self, data):
        '''
        Creates a list of observations for dependent variable y. 
        
        Input: 
            data(np.array): data used to construct y
        Returns:
            y: list
        '''
        y = data[:, self.dep_var]
        
        return y

    
    def create_beta(self):
        '''
        Runs a linear regression using the observations of the independent
        variables and the dependent variable and returns a list of coefficients.
        Returns:
            beta: a list of coefficients
        '''
        x = self.create_x(self.training_data)
        y = self.create_y(self.training_data)
        beta_lst = util.linear_regression(x, y)

        return beta_lst

    def find_R2(self, data):
        '''
        Computes the R2 value of the model.  
        
        Input: 
            data(np.array): data used to construct find R2.
        Returns:
            R_squared: R2 value of the model. 
        '''
        y = self.create_y(data)
        y_hat = util.apply_beta(self.beta, self.create_x(data))
        y_bar = np.mean(y)
        R_squared = 1 - (np.sum((y - y_hat) ** 2) / np.sum((y - y_bar) ** 2))

        return R_squared


def compute_single_var_models(dataset):
    '''
    Computes all the single-variable models for a dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        List of Model objects, each representing a single-variable model
    '''

    return [Model(dataset, [i]) for i in dataset.pred_vars]


def compute_all_vars_model(dataset):
    '''
    Computes a model that uses all the predictor variables in the dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object that uses all the predictor variables
    '''
    pred_vars = dataset.pred_vars
    return Model(dataset, pred_vars)


def compute_best_pair(dataset):
    '''
    Find the bivariate model with the best R2 value

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object for the best bivariate model
    '''
    # initialize best bivariate model to the first possible combination of
    # predictor variables
    lst_pred = dataset.pred_vars[:]
    best_biv = Model(dataset, lst_pred[0:2])

    for i, x in enumerate(lst_pred):
        for y in lst_pred[i+1:]:
            new_biv = Model(dataset, [x, y])
            if new_biv.R2 > best_biv.R2:
                best_biv = new_biv

    return best_biv


def forward_selection(dataset):
    '''
    Given a dataset with P predictor variables, uses forward selection to
    select models for every value of K between 1 and P.

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A list (of length P) of Model objects. The first element is the
        model where K=1, the second element is the model where K=2, and so on.
    '''

    # create list of lists of indices to keep track of index combinations for 
    # independent variables that yield the highest value of R2 for each K, and
    # a list of models containing those indices. 

    best_indices = []
    best_models_lst = []
    lst_pred = dataset.pred_vars[:]

    for k, _ in enumerate(lst_pred):
        best_R2 = 0
        for i in lst_pred:
            # create k_lst, a cumulative list with best 
            # combination of indices, no overlap of indices
            if k > 0:
                k_lst = list(best_indices[-1])
            else:
                k_lst = []

            if i not in k_lst:  
                k_lst.append(i)
                new_model = Model(dataset, k_lst)

                if new_model.R2 > best_R2:
                    best_R2 = new_model.R2
                    best_k_lst = list(k_lst)
                    best_model = new_model

        # update best_indices per K, so next list can build off of last
        best_indices.append(best_k_lst)
        best_models_lst.append(best_model)
        
    return best_models_lst


def validate_model(dataset, model):
    '''
    Given a dataset and a model trained on the training data,
    compute the R2 of applying that model to the testing data.

    Inputs:
        dataset: (DataSet object) a dataset (unused)
        model: (Model object) A model that must have been trained
           on the dataset's training data.

    Returns:
        (float) An R2 value
    '''

    return model.find_R2(dataset.testing_data)
