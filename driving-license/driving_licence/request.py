from pydantic.main import BaseModel


class DrivingLicenseRequestModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    date_of_birth: str
    gender: str
