# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @ReeveWu
Version: v0.0.1
'''


from typing import Optional, Union
class DatasetConfig:
    object_col = {
        "Titanic": [['Name', 'Ticket', 'Cabin', 'SibSp'], ['Sex', 'Embarked']],
        "Diabetes": [[], []]
    }

    y_col = {
        "Titanic": ["Survived"],
        "Diabetes": ["Outcome"]
    }

    def __init__(self, dataset: str, select_col: list[str], handling_missing_value: bool, scaling: str, data_split: list[float]):
        self.dataset = dataset
        self.select_col = select_col
        self.handling_missing_value = handling_missing_value
        self.scaling = scaling
        self.data_split = data_split
        self.col_onehot = self._get_col_onehot()
        self.col_label = self._get_col_label()
        self.col_remaining = self._get_col_remaining()
        self.y_col = self._get_y_col()

    def _get_col_onehot(self):
        return list(set(self.object_col[self.dataset][0]) & set(self.select_col))

    def _get_col_label(self):
        return list(set(self.object_col[self.dataset][1]) & set(self.select_col))

    def _get_col_remaining(self):
        return [item for item in self.select_col if item not in set(self.col_onehot + self.col_label)]

    def _get_y_col(self):
        return self.y_col[self.dataset]

class DecisionTreeModelConfig:
    def __init__(self, criterion: str, min_samples_split: int, min_samples_leaf: int, max_features: Union[int, float, str, None] = None, max_depth: Optional[int] = None, max_leaf_nodes: Optional[int] = None):
        self.criterion = criterion
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.max_depth = max_depth
        self.max_leaf_nodes = max_leaf_nodes
