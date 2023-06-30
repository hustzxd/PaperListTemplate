import os
import pandas as pd
import google.protobuf as pb
import google.protobuf.text_format
from proto import efficient_paper_pb2 as eppb
import ipdb
import shutil

def readMeta():
    pinfos = []
    for f in os.listdir("./meta"):
        print(f)
        pinfo = eppb.PaperInfo()
        with open(os.path.join("./meta", f), "r") as rf:
            pb.text_format.Merge(rf.read(), pinfo)
        pinfos.append((pinfo, f))
    return pinfos


def main():
    columns = [
        "meta",
        "title",  # (abbr) [title](url)
        "publication",  # ICLR-2022
        "code",  # [type](url)
        "note",  # [](url)
    ]
    pinfos = readMeta()
    data_list = []

    year_cls = {}
    pub_cls = {}
    inst_cls = {}

    for pinfo, f in pinfos:
        meta = "[m](./meta/{})".format(f)

        title = ""
        if pinfo.paper.abbr:
            title += " ({}) ".format(pinfo.paper.abbr)
        title += pinfo.paper.title
        if pinfo.paper.url:
            title = "[{}]({})".format(title, pinfo.paper.url)

        pub = ""
        if pinfo.pub.where and pinfo.pub.year:
            pub = "{}-{}".format(pinfo.pub.where, pinfo.pub.year)
        elif pinfo.pub.where:
            pub = pinfo.pub.where
        elif pinfo.pub.year:
            pub = pinfo.pub.year

        code = ""
        codetype = pinfo.code.type if pinfo.code.type else "code"

        if pinfo.code.url:
            code = "[{}]({})".format(codetype, pinfo.code.url)

        note = ""
        if pinfo.note.url:
            note = "[note]({})".format(pinfo.note.url)

        data = [meta, title, pub, code, note]

        if pinfo.pub.year:
            if pinfo.pub.year in year_cls:
                year_cls[pinfo.pub.year].append(data)
            else:
                year_cls[pinfo.pub.year] = [data]

        if pinfo.pub.where:
            if pinfo.pub.where in pub_cls:
                pub_cls[pinfo.pub.where].append(data)
            else:
                pub_cls[pinfo.pub.where] = [data]
            
        if pinfo.paper.institutions:
            for inst in pinfo.paper.institutions:
                if inst in inst_cls:
                    inst_cls[inst].append(data)
                else:
                    inst_cls[inst] = [data]

        data_list.append(data)
    df = pd.DataFrame(data_list, columns=columns)
    markdown = '''# EfficientPaper\nPruning, Quantization and efficient-inference/training paper list.\n'''
    markdown += df.to_markdown()
    with open("README.md", "w") as wf:
        wf.write(markdown)
    print("Generate README.md done")

    fast_search = "fast_search"
    # os.removedirs(fast_search)
    shutil.rmtree(fast_search)
    if not os.path.exists(fast_search):
        os.makedirs(fast_search)   
    # search by year
    year_path = os.path.join(fast_search, 'year')
    if not os.path.exists(os.path.join(year_path)):
        os.makedirs(year_path)

    for year, data in year_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        with open("{}/{}.md".format(year_path, year), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(year_path, year))
        
    # search by publication
    pub_path = os.path.join(fast_search, 'pub')
    if not os.path.exists(os.path.join(pub_path)):
        os.makedirs(pub_path)

    for pub, data in pub_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        with open("{}/{}.md".format(pub_path, pub), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(pub_path, pub))

    # search by institutions
    inst_path = os.path.join(fast_search, 'inst')
    if not os.path.exists(os.path.join(inst_path)):
        os.makedirs(inst_path)

    for inst, data in inst_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        with open("{}/{}.md".format(inst_path, inst), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(inst_path, inst))


if __name__ == "__main__":
    main()
