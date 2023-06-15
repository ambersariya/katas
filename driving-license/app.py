from driving_license.generator import DrivingLicenseGenerator

from fastapi import FastAPI

from driving_license.request import DrivingLicenseRequestModel

driving_license_app = FastAPI()


@driving_license_app.get("/")
def read_root():
    return {"Ping": "Pong!"}


@driving_license_app.post("/license")
def generate_license(driving_license_model: DrivingLicenseRequestModel) -> dict[str, str]:
    data = list(driving_license_model.dict().values())
    return {"license": DrivingLicenseGenerator().generate(data=data)}
