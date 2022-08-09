import logging
import os
import uuid

from . import config, pattern

all_files = []

log_path = os.path.join(os.getcwd(), ".mksci")
if not os.path.exists(log_path):
    os.mkdir(log_path)
else:
    pass
logging.basicConfig(
    filename=os.path.join(log_path, "refresh.log"),
    format="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S ",
    level=logging.INFO,
)
logger = logging.getLogger()
KZT = logging.StreamHandler()
KZT.setLevel(logging.DEBUG)
logger.addHandler(KZT)
logging.basicConfig(
    filename=os.path.join(log_path, "refresh.log"),
    format="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S ",
    level=logging.INFO,
)
logger = logging.getLogger()
KZT = logging.StreamHandler()
KZT.setLevel(logging.DEBUG)


# config_name为config.yaml绝对路径
def refresh_file(path, file, config_name):
    # Load config
    config_path = os.path.join(os.getcwd(), config_name)
    configs = config.getConfig(config_path)

    # get file name, generate uuid.
    filename = os.path.basename(file)
    suffix = filename.split(".")[1]
    filename = filename.split(".")[0]
    uuId = str((uuid.uuid1())).replace("-", "")[:13]

    # Refreshed new file
    newfile = filename + "_" + uuId + "." + suffix
    generated_path = os.path.join(path, "generated")
    if filename == "":
        return
    else:
        pass
    if not os.path.exists(generated_path):
        os.mkdir(generated_path)
    else:
        pass
    newfile_path = os.path.join(generated_path, newfile)
    # print(generated_path, newfile_path)
    # print(configs)
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    # print(configs)
    for ck in configs.keys():
        cv = str(configs.get(ck))
        # print(ck,cv)
        # 这里用一下正则吧，不要替换，容易出现空格什么之类的问题
        _, reg_pattern = pattern.get_doc_pattern(ck)
        text = pattern.replace_with_pattern(reg_pattern, cv, text)
        # text = text.replace(pattern, cv)
    with open(newfile_path, "w", encoding="utf-8") as f:
        f.write(text)
    # logger.info(f"{newfile}={os.path.basename(file)}+{config_name}")
    # print("newfile1:", newfile)
    return newfile


def getFiles(path):
    if not os.path.isdir(path):
        raise FileNotFoundError(
            f"{os.path.dirname(path)} is not a Mksci project directory. Please run 'mksci project init' first."
        )
    else:
        file_list = os.listdir(path)
        for file in file_list:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                getFiles(file_path)
            else:
                all_files.append(file_path)


def refresh_single_file(path, file, config_name):
    newfile = refresh_file(path, file, config_name)
    logger.info(f"{newfile}={os.path.basename(file)}+{config_name}")


def refresh_all(config_name):
    dir_path = os.getcwd()
    docs_path = os.path.join(dir_path, "docs")
    # config_path = os.path.join(dir_path, "config.yaml")
    # config_name = "config.yaml"
    getFiles(docs_path)
    # print(all_files)
    for file in all_files:
        if "generated" not in file and ".mksci" not in file:
            newfile = refresh_file(docs_path, file, config_name)
            # print("newfile2:", newfile)
            # logger.info(f"{newfile}={os.path.basename(file)}+{config_name}")
            if newfile is None:
                continue
            else:
                # pass
                logger.info(
                    f"{newfile}={os.path.basename(file)}+{config_name}"
                )


# 测试代码
if __name__ == "__main__":  # pragma: no cover
    refresh_all()
