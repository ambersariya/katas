package com.github.ambersariya.hotel;

public interface HotelRepository {
    void saveHotel(Hotel hotel);

    Hotel findHotelBy(int hotelId);
}
