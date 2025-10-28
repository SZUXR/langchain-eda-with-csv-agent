# prepare_data.py
import seaborn as sns
df = sns.load_dataset("taxis")
df.to_csv("taxis.csv", index=False)
print("Saved taxis.csv")