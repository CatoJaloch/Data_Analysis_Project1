import requests
import pandas as pd
from loguru import logger
import json

api_v3_base_url = "https://f3jmrf22mp.eu-west-1.awsapprunner.com/api/v3"
api_v3_key = "fAS|7V?aS3!%C;yk:fC_GQc6gKxEPxCfGcz~n-m`F:Y1]/abo)eF<d49A$eW(#CL+{oN^|M"


def get_farms():
    response = requests.get(
        f"{api_v3_base_url}/farms",
        headers={"x-api-key": api_v3_key},
        timeout=60,
    )
    return response.json() if response.status_code == 200 else []


def get_varieties():
    response = requests.get(
        f"{api_v3_base_url}/varieties",
        headers={"x-api-key": api_v3_key},
        timeout=60,
    )

    data = response.json() if response.status_code == 200 else[]
    return {
        item.get("id"): {
            "variety_name": item.get("name"),
            "variety_type": item.get("type"),
        }
        for item in data
        if isinstance(item, dict)
    }


def get_fields(customer_id):
    response = requests.get(
        url=f"{api_v3_base_url}/fields?farm_id={customer_id}&skip=0&limit=1000",
        headers={"x-api-key": api_v3_key},
        timeout=60,
    )
    if response.status_code == 404:
        logger.warning(f"No fields found for farm_id {customer_id}")
        return []

    if response.status_code != 200:
        logger.error(f"API request failed: {response.content}")
        return []

    data = json.loads(response.content.decode("utf-8"))
    results = []

    for item in data:
        if not isinstance(item, dict):
            continue

        results.append(
            {
                "field_name": item.get("name"),
                "field_id": item.get("id"),
                "variety_id": item.get("variety_id"),
                "image_bed_number": item.get("image_bed_number"),
                "area_msqr": item.get("area_msqr"),
            }
        )

    return results


def classify_field_size(area):
    if area == 0:
        return "Uncategorised"
    if 1 < area < 5000:
        return "small"
    elif 5001< area < 70000:
        return "medium"
    else:
        return "large"


farms = get_farms()
varieties = get_varieties()

rows = []

for farm in farms:
    farm_id = farm.get("id")
    farm_name = farm.get("name")

    fields = get_fields(farm_id)

    for field in fields:
        variety_info = varieties.get(field["variety_id"], {})

        rows.append(
            {
                "farm_id": farm_id,
                "farm_name": farm_name,
                "field_name": field["field_name"],
                "field_id": field["field_id"],
                "variety_id": field["variety_id"],
                "variety_name": variety_info.get("variety_name"),
                "variety_type": variety_info.get("variety_type"),
                "image_bed_number": field["image_bed_number"],
                "area_msqr": field["area_msqr"],
                "field_size_category": classify_field_size(field["area_msqr"]),
            }
        )

df = pd.DataFrame(rows)
df.to_csv("farm_field_variety_summary.csv", index=False)
df.to_excel("farm_field_variety_summary.xlsx", index=False)

print("CSV saved: farm_field_variety_summary.csv")
print("Excel saved: farm_field_variety_summary.xlsx")
