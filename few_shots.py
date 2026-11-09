import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        # Create empty dataframe instead of None
        self.df = pd.DataFrame()
        self.unique_tags = []

        # Load data
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Convert JSON to DataFrame
        self.df = pd.json_normalize(data)

        # Check required columns exist
        required_columns = ["line_count", "tags", "language"]

        for col in required_columns:
            if col not in self.df.columns:
                raise KeyError(f"Missing column: {col}")

        # Add length category column
        self.df["length"] = self.df["line_count"].apply(
            self.categorize_length
        )

        # Collect unique tags safely
        all_tags = []

        for tags in self.df["tags"]:
            if isinstance(tags, list):
                all_tags.extend(tags)

        self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (
                self.df["tags"].apply(
                    lambda tags: tag in tags
                    if isinstance(tags, list)
                    else False
                )
            )
            & (self.df["language"] == language)
            & (self.df["length"] == length)
        ]

        return df_filtered.to_dict(orient="records")

    @staticmethod
    def categorize_length(line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()

    # Print all available tags
    print("Available Tags:")
    print(fs.get_tags())

    # Filter posts
    posts = fs.get_filtered_posts(
        "Large",
        "Hinglish",
        "Job Search"
    )

    print("\nFiltered Posts:")
    print(posts)