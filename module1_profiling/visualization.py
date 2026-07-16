import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


class Visualization:

    def missing_heatmap(self, df, output_path):

        if df.isnull().sum().sum() == 0:
            print("No missing values found.")
            return

        plt.figure(figsize=(10, 6))
        msno.heatmap(df)
        plt.title("Missing Value Heatmap")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def correlation_heatmap(self, df, output_path):

        numeric = df.select_dtypes(include=["number"])

        if numeric.shape[1] < 2:
            print("Skipping correlation heatmap")
            return

        plt.figure(figsize=(8,6))

        sns.heatmap(
            numeric.corr(),
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        plt.tight_layout()

        plt.savefig(output_path)

        plt.close()

    def outlier_plot(self, df, output_folder):

        numeric = df.select_dtypes(include=["number"])

        if numeric.empty:
            return

        for column in numeric.columns:

            plt.figure(figsize=(6,4))

            sns.boxplot(y=df[column])

            plt.title(column)

            plt.tight_layout()

            plt.savefig(
                output_folder / f"{column}_outliers.png"
            )

            plt.close()