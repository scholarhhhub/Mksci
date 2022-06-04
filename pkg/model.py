#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# Created date: 2022-02-10
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import pandas as pd
from attrs import define, field
from SyntheticControlMethods import DiffSynth, Synth

from .unit_base import ItemBase, UnitBase


class MethodItem(ItemBase):
    def __init__(self, parameters, **kwargs):
        super().__init__(**kwargs)
        self._parameters = parameters

    pass

    @property
    def parameters(self):
        return self._parameters

    @property
    def function(self):
        return self._obj

    def str_parameters(self):
        str_parameters = []
        for i, k in enumerate(self.parameters):
            str_parameters.append(f"({i+1}) {k}.")
        return "".join(str_parameters)


class Method(UnitBase):
    def __init__(self, name="model", **kwargs):
        super().__init__(unit_name=name, **kwargs)

    def add_function_item(
        self, function, name=None, parameters=None, description=""
    ):
        if not parameters:
            parameters = {}
        if not name:
            name = function.__name__
        item = MethodItem(
            name=name,
            obj=function,
            parameters=parameters,
            description=description,
        )
        item.update_metadata("parameters", parameters)
        self.add_item(item)
        return item

    def add_item_from_yaml(self, yaml_file):
        pass

    def check_dataset(self, dataset):
        self.dataset = dataset
        pass

    def report(self, show=True, show_notes=False, max_width=30):
        table = super().report(show=False, show_notes=show_notes)
        funcs, parameters = [], []
        for item in self.items:
            item = self.get_item(item)
            funcs.append(item.obj.__name__)
            parameters.append(item.str_parameters())
        table.add_column("Func", funcs)
        table.add_column("Params", parameters)
        table.max_width = max_width
        if show:
            print(table)
        else:
            return table


if __name__ == "__main__":
    pass
