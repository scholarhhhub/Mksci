#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import os

import pandas as pd

from .unit_base import ItemBase, UnitBase


class DataItem(ItemBase):
    def __init__(self, abs_path, category, **kwargs):
        super().__init__(**kwargs)
        self._abs_path = abs_path
        self._category = category
        self.update_metadata("path", abs_path)
        self.update_metadata("category", category)

    pass

    @property
    def rel_path(self):
        if self.abs_path:
            return os.path.relpath(self._abs_path)
        else:
            return None

    @property
    def category(self):
        return self._category


class Datasets(UnitBase):
    def __init__(self, categories=None, name="dataset", **kwargs):
        super().__init__(unit_name=name, **kwargs)
        if not categories:
            categories = {
                "assets": "Original datasets",
                "source": "Source of used data",
                "out": "Outputs",
            }
        self._category = categories

    @property
    def categories(self):
        return self._category

    def report_by_category(self):
        # TODO finish the function
        pass

    def dt(self, name):
        return self.get_item(name).obj

    def in_category(self, category):
        if category not in self.categories:
            False
        else:
            return True

    def add_item_from_dataframe(
        self,
        data,
        name,
        category="assets",
        rel_path_folder="",
        save=False,
        description="",
    ):
        if not self.in_category(category):
            raise ValueError(
                f"{category} not valid in {self.categories.keys()}."
            )
        path = self.return_or_add_dir(rel_path_folder)
        abs_path = os.path.join(path, f"{name}.csv")
        if save:
            data.to_csv(abs_path)

        item = DataItem(
            name=name,
            obj=data,
            abs_path=abs_path,
            category=category,
            description=description,
        )
        item.update_metadata("category", category)
        item.update_metadata("path", abs_path)
        self.add_item(item)
        return item

    def add_item_from_file(
        self,
        rel_path,
        name=None,
        category="assets",
        format="csv",
        description="",
        **kwargs,
    ):
        func = getattr(pd, f"read_{format}")
        path = os.path.join(self.path, rel_path)
        if os.path.isfile(path):
            self.log.info(f"Loading data from {rel_path}.")
        else:
            msg = f"Failed in loading data from {rel_path}."
            self.log.error(msg)
            raise FileExistsError(msg)
        data = func(path, **kwargs)
        if not name:
            name = os.path.basename(path).split(".")[0]
        rel_path_folder = os.path.dirname(rel_path)
        item = self.add_item_from_dataframe(
            data,
            name,
            rel_path_folder=rel_path_folder,
            category=category,
            description=description,
        )
        return item

    def load_from_pickle(self, filename):
        pass

    def dump_all(self, out_path):
        pass

    def process_dataset(self, data, how, name=None):
        pass

    def metadata(self, name=None):
        pass

    def report(self, show=True, show_notes=False, max_width=30):
        table = super().report(show=False, show_notes=show_notes)
        paths, categories = [], []
        for item in self.items:
            item = self.get_item(item)
            paths.append(item.rel_path)
            categories.append(item.category)
        table.add_column("Path", paths)
        table.add_column("Category", categories)
        table.max_width = max_width
        if show:
            print(table)
        else:
            return table

    pass
