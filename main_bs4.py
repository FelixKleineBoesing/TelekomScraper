from bs4 import BeautifulSoup


def parse_html_contents(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    # subset by div with id wrapper
    wrapper = soup.find("div", {"id": "wrapper"})
    # get the first div with a class that contains "feedback"
    feedback = wrapper.find("div", class_=lambda x: x and "feedback" in x)
    title = wrapper.find(["h2", "h3"]).text
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



if __name__ =="__main__":
    html_file = "data/f5a515d4-0af4-11ee-b481-4cedfb68e75a.html"
    parse_html_contents(html_file)
