from acceptance_tests.base_test_case import BaseTestCase
from constants import USER_ID, STRATEGIES
from shopping_basket.basket.shopping_basket_service import ShoppingBasketService
from shopping_basket.discount.discount_calculator import DiscountCalculator
from shopping_basket.product.product_id import ProductId


class ApplyDiscountShould(BaseTestCase):

    def setUp(self) -> None:
        BaseTestCase.setUp(self)
        self.discount_calculator = DiscountCalculator(STRATEGIES)
        self.shopping_basket_service = ShoppingBasketService(
            product_service=self.product_service,
            shopping_basket_repository=self.shopping_basket_repository,
            item_logger=self.item_logger,
            discount_calculator=self.discount_calculator,
        )

    def test_return_contents_of_the_basket(self):
        self._add_item(ProductId("10002"), 4)
        self._add_item(ProductId("20110"), 5)

        basket = self.shopping_basket_service.basket_for(USER_ID)

        basket_printout = (
            "Creation date 15/06/2022\n"
            "4 x The Hobbit // Book // 4 x 5.00 = £20.00\n"
            "5 x Breaking Bad // Video // 5 x 7.00 = £35.00\n"
            "Discount applied: 20%\n"
            "Total: £44.00"
        )

        assert str(basket) == basket_printout

