from driving_licence.generator import DrivingLicenceGenerator

from fastapi import FastAPI

from driving_licence.request import DrivingLicenseRequestModel

driving_licence_app = FastAPI()


@driving_licence_app.get("/")
def read_root():
    return {"Ping": "Pong!"}


@driving_licence_app.post("/license")
def generate_license(driving_licence_model: DrivingLicenseRequestModel) -> dict[str, str]:
    data = list(driving_licence_model.dict().values())
    return {"license": DrivingLicenceGenerator().generate(data=data)}
