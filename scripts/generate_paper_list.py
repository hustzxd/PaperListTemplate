import os
import shutil
import sys

import google.protobuf as pb
import google.protobuf.text_format
import pandas as pd

sys.path.append("./")

from proto import efficient_paper_pb2 as eppb

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
        "publication",  # ICLR
        "year", # 2022
        "code",  # [type](url)
        "note",  # [](url)
    ]
    pinfos = readMeta()
    data_list = []

    year_cls = {}
    year_out_cls = {}
    pub_cls = {}
    inst_cls = {}
    author_cls = {}
    keyword_cls = {}

    for pinfo, f in pinfos:
        if pinfo.paper.abbr:
            meta = "[{}](./meta/{})".format(pinfo.paper.abbr, f)
            meta_inner = "[{}](../../meta/{})".format(pinfo.paper.abbr, f)
        else:
            meta = "[m](./meta/{})".format(f)
            meta_inner = "[m](../../meta/{})".format(f)

        title = ""
        title += pinfo.paper.title
        if pinfo.paper.url:
            title = "[{}]({})".format(title, pinfo.paper.url)

        pub = pinfo.pub.where
        year = pinfo.pub.year

        code = ""
        codetype = pinfo.code.type if pinfo.code.type else "code"

        if pinfo.code.url:
            code = "[{}]({})".format(codetype, pinfo.code.url)

        note = ""
        note_inner = ""
        if pinfo.note.url:
            if pinfo.note.url.endswith(".md"):
                note = "[note](./notes/{})".format(pinfo.note.url)
                note_inner = "[note](../../notes/{})".format(pinfo.note.url)
            else:
                note = "[note]({})".format(pinfo.note.url)
                note_inner = note

        data = [meta, title, pub, year, code, note]
        data_inner = [meta_inner, title, pub, year, code, note_inner]

        if pinfo.pub.year:
            if pinfo.pub.year in year_cls:
                year_cls[pinfo.pub.year].append(data_inner)
            else:
                year_cls[pinfo.pub.year] = [data_inner]

        if pinfo.pub.year in year_out_cls:
            year_out_cls[pinfo.pub.year].append(data)
        else:
            year_out_cls[pinfo.pub.year] = [data]
        
        if pinfo.pub.where:
            pub_ = pinfo.pub.where.replace(" ", "-")
            if pub_ in pub_cls:
                pub_cls[pub_].append(data_inner)
            else:
                pub_cls[pub_] = [data_inner]

        if pinfo.paper.institutions:
            for inst in pinfo.paper.institutions:
                inst = inst.replace(" ", "-")
                if inst in inst_cls:
                    inst_cls[inst].append(data_inner)
                else:
                    inst_cls[inst] = [data_inner]

        if pinfo.paper.authors:
            for author in pinfo.paper.authors:
                author = author.replace(" ", "-")
                if author in author_cls:
                    author_cls[author].append(data_inner)
                else:
                    author_cls[author] = [data_inner]

        if pinfo.keyword.words:
            for word in pinfo.keyword.words:
                word = word.replace(" ", "-")
                if word in keyword_cls:
                    keyword_cls[word].append(data_inner)
                else:
                    keyword_cls[word] = [data_inner]

        data_list.append(data)

    fast_search = "fast_search"
    # os.removedirs(fast_search)
    shutil.rmtree(fast_search)
    if not os.path.exists(fast_search):
        os.makedirs(fast_search)
    # search by year
    year_path = os.path.join(fast_search, "year")
    if not os.path.exists(os.path.join(year_path)):
        os.makedirs(year_path)

    for year, data in year_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        with open("{}/{}.md".format(year_path, year), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(year_path, year))

    # search by publication
    pub_path = os.path.join(fast_search, "pub")
    if not os.path.exists(os.path.join(pub_path)):
        os.makedirs(pub_path)

    for pub, data in pub_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        with open("{}/{}.md".format(pub_path, pub), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(pub_path, pub))

    # search by institutions
    inst_path = os.path.join(fast_search, "inst")
    if not os.path.exists(os.path.join(inst_path)):
        os.makedirs(inst_path)

    for inst, data in inst_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        with open("{}/{}.md".format(inst_path, inst), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(inst_path, inst))

    # search by authors
    author_path = os.path.join(fast_search, "author")
    if not os.path.exists(os.path.join(author_path)):
        os.makedirs(author_path)

    for key, data in author_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        with open("{}/{}.md".format(author_path, key), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(author_path, key))

    # search by key words
    keyword_path = os.path.join(fast_search, "keyword")
    if not os.path.exists(os.path.join(keyword_path)):
        os.makedirs(keyword_path)

    for key, data in keyword_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        with open("{}/{}.md".format(keyword_path, key), "w") as wf:
            wf.write(df_.to_markdown())
        print("Generate {}/{}.md done".format(keyword_path, key))
    
    # 
    df = pd.DataFrame(data_list, columns=columns)
    df = df.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
    # markdown = """# EfficientPaper\nPruning, Quantization and efficient-inference/training paper list.\n"""
    with open("README_base.md") as rf:
        markdown = rf.read()
    markdown += "\n\n"
    
    # add fast search
    byclasses = os.listdir('./fast_search')
    markdown += "## Fast Search \n"
    # markdown += "<details><summary><b>search by classify</b></summary> \n"
    # markdown += "<p>\n"

    for byclass in byclasses:
        markdown += "<details><summary><b>{}</b></summary> \n".format(byclass)
        markdown += "<p>\n\n"
        ks = os.listdir('./fast_search/{}'.format(byclass))
        ks.sort()
        for k in ks:
            markdown += "1. [{}](./fast_search/{}/{}) \n".format(k, byclass, k)
        markdown += "</p>\n"
        markdown += "</details>\n"
    # markdown += "</p>\n"
    # markdown += "</details>\n\n"

    markdown += "\n## Paper List\n\n"
    year_out_cls = dict(sorted(year_out_cls.items(), reverse=True))
    for year, data in year_out_cls.items():
        df_ = pd.DataFrame(data, columns=columns)
        df_ = df_.sort_values(by=["year", "publication", "meta"], ascending=True).reset_index(drop=True)
        markdown += "\n### {}\n\n".format(year)
        markdown += df_.to_markdown()
    # markdown += df.to_markdown()
    with open("README.md", "w") as wf:
        wf.write(markdown)
    print("Generate README.md done")


if __name__ == "__main__":
    main()
