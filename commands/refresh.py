import os
import uuid

import config

all_files = []


def refresh(path, file, config_name):
    configs = config.getConfig(config_name)
    filename = os.path.basename(file)
    suffix = filename.split(".")[1]
    filename = filename.split(".")[0]
    newfile = filename + "_" + str(uuid.uuid1())[:13] + "." + suffix
    generated_path = os.path.join(path, "generated")
    if not os.path.exists(generated_path):
        os.mkdir(generated_path)
    else:
        None
    newfile_path = os.path.join(generated_path, newfile)
    print(generated_path, newfile_path)
    # print(configs)
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    # print(configs)
    for ck in configs.keys():
        cv = str(configs.get(ck))
        # print(ck,cv)
        pattern = "{%" + ck + "%}"
        text = text.replace(pattern, cv)
    with open(newfile_path, "w", encoding="utf-8") as f:
        f.write(text)


def getFiles(path):
    if not os.path.isdir(path):
        raise FileNotFoundError(f"{path} is not a folder.")
    else:
        file_list = os.listdir(path)
        for file in file_list:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                getFiles(file_path)
            else:
                all_files.append(file_path)


# 测试代码
dir_path = os.path.abspath(os.path.dirname(__file__))
docs_path = os.path.join(dir_path, "docs")
config_path = os.path.join(dir_path, "config.yaml")
getFiles(docs_path)
print(all_files)
for file in all_files:
    if not "generated" in file:
        refresh(docs_path, file, config_path)
