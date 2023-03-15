# Say we have a number of records per year
# And we need to get the percentage breakdown/makeup of a category for each year
# If we leave the column name as "SomeCategory", but it shows a percent, then we need to rename in order to keep the category's name

x = pd.DataFrame(df.groupby("year").some_category.value_counts(normalize=True).round(2))
x.columns = ["percentage"]
x.reset_index()



# Interesting approach but the scale
# Scale might be an issue if the minority classes are significantly smaller
x = pd.DataFrame(df.groupby("year").some_category.value_counts())
x.columns = ["count"]
x.reset_index(inplace=True)
sns.barplot(x="year", y="count", hue="some_category", data=x)


