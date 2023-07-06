import pandas as pd


def main():
    data = pd.read_json("data/cleaned_html.json")
    data["texts"] = data.texts.apply(lambda x: [t for t in x if t != "expand_outline-optimized"])
    data["texts"] = data["texts"].str.join(" ").replace("  ", " ")
    data.to_json("data/processed_html.json", orient="records")


if __name__ == "__main__":
    main()
    print("Done.")