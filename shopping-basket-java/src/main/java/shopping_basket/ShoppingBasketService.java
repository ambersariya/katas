package shopping_basket;

public class ShoppingBasketService {
    private final ShoppingBasketRepository shoppingBasketRepository;

    public ShoppingBasketService(ShoppingBasketRepository shoppingBasketRepository) {
        this.shoppingBasketRepository = shoppingBasketRepository;
    }

    public void addItem(UserID userId, ProductID productID, int quantity) {
        shoppingBasketRepository.addItemToBasket(userId, productID, quantity);
    }

    public ShoppingBasket basketFor(UserID userId) {
        return shoppingBasketRepository.findByUserId(userId);
    }
}
