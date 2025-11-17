import csv
import json
from pathlib import Path
from typing import Dict, List


SALES_CSV = Path(__file__).with_name("sales.csv")
SUMMARY_JSON = Path(__file__).with_name("sales_summary.json")


def read_sales(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Не найден файл продаж: {path}")

    with path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def analyze_sales(rows: List[Dict[str, str]]) -> Dict[str, object]:
    total_revenue = 0.0
    products: Dict[str, Dict[str, float]] = {}

    for row in rows:
        product = row["product_name"]
        quantity = int(row["quantity"])
        price = float(row["price_per_unit"])
        revenue = quantity * price
        total_revenue += revenue

        if product not in products:
            products[product] = {"quantity": 0, "revenue": 0.0}

        products[product]["quantity"] += quantity
        products[product]["revenue"] += revenue

    top_by_quantity = max(products.items(), key=lambda item: item[1]["quantity"])
    top_by_revenue = max(products.items(), key=lambda item: item[1]["revenue"])

    return {
        "total_revenue": round(total_revenue, 2),
        "top_selling_product": {
            "name": top_by_quantity[0],
            "quantity": top_by_quantity[1]["quantity"],
        },
        "most_profitable_product": {
            "name": top_by_revenue[0],
            "revenue": round(top_by_revenue[1]["revenue"], 2),
        },
    }


def save_summary(summary: Dict[str, object], path: Path) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)


def main() -> None:
    rows = read_sales(SALES_CSV)
    summary = analyze_sales(rows)
    save_summary(summary, SUMMARY_JSON)
    print(f"Анализ завершен. Результаты сохранены в {SUMMARY_JSON.name}")


if __name__ == "__main__":
    main()

