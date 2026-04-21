import pandas as pd


def find_column(df: pd.DataFrame, possible_names: list[str]):
    column_map = {col.lower(): col for col in df.columns}
    for name in possible_names:
        if name.lower() in column_map:
            return column_map[name.lower()]
    return None


def analyze_question(df: pd.DataFrame, question: str):
    q = question.lower().strip()

    revenue_col = find_column(df, ["Revenue", "Sales", "Amount"])
    price_col = find_column(df, ["Price", "Unit Price", "Cost"])
    product_col = find_column(df, ["Product", "Product Name", "Item"])
    category_col = find_column(df, ["Category", "Category Name", "Segment"])
    date_col = find_column(df, ["Date", "Order Date", "Created At"])

    working_df = df.copy()

    if revenue_col:
        working_df[revenue_col] = pd.to_numeric(working_df[revenue_col], errors="coerce")
    if price_col:
        working_df[price_col] = pd.to_numeric(working_df[price_col], errors="coerce")

    if ("total revenue" in q or "total sales" in q) and revenue_col:
        total_revenue = working_df[revenue_col].sum(skipna=True)
        return {
            "type": "metric",
            "title": "Total Revenue",
            "value": float(total_revenue),
        }

    if ("average price" in q or "mean price" in q) and price_col:
        avg_price = working_df[price_col].mean(skipna=True)
        return {
            "type": "metric",
            "title": "Average Price",
            "value": float(avg_price),
        }

    if (
        ("top" in q or "highest" in q)
        and "product" in q
        and ("revenue" in q or "sales" in q)
        and product_col
        and revenue_col
    ):
        result = (
            working_df.groupby(product_col)[revenue_col]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )

        return {
            "type": "table_chart",
            "title": "Top Products by Revenue",
            "x": result[product_col].astype(str).tolist(),
            "y": result[revenue_col].fillna(0).tolist(),
            "table": result.to_dict(orient="records"),
            "chart_type": "bar",
        }

    if (
        ("category" in q or "segment" in q)
        and ("revenue" in q or "sales" in q or "compare" in q or "distribution" in q)
        and category_col
        and revenue_col
    ):
        result = (
            working_df.groupby(category_col)[revenue_col]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        return {
            "type": "table_chart",
            "title": "Revenue by Category",
            "x": result[category_col].astype(str).tolist(),
            "y": result[revenue_col].fillna(0).tolist(),
            "table": result.to_dict(orient="records"),
            "chart_type": "bar",
        }

    if (
        ("trend" in q or "monthly" in q or "over time" in q)
        and revenue_col
        and date_col
    ):
        temp_df = working_df.copy()
        temp_df[date_col] = pd.to_datetime(temp_df[date_col], errors="coerce")
        temp_df = temp_df.dropna(subset=[date_col])
        temp_df["Month"] = temp_df[date_col].dt.to_period("M").astype(str)

        result = (
            temp_df.groupby("Month")[revenue_col]
            .sum()
            .reset_index()
            .sort_values("Month")
        )

        return {
            "type": "table_chart",
            "title": "Monthly Revenue Trend",
            "x": result["Month"].astype(str).tolist(),
            "y": result[revenue_col].fillna(0).tolist(),
            "table": result.to_dict(orient="records"),
            "chart_type": "line",
        }

    return {
        "type": "summary",
        "title": "Dataset Summary",
        "columns": list(working_df.columns),
        "rows": int(len(working_df)),
        "preview": working_df.head(5).fillna("").to_dict(orient="records"),
    }