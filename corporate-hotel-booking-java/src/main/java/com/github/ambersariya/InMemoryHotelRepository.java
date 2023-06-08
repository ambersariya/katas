package com.github.ambersariya;

import java.util.HashMap;

public class InMemoryHotelRepository implements HotelRepository {
    private final HashMap<Integer, Hotel> hotels = new HashMap<>();

    @Override
    public void saveHotel(Hotel hotel) {
        hotels.put(hotel.id, hotel);
    }

    @Override
    public Hotel findHotelBy(int hotelId) {
        return hotels.get(hotelId);
    }
}
