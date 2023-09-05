package shopping_basket.unit;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import shopping_basket.ProductID;
import shopping_basket.ShoppingBasketRepository;
import shopping_basket.ShoppingBasketService;
import shopping_basket.UserID;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class ShoppingBasketShould {

    @Mock
    private ShoppingBasketRepository shoppingBasketRepository;
    private ShoppingBasketService shoppingBasketService;

    private static final UserID USER_ID = new UserID("some-user-id-1");
    private static final ProductID PRODUCT_ID_HOBBIT = new ProductID(10002);
    private static final ProductID PRODUCT_ID_BREAKING_BAD = new ProductID(10001);
    private static final int QUANTITY_PRODUCT_HOBBIT = 2;
    private static final int QUANTITY_PRODUCT_BREAKING_BAD = 5;

    @BeforeEach
    public void setUp() {
        shoppingBasketService = new ShoppingBasketService(shoppingBasketRepository);
    }

    @Test
    public void be_created_when_the_first_product_is_added() {
        when(shoppingBasketRepository.findByUserId(USER_ID)).thenReturn(null);

        assertEquals(shoppingBasketService.basketFor(USER_ID), null);

        shoppingBasketService.addItem(USER_ID, PRODUCT_ID_HOBBIT, QUANTITY_PRODUCT_HOBBIT);

        verify(shoppingBasketRepository, times(1)).findByUserId(USER_ID);
    }
}
