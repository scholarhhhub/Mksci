"""Project Managing Tools
Usage:
  mksci project new (<directory>)
  mksci project init
  mksci project refresh [<file> <config>]
  mksci -h | --help
  mksci --version

Options:
  -h --help     帮助.
  -v --version     查看版本号.
"""
import os

import init
import project
import refresh
from docopt import docopt


def cli():
    arguments = docopt(__doc__, version=init.__version__)
    if arguments.get("new"):
        dir_path = arguments["<directory>"]
        print(arguments["<directory>"])
        project.new(dir_path)
    elif arguments.get("init"):
        project.init()
    elif arguments.get("refresh"):
        if arguments["<file>"]:
            filename = arguments["<file>"]
            dir_path = os.getcwd()
            docs_path = os.path.join(dir_path, "docs")
            if arguments["<config>"]:
                config_name = arguments["<config>"]
            else:
                config_name = "config.yaml"
            file = os.path.join(docs_path, filename)
            if os.path.exists(file):
                refresh.refreshFile(docs_path, file, config_name)
            else:
                raise FileNotFoundError(
                    f"{filename} cannot be found in doc folder. Please move it into doc folder."
                )
        else:
            refresh.refreshAll()
    else:
        pass


if __name__ == "__main__":  # pragma: no cover
    cli()
