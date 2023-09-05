package shopping_basket;

public class InMemoryShoppingBasketRepository implements ShoppingBasketRepository{
    @Override
    public ShoppingBasket findByUserId(UserID userId) {
        return null;
    }

    @Override
    public void addItemToBasket(UserID userId, ProductID productID, int quantity) {

    }
}
