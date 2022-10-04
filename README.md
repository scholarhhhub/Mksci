# MKSCI

A flexible project managing tools powered by Scholar Hub Team

## Introduction
This is a flexible project managing tools developed with Python.



## Preparation

- Python 3.9

- Git

- Command Line Tool

  

## Installation

The simplest way to install is to clone the entire repository:
```
git clone git@github.com:scholarhhhub/Mksci.git
```

Then enter the project:

```
cd Mksci
```

Then  install the dependencies required for this project:

```
pip3 install -r requirement.txt
```

Install  the project on your computer:

```
python3.9 setup.py install
```

Run `mksci ` to make sure the  project managing tool is  successfully installed on your computer:
```
Usage:
  mksci project new (<directory>)
  mksci project init
  mksci project refresh [<file> <config>]
  mksci -h | --help
  mksci --version
```



## Getting Started

Before using `mksci` tool, you should first set an environment variable`MKSCI_PATH` to store the system logs:

​	MacOS:

```
export MKSCI_PATH='/Users/scholarhhhub/mksci/log'
```

​	Windows:

```
set MKSCI_PATH='C:\scholarhhhub\mksci\log'
```

​	Linux:

```
export MKSCI_PATH='/root/scholarhhhub/mksci/log'
```

After setting up the environment variable, you can enter the following commad to create a new Mksci project named `example`:

```
mksci project new example
```

You will find a new directory named example created by the tool. In the directory there's a config file named `config.yaml`and a directory used for document storage. You can put the documents in `docs` directory so that they can be managed correctly.

If you already have a project directory, you can run `mksci project init` to initialize. Then you just need to move your documents into `docs`directory.




## Config File
This tool can help refresh the documents in `docs` directory according to the keys in the config file.

Here is the template of `config.yaml`:

```
# Project name
project:
  name: "Project Managing Tools"
  status: "Ongoing"
  start: 2022
  end: None

# Repository name
repo:
  name: "Python-Project-Template"
  owner: "SongshGeo"
  background: "fig@background"
  license: "MIT"
  introduction: "A toolbox for initialize a standard python project."

# contributors:
contributors:
  Shuang Song: True
  Shuai Wang: False

# dir structure
structure:
  data:
    source: local
    processed: local
    results: support

  docs:
    papers: main
    docs: support
    drafts: support

  figs:
    diagrams: support
    outputs: support
    resources: support

  tests: support
  notebooks: main
  reports: support

  main:
    modules: main
    tools: main

python:
  version: "3.x"

links:
  fig@background: "![background](https://gitee.com/SongshGeo/Picgo2/raw/master/uPic/background.jpeg)"
  github@songshgeo: "[my GitHub](https://github.com/SongshGeo)"
  researchgate@songshgeo: "https://www.researchgate.net/profile/Shuang-Song-14"

log:
  name: "project"
  path: ""
  LOG_FORMAT: "%(asctime)s %(name)s %(levelname)s %(filename)s %(message)s "
  DATE_FORMAT: '%Y-%m-%d  %H:%M:%S %a '
  cmd_level: "WARNING"
  file_level: "INFO"

# Set folder levels to each structure
folder_level:
  # main modules
  main:
    ignore: False
    doc: True
  # support
  support:
    ignore: False
    doc: False
  # local
  local:
    ignore: True
    doc: False

```

If you want to refresh the name of the project, you just need to use key`project:name` enclosed by `<%%>` in the document. We allow space between `<%%>`, like `<% project:name %>`, but we don't allow space in keys, like `<%project : name%>`

You can modify the config file according to your demands.



### Refresh Document

- Refresh a specific document (ex: example.txt) with default config file(`config.yaml`)

  ```
  mksci project refresh example.txt
  ```

  

- Refresh a specific document (ex: example.txt) with a cutomized config file(ex: example.yaml)

  ```
  mksci project refresh example.txt example.yaml
  ```

  Note:

  - All documents that you want to refresh should be put in `docs` directory.
  - If you don't add `<config>` argument in the command, it will be indentified with using default config file(`config.yaml`) to refresh document.

  

- Refresh all documents with a default config file

  ```
  mksci project refresh .
  ```

  



## Packages Used In the Project

- **Docopt**: https://github.com/docopt/docopt



## Q&A

If you have any questions or good suggestions, please don't hesitate to contact us via Email: scholarhhhub@gmail.com.

## Changelogs

🚀[Release page](https://github.com/scholarhhhub/Mksci/releases)

- **v0.0.1**: finish basic functionalities