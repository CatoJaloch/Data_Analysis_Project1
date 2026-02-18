import requests
import pandas as pd
from loguru import logger
import json

api_v3_base_url = "https://f3jmrf22mp.eu-west-1.awsapprunner.com/api/v3"
api_v3_key = "fAS|7V?aS3!%C;yk:fC_GQc6gKxEPxCfGcz~n-m`F:Y1]/abo)eF<d49A$eW(#CL+{oN^|M"


def get_fields(customer_id):
    """
    Get field details based on a farm

    :param customer_id: id of the farm
    """

    response: requests.Response = requests.get(
        url=f"{api_v3_base_url}/fields?farm_id={customer_id}&skip=0&limit=1000",
        params={"customer_id": customer_id},
        headers={"x-api-key": api_v3_key},
        timeout=60,
    )
    try:
        if response.status_code != 200:
            logger.error(
                f"API request failed with status {response.status_code}: {response.content}"
            )
            return pd.DataFrame()

        data = json.loads(response.content.decode("utf-8"))

        if not data:
            return []

        results = []

        for item in data:
            # Skip any strings or wrong formats
            if not isinstance(item, dict):
                logger.warning(f"Skipping non-dict item in API response: {item}")
                continue

            results.append(
                {
                    "field": item.get("name"),
                    "field_id": item.get("id"),
                    "variety_id": item.get("variety_id"),
                    "avg_img_bed_length": item.get("avg_img_bed_length"),
                    "area_msqr": item.get("area_msqr"),
                    "image_bed_number": item.get("image_bed_number"),
                    "location": item.get("location"),
                }
            )

        return results

    except Exception as e:
        logger.error(f"Unexpected error in get_varieties: {e}")
        return []


# Run the script
# STEPS
# 1. First, install pandas, requests and loguru: pip install pandas requests loguru
# 2. Use any of the customer ids:
#  4 = AAA Flowers
#  5 = Maasai Flowers (Sian)
#  6 = Mount Elgon Orchaards
#  19  = Golden Tulip Farm
#  20 = Rainforest Farmlands

# Run the script to get the results. You can save as csv

fields = get_fields(5)
fields_df = pd.DataFrame(fields)
print(fields_df.head())        