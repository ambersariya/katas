from shopping_basket.basket.shopping_basket import ShoppingBasket
from shopping_basket.basket.shopping_basket_error import ShoppingBasketNotFoundError
from shopping_basket.basket.shopping_basket_item import ShoppingBasketItem
from shopping_basket.basket.shopping_basket_repository import ShoppingBasketRepository
from shopping_basket.basket.user import UserId
from shopping_basket.core.utilities import ItemLogger
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.product.product_id import ProductId
from shopping_basket.product.product_service import ProductService


class ShoppingBasketService:
    def __init__(
        self,
        shopping_basket_repository: ShoppingBasketRepository,
        product_service: ProductService,
        item_logger: ItemLogger,
        discount_calculator: DiscountCalculator
    ):
        self._discount_calculator = discount_calculator
        self._item_logger = item_logger
        self._product_service = product_service
        self._shopping_basket_repository = shopping_basket_repository

    def basket_for(self, user_id: UserId) -> ShoppingBasket:
        basket = self._shopping_basket_repository.basket_for(user_id)
        if basket is None:
            raise ShoppingBasketNotFoundError()

        return self._discount_calculator.apply_discount(basket=basket)

    def add_item(self, user_id: UserId, product_id: ProductId, quantity: int) -> None:
        product = self._product_service.reserve(product_id=product_id, quantity=quantity)
        if product:
            item = ShoppingBasketItem.for_product(product, quantity=quantity)
            self._shopping_basket_repository.add_item(item=item, user_id=user_id)
            self._item_logger.log(user_id=user_id, item=item)
