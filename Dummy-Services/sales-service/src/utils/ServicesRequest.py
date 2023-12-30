import requests
from pydantic import Field
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./src/service.env",
        env_file_encoding="utf-8"
    )
    general: str = Field(...,alias="GENERAL_SERVICE")
    sales: str = Field(...,alias="SALES_SERVICE")
    aftersales: str = Field(...,alias="AFTERSALES_SERVICE")
    finance: str = Field(...,alias="FINANCE_SERVICE")
    common: str = Field(...,alias="COMMON_SERVICE")
    report: str = Field(...,alias="REPORT_SERVICE")

services = Settings()

# Please use this for making request among services (GET data)
def cross_service_request(service_endpoint: str, data_field: list):
    try:
        if service_endpoint.__contains__("general"):
            base_url = services.general_service
        else:
            print("What service ?") # Need to add more services condition with elif

        full_url = f"{base_url}/api/{service_endpoint}"
        response = requests.get(full_url)

        if response.status_code == 200:
            result = []
            for item in data_field:
                result.append(response.json()["data"][item])
            return result
        else:
            raise Exception(f"Error in sending request to: {full_url}, Status code: {response.status_code}")
    except Exception as error:
        return error