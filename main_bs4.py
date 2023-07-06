from pathlib import Path

from bs4 import BeautifulSoup


def parse_html_contents(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")
        # subset by div with id wrapper
        wrapper = soup.find("div", {"id": "wrapper"})
        # get the first div with a class that contains "feedback"
        feedback = wrapper.find("div", class_=lambda x: x and "feedback" in x)
        title = wrapper.find(["h2", "h3"])
        if title is not None:
            title = title.text
        if feedback is not None:
            # pages like this: https://www.telekom.de/hilfe/geraete-zubehoer/handy-smartphone-tablet/reservierungs-service/vorteile-reservierungs-service
            # get the parent div of feedback that is an ul
            ul = feedback.find_parent("ul")
            ul.decompose()
            # find the title of the wrapper which is of type h2 or h3
            # extract all inner texts from the wrapper
            texts = wrapper.find_all(text=True, recursive=True)
        else:
            texts = wrapper.find_all(text=True, recursive=True)
        # remove line breaks
        texts = [t for t in texts if t != "\n"]
        return title, texts
    except Exception as e:
        print(f"Error while parsing html file {file_path} with error {e}")


def parse_all_files(path: str, id_url_matching: dict):
    # list all files in path
    data = []
    files = Path(path).glob("*.html")
    for file in files:
        id_ = str(file).split("\\")[-1].split(".")[0]
        html_content = parse_html_contents(str(file))
        if html_content is not None:
            title, texts = html_content
            data.append({"title": title, "texts": texts, "file": None, "url": id_url_matching[id_]})
    return data


def read_csv_and_convert_to_dict(file: str):
    data = {}
    with open(file, "r") as f:
        for line in f.readlines():
            if len(line) > 3:
                values = line.split(',')
                if len(values) == 2:
                    id_, url = values
                elif len(values) > 2:
                    id_ = values[0]
                    url = ",".join(values[1:])
                else:
                    raise ValueError(f"Line {line} not parsable")
                url = url.replace("\n", "").replace('"', "")
                data[id_] = url
    return data


if __name__ =="__main__":
    id_url_matching_file = "page_urls.csv"
    id_matching = read_csv_and_convert_to_dict(id_url_matching_file)
    data = parse_all_files("data/raw", id_matching)
    import json
    with open("data/cleaned_html.json", "w") as f:
        json.dump(data, f)
