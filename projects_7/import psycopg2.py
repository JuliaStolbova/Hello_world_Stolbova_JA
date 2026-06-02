import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres_task",
        password="student",
        database="student"
    )
    print("✓ Подключение установлено")

    query = """
    SELECT
        pr.price,
        p.name AS product_name,
        p.category
    FROM prices pr
    JOIN products p
        ON pr.product_id = p.id
    """

    df = pd.read_sql_query(query, connection)

    if df.empty:
        raise ValueError("Запрос вернул пустой результат")

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price", "product_name", "category"])

    mean_price = df["price"].mean()
    median_price = df["price"].median()
    std_price = df["price"].std()
    q1 = df["price"].quantile(0.25)
    q2 = df["price"].quantile(0.50)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print("\n=== Статистики по ценам ===")
    print(f"Среднее: {mean_price:.2f} руб.")
    print(f"Медиана: {median_price:.2f} руб.")
    print(f"Ст. отклонение: {std_price:.2f} руб.")
    print(f"Q1: {q1:.2f} руб.")
    print(f"Q2: {q2:.2f} руб.")
    print(f"Q3: {q3:.2f} руб.")
    print(f"IQR: {iqr:.2f} руб.")

    anomalies = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]

    if anomalies.empty:
        print("\nАномалии не обнаружены.")
    else:
        print("\nАномальные записи:")
        print(
            anomalies[["product_name", "category", "price"]]
            .sort_values("price", ascending=False)
            .to_string(index=False)
        )

    category_stats = (
        df.groupby("category")["price"]
        .agg(count="count", mean="mean", median="median", std="std")
        .round(2)
        .sort_values("mean", ascending=False)
    )

    print("\n=== Статистика по категориям ===")
    print(category_stats)

    top_categories = category_stats.head(10)
    category_counts = df["category"].value_counts().head(10)

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
        "figure.dpi": 130,
    })

    fig = plt.figure(figsize=(16, 10))
    fig.suptitle("Анализ цен товаров", fontsize=15, fontweight="bold", y=1.02)

    gs = gridspec.GridSpec(
        2, 2, figure=fig,
        height_ratios=[5, 4],
        width_ratios=[2, 2],
        hspace=0.4, wspace=0.28
    )

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    counts_by_category = df["category"].value_counts()
    colors = ["#4a90d9"] * len(counts_by_category)

    ax1.hist(df["price"], bins=20, color="#4a90d9", edgecolor="white")
    ax1.axvline(mean_price, color="crimson", linestyle="--", linewidth=1.5, label=f"Среднее: {mean_price:.2f}")
    ax1.axvline(median_price, color="green", linestyle="--", linewidth=1.5, label=f"Медиана: {median_price:.2f}")
    ax1.axvline(q1, color="orange", linestyle=":", linewidth=1.5, label=f"Q1: {q1:.2f}")
    ax1.axvline(q3, color="purple", linestyle=":", linewidth=1.5, label=f"Q3: {q3:.2f}")
    ax1.set_title("Распределение цен")
    ax1.set_xlabel("Цена, руб.")
    ax1.set_ylabel("Количество")
    ax1.legend(fontsize=8)

    ax2.boxplot(df["price"], vert=True)
    ax2.axhline(lower_bound, color="red", linestyle="--", linewidth=1, label="Нижняя граница IQR")
    ax2.axhline(upper_bound, color="red", linestyle="--", linewidth=1, label="Верхняя граница IQR")
    ax2.set_title("Boxplot цен")
    ax2.set_ylabel("Цена, руб.")
    ax2.legend(fontsize=8)

    ax3.bar(top_categories.index.astype(str), top_categories["mean"], color="#72B7B2", edgecolor="white")
    ax3.set_title("Средняя цена по категориям")
    ax3.set_xlabel("Категория")
    ax3.set_ylabel("Средняя цена, руб.")
    ax3.tick_params(axis="x", rotation=45)

    ax4.bar(category_counts.index.astype(str), category_counts.values, color="#f0ad4e", edgecolor="white")
    ax4.set_title("Количество записей по категориям")
    ax4.set_xlabel("Категория")
    ax4.set_ylabel("Количество")
    ax4.tick_params(axis="x", rotation=45)

    stats_text = (
        f"Всего записей: {len(df)}\n"
        f"Среднее: {mean_price:.2f}\n"
        f"Медиана: {median_price:.2f}\n"
        f"Q1: {q1:.2f}\n"
        f"Q3: {q3:.2f}\n"
        f"IQR: {iqr:.2f}"
    )

    ax2.text(
        1.05, 0.95, stats_text,
        transform=ax2.transAxes,
        va="top", ha="left", fontsize=8,
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "lightyellow", "edgecolor": "lightgray"}
    )

    if anomalies.empty:
        fig.text(
            0.5, -0.02,
            "Аномалии не обнаружены по правилу IQR.",
            ha="center", fontsize=9, color="darkgreen"
        )
    else:
        fig.text(
            0.5, -0.02,
            f"Аномалии обнаружены: {len(anomalies)} записей вне границ IQR.",
            ha="center", fontsize=9, color="darkred"
        )

    plt.tight_layout()
    plt.savefig("student_charts.png", bbox_inches="tight", dpi=150)
    print("✓ График сохранён: student_charts.png")
    plt.show()

except Exception as error:
    print(f"Ошибка: {error}")

finally:
    if 'connection' in locals():
        connection.close()
        print("✓ Соединение закрыто")