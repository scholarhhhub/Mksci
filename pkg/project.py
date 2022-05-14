import logging
import os
from shutil import copyfile


def new(output_dir=""):
    log_path = os.path.join(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "log"
    )
    logging.basicConfig(
        filename=os.path.join(log_path, "new.log"),
        format="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S ",
        level=logging.INFO,
    )
    logger = logging.getLogger()
    KZT = logging.StreamHandler()
    KZT.setLevel(logging.DEBUG)
    logger.addHandler(KZT)

    dir_path = os.getcwd()
    dirname = output_dir
    output_dir = os.path.join(dir_path, dirname)
    mksci_config = os.path.join(output_dir, ".mksci")
    if len(output_dir) > 1:
        if not os.path.exists(output_dir):
            logger.info(f"Creating project directory: {output_dir}")
            os.mkdir(output_dir)
            os.mkdir(mksci_config)
            config_path = os.path.join(output_dir, "config.yaml")
            template_path = os.path.join(
                os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
                "template.yaml",
            )
            logger.info(f"Writing initial config yaml: {config_path}")
            # copyfile("../template.yaml",config_path)
            copyfile(template_path, config_path)
        else:
            logger.error(f"Project {output_dir} already exists.")
            # return
    else:
        logger.error("Please enter project name.")

    docs_path = os.path.join(output_dir, "docs")
    if not os.path.exists(docs_path):
        os.mkdir(docs_path)
    else:
        None


def init():
    log_path = os.path.join(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "log"
    )
    logging.basicConfig(
        filename=os.path.join(log_path, "init.log"),
        format="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S ",
        level=logging.INFO,
    )
    logger = logging.getLogger()
    KZT = logging.StreamHandler()
    KZT.setLevel(logging.DEBUG)
    logger.addHandler(KZT)
    dir_path = os.getcwd()
    config_path = os.path.join(dir_path, "config.yaml")
    mksci_config = os.path.join(dir_path, ".mksci")
    template_path = os.path.join(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
        "template.yaml",
    )
    if not os.path.exists(mksci_config):
        os.mkdir(mksci_config)
    else:
        None
    if os.path.exists(config_path):
        logger.error(f"Project {dir_path} already exists.")
    else:
        logger.info(f"Writing initial config yaml: {config_path}")
        copyfile(template_path, config_path)

    docs_path = os.path.join(dir_path, "docs")
    if not os.path.exists(docs_path):
        os.mkdir(docs_path)
    else:
        None


# 测试代码
if __name__ == "__main__":
    new("testproject")
    init()
