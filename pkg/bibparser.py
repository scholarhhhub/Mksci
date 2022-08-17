import bibtexparser as bp
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


def get_bib(file):
    with open(file) as bibfile:
        parser = BibTexParser(common_strings=True)
        # parser = BibTexParser()  # 声明解析器类
        parser.customization = convert_to_unicode  # 将BibTeX编码强制转换为UTF编码
        # parser.common_strings = True
        bibdata = bp.load(bibfile, parser=parser)  # 通过bp.load()加载
        return bibdata


# 测试代码
if __name__ == "__main__":  # pragma: no cover
    bibdata = get_bib("references.bib")
    # 输出作者和DOI
    print(bibdata.entries[0]["author"])
    print(bibdata.entries[0]["doi"])
    print(bibdata.entries)
