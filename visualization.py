import matplotlib.pyplot as plt


def plot_age_distribution(df):
    """Age Distribution"""

    plt.figure(figsize=(8, 5))
    plt.hist(df["Age"], bins=8)

    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Customers")
    plt.grid(True)

    plt.savefig("age_distribution.png")
    plt.show()


def plot_income_distribution(df):
    """Annual Income Distribution"""

    plt.figure(figsize=(8, 5))
    plt.hist(df["AnnualIncome"], bins=8)

    plt.title("Annual Income Distribution")
    plt.xlabel("Annual Income")
    plt.ylabel("Customers")
    plt.grid(True)

    plt.savefig("income_distribution.png")
    plt.show()


def plot_spending_distribution(df):
    """Spending Score Distribution"""

    plt.figure(figsize=(8, 5))
    plt.hist(df["SpendingScore"], bins=8)

    plt.title("Spending Score Distribution")
    plt.xlabel("Spending Score")
    plt.ylabel("Customers")
    plt.grid(True)

    plt.savefig("spending_distribution.png")
    plt.show()


def plot_customer_segments(df):
    """Customer Segmentation"""

    plt.figure(figsize=(8, 6))

    plt.scatter(
        df["AnnualIncome"],
        df["SpendingScore"],
        c=df["Cluster"],
        s=80
    )

    plt.title("Customer Segmentation")
    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.grid(True)

    plt.savefig("customer_segmentation.png")
    plt.show()


def plot_cluster_count(df):
    """Number of Customers in Each Cluster"""

    counts = df["CustomerSegment"].value_counts()

    plt.figure(figsize=(7, 5))

    plt.bar(counts.index, counts.values)

    plt.title("Customers per Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Number of Customers")

    plt.savefig("cluster_count.png")
    plt.show()