import logging
import os
import urllib.request
from shutil import copyfile

oss_endpoint = "https://mksci.oss-cn-beijing.aliyuncs.com/"
# put all tuples of the files need to download from alicloud oss in list
# tuple elements:first element=the filename meeded to be saved to user local; the second element=file path in alicloud oss
config_list = [
    ("config.yaml", "config/config.yaml"),
    ("author.yaml", "config/author.yaml"),
]
docs_list = [
    ("readme_template.md", "doc/docs/readme_template.md"),
    ("paper_template.text", "doc/paper/paper_template.tex"),
    ("doc.yaml", "doc/doc.yaml"),
    (""),
]


def download_template(url, path):
    result = urllib.request.urlretrieve(
        url,
        filename=path,
    )


def download_config(osspath, filepath):
    url = oss_endpoint + osspath
    # file_path = os.path.join(path, filename)
    download_template(url, filepath)


def new(output_dir=""):
    log_path = os.path.join(os.environ["MKSCI_PATH"], "new.log")
    logging.basicConfig(
        filename=log_path,
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
    config_path = os.path.join(output_dir, "config")
    docs_path = os.path.join(output_dir, "docs")
    # if not os.path.exists(docs_path):
    #     os.mkdir(docs_path)
    # else:
    #     None
    if len(output_dir) > 1:
        if not os.path.exists(output_dir):
            logger.info(f"Creating project directory: {output_dir}")
            os.mkdir(output_dir)
            os.mkdir(mksci_config)
            os.mkdir(config_path)
            os.mkdir(docs_path)
            # config_path = os.path.join(output_dir, "config.yaml")
            # template_path = os.path.join(
            #     os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
            #     "template.yaml",
            # )
            # template_path = os.path.join(
            #     os.path.dirname(__file__),
            #     "template.yaml",
            # )

            for configg in config_list:
                logger.info(
                    f"Writing config yaml: {os.path.join(config_path,configg[0])}"
                )
                download_config(
                    configg[1], os.path.join(config_path, configg[0])
                )
            # copyfile("../template.yaml",config_path)
            # copyfile(template_path, config_path)
            # download_template(template_path, config_path)
        else:
            logger.error(f"Project {output_dir} already exists.")
            # return
    else:
        logger.error("Please enter project name.")


def init():
    log_path = os.path.join(os.environ["MKSCI_PATH"], "init.log")
    logging.basicConfig(
        filename=log_path,
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
    # template_path = os.path.join(
    #     os.path.dirname(os.path.abspath(os.path.dirname(__file__))),
    #     "template.yaml",
    # )
    # template_path = os.path.join(
    #     os.path.dirname(__file__),
    #     "template.yaml",
    # )
    template_path = "https://mksci.oss-cn-hangzhou.aliyuncs.com/template.yaml"
    if not os.path.exists(mksci_config):
        os.mkdir(mksci_config)
    else:
        None
    if os.path.exists(config_path):
        logger.error(f"Project {dir_path} already exists.")
    else:
        logger.info(f"Writing initial config yaml: {config_path}")
        # copyfile(template_path, config_path)
        download_template(template_path, config_path)

    docs_path = os.path.join(dir_path, "docs")
    if not os.path.exists(docs_path):
        os.mkdir(docs_path)
    else:
        None


# 测试代码
if __name__ == "__main__":
    new("testproject")
    # init()
