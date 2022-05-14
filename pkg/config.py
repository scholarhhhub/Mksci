import os

import yaml


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)  # FullLoafer可以yaml解析变得安全
    return result


def getKV(dictionary, k, key, configs):
    v = dictionary.get(k)
    if key == "":
        ktemp = k
    else:
        ktemp = key + ":" + k
    if isinstance(v, dict):
        for vk in v.keys():
            getKV(v, vk, ktemp, configs)

    if isinstance(v, bool):
        if v:
            if key in configs.keys():
                configs[key] = configs[key] + "," + v
            else:
                configs[key] = v
            configs[key] = k
        else:
            None
    else:
        if key == "":
            ktemp = k
        else:
            ktemp = key + ":" + k
            if not isinstance(v, dict):
                if ktemp in configs.keys():
                    configs[ktemp] = configs[ktemp] + "," + v
                else:
                    configs[ktemp] = v
    return configs


def getConfig(config_name):
    # dir_path = os.path.abspath(os.path.dirname(__file__))
    dir_path = os.getcwd()
    config_path = os.path.join(dir_path, config_name)
    if os.path.exists(config_path):
        config = read(config_path)
    else:
        raise FileNotFoundError(
            f"{dir_path} is not a Mksci project directory.Please run 'mksci project init' first"
        )

    configs = {}
    for k in config.keys():
        configs = getKV(config, k, "", configs)

    return configs


# 测试代码
# config = getConfig("config.yaml")
# print(config)
