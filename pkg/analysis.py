#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

from .unit_base import ItemBase, UnitBase


class AnalystItem(ItemBase):
    def __init__(self, data_item, method_item, **kwargs):
        super().__init__(**kwargs)
        self._data = data_item
        self._method = method_item
        self._is_checked = False
        self._results = None

    @property
    def check_func(self):
        return self._obj

    @property
    def data(self):
        return self._data

    @property
    def method(self):
        return self._method

    @property
    def is_checked(self):
        return self._is_checked

    @property
    def results(self):
        return self._results

    @property
    def check_state(self):
        if self.check_func:
            return self.is_checked
        else:
            return self.check_func

    def check(self, *argv, **kwargs):
        self.is_checked = self.obj(*argv, **kwargs)
        return self.is_checked

    def do_analysis(self, save_mode=False, *argv, **kwargs):
        # TODO: Safe mode -- check it before do analysis.
        results = self.method.function(
            self.data.obj, self.method.parameters, *argv, **kwargs
        )
        self._results = results
        return results
        pass


class Analyst(UnitBase):
    def __init__(self, name="analyst", **kwargs):
        super().__init__(unit_name=name, **kwargs)

    def add_analyst_item(
        self, name, description, data_item, method_item, check=None
    ):
        item = AnalystItem(
            obj=check,
            data_item=data_item,
            method_item=method_item,
            name=name,
            description=description,
        )
        item.update_metadata("data", data_item.name)
        item.update_metadata("method", method_item.name)
        self.add_item(item)
        return item

    def report(self, show=True, show_notes=False, max_width=30):
        table = super().report(show=False, show_notes=show_notes)
        data_list, method_list, check_states = [], [], []
        for item in self.items:
            item = self.get_item(item)
            data = item.data.name
            method = item.method.name
            data_list.append(data)
            method_list.append(method)
            check_states.append(item.check_state)
        table.add_column("Data", data_list)
        table.add_column("Method", method_list)
        table.add_column("Check?", check_states)
        table.max_width = max_width
        if show:
            print(table)
        else:
            return table

    pass
