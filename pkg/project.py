import os
import urllib.request
from . import logger
from shutil import copyfile


def downloadTemplate(url, path):
    result = urllib.request.urlretrieve(
        url,
        filename=path,
    )


def new(output_dir=""):
    log_path = os.path.join(os.environ["MKSCI_PATH"], "new.log")
    new_logger = logger.get_logger(log_path)

    dir_path = os.getcwd()
    dirname = output_dir
    output_dir = os.path.join(dir_path, dirname)
    mksci_config = os.path.join(output_dir, ".mksci")
    if len(output_dir) > 1:
        if not os.path.exists(output_dir):
            new_logger.info(f"Creating project directory: {output_dir}")
            os.mkdir(output_dir)
            os.mkdir(mksci_config)
            config_path = os.path.join(output_dir, "config.yaml")

            template_path = (
                "https://mksci.oss-cn-beijing.aliyuncs.com/template.yaml"
            )
            new_logger.info(f"Writing initial config yaml: {config_path}")
            # copyfile("../template.yaml",config_path)
            # copyfile(template_path, config_path)
            downloadTemplate(template_path, config_path)
        else:
            new_logger.error(f"Project {output_dir} already exists.")
            # return
    else:
        new_logger.error("Please enter project name.")

    docs_path = os.path.join(output_dir, "docs")
    if not os.path.exists(docs_path):
        os.mkdir(docs_path)
    else:
        pass


def init():
    log_path = os.path.join(os.environ["MKSCI_PATH"], "init.log")
    init_logger = logger.get_logger(log_path)
    print(logger.handlers)

    dir_path = os.getcwd()
    config_path = os.path.join(dir_path, "config.yaml")
    mksci_config = os.path.join(dir_path, ".mksci")
    template_path = "https://mksci.oss-cn-beijing.aliyuncs.com/template.yaml"
    if not os.path.exists(mksci_config):
        os.mkdir(mksci_config)
    else:
        None
    if os.path.exists(config_path):
        init_logger.error(f"Project {dir_path} already exists.")
    else:
        init_logger.info(f"Writing initial config yaml: {config_path}")
        # copyfile(template_path, config_path)
        downloadTemplate(template_path, config_path)

    docs_path = os.path.join(dir_path, "docs")
    if not os.path.exists(docs_path):
        os.mkdir(docs_path)
    else:
        pass


# 测试代码
if __name__ == "__main__":
    new("testproject1")
    # init()
