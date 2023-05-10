package shopping_basket.acceptance;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import shopping_basket.ProductID;
import shopping_basket.ShoppingBasket;
import shopping_basket.ShoppingBasketService;
import shopping_basket.UserID;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddItemsToShoppingBasketShould {
    private static final UserID USER_ID = new UserID("some-user-id-1");
    private static final ProductID PRODUCT_ID_HOBBIT = new ProductID(10002);
    private static final ProductID PRODUCT_ID_BREAKING_BAD = new ProductID(10001);
    private static final int QUANTITY_PRODUCT_HOBBIT = 2;
    private static final int QUANTITY_PRODUCT_BREAKING_BAD = 5;
    private ShoppingBasketService shoppingBasketService;

    @BeforeEach
    public void setUp() {
        shoppingBasketService = new ShoppingBasketService();
    }

    @Test
    public void printout_basket_items() {
        shoppingBasketService.addItem(USER_ID, PRODUCT_ID_HOBBIT, QUANTITY_PRODUCT_HOBBIT);
        shoppingBasketService.addItem(USER_ID, PRODUCT_ID_BREAKING_BAD, QUANTITY_PRODUCT_BREAKING_BAD);

        ShoppingBasket basket = shoppingBasketService.basketFor(USER_ID);

        String printout = """
                09 May 2023
                2 x The Hobbit // 2 x 5.00 = £10.00
                5 x Breaking Bad // 5 x 7.00 = £35.00
                Total: £45.00""";

        assertEquals(basket.print(), printout);
    }
}
