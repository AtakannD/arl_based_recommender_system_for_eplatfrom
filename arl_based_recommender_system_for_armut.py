import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

# Task 1.1
df = pd.read_csv(r"C:\Users\atakan.dalkiran\PycharmProjects\Association Rule Based Recommender System for e-platform\armut_data.csv")
df.head()


# Task 1.2
df["Service"] = [str(row[1]) + "_" + str(row[2]) for row in df.values]


# Task 1.3
df.info()
df["CreateDate"] = pd.to_datetime(df["CreateDate"])
df["NewDate"] = df["CreateDate"].dt.strftime("%Y-%m")
df["BasketId"] = [str(row[0]) + "_" + str(row[5]) for row in df.values]


# Task 2.1
invoice_product_df = df.groupby(["BasketId", "Service"])["Service"].count().unstack().fillna(0). \
    applymap(lambda x: 1 if x > 0 else 0)


# Task 2.2
frequent_itemsets = apriori(invoice_product_df,
                            min_support=0.01,
                            use_colnames=True)
rules = association_rules(frequent_itemsets,
                          metric="support",
                          min_threshold=0.01)


# Task 2.3


def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))
    return recommendation_list[:rec_count]


arl_recommender(rules, "2_0", 1)
