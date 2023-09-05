package shopping_basket;

public interface ShoppingBasketRepository {
    ShoppingBasket findByUserId(UserID userId);

    void addItemToBasket(UserID userId, ProductID productID, int quantity);
}
