import os
import re
from unittest import result

import yaml

import config

import refresh

from deepmerge import always_merger


def load(path):
    result = config.read(path)
    return result


def dump(file, data):
    f = open(file, "w")
    yaml.dump(data, f)
    f.close()


def merge(dict1, dict2):
    result = always_merger.merge(dict1, dict2)
    # print(result)
    dump(r"merged.yaml", result)
    return result


def get_author(path):
    result = load(path)
    author_list = []
    for key in result.keys():
        author_list.append(key)
    result = config.getConfig(path)
    return author_list, result


# 测试代码
if __name__ == "__main__":  # pragma: no cover
    dict1 = load("config.yaml")
    dict2 = load("doc.yaml")
    result = merge(dict1, dict2)
    # config1 = config.getConfig("config.yaml")
    # config2 = config.getConfig("doc.yaml")
    config3 = config.getConfig("merged.yaml")
    # print(config3)
    # print(config1)
    # print(config2)
    # print(get_author("author.yaml"))
    author_list, result = get_author("author.yaml")
    print(author_list)
    print(result)
