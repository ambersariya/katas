from pydantic import BaseModel


class AddItem(BaseModel):
    product_id: str
    quantity: int
