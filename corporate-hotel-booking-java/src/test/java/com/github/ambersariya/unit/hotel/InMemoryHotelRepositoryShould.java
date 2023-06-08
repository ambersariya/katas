package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.Hotel;
import com.github.ambersariya.InMemoryHotelRepository;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class InMemoryHotelRepositoryShould {
    private static final int HOTEL_ID = 1;
    private static final String HOTEL_NAME = "Hotel Casablanca";

    @Test
    public void find_a_hotel_by_id() {
        InMemoryHotelRepository hotelRepository = new InMemoryHotelRepository();
        var hotelToSave = new Hotel(HOTEL_ID, HOTEL_NAME);
        hotelRepository.saveHotel(hotelToSave);
        var hotel = hotelRepository.findHotelBy(HOTEL_ID);
        assertEquals(HOTEL_NAME, hotel.name);
        assertEquals(HOTEL_ID, hotel.id);
    }
}
