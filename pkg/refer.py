import bibparser
import config
import os
import logging

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


def get_refer_config(path):
    return config.getConfig(path)


if __name__ == "__main__":  # pragma: no cover
    configs = get_refer_config("assets.yaml")
    # print(configs)
    if "refer:key_references" in configs.keys():
        path = configs["refer:key_references"]
        if os.path.exists((os.path.join(os.getcwd(), path))):
            bibdata = bibparser.get_bib(path).entries
            print(bibdata)
        else:
            logger.error("Can not find bib file {path}")
