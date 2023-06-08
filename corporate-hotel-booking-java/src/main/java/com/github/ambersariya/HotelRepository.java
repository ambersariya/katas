package com.github.ambersariya;

public interface HotelRepository {
    void saveHotel(Hotel hotel);

    Hotel findHotelBy(int hotelId);
}
