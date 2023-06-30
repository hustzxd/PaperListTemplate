import os
import pandas as pd
import google.protobuf as pb
import google.protobuf.text_format
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
        "title",  # (abbr) [title](url)
        "publication",  # ICLR-2022
        "code",  # [type](url)
        "note",  # [](url)
    ]
    pinfos = readMeta()
    data_list = []
    for pinfo, f in pinfos:
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

        data = [title, pub, pinfo.code.url, pinfo.note.url]
        data_list.append(data)
    df = pd.DataFrame(data_list, columns=columns)
    markdown = df.to_markdown()
    with open("README.md", "w") as wf:
        wf.write(markdown)


if __name__ == "__main__":
    main()
