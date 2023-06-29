package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.hotel.Hotel;
import com.github.ambersariya.hotel.InMemoryHotelRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class InMemoryHotelRepositoryShould {
    private static final int HOTEL_ID = 1;
    private static final String HOTEL_NAME = "Hotel Casablanca";
    private static final List<RoomType> SUPPORTED_ROOM_TYPES = List.of(RoomType.STANDARD, RoomType.MASTER_SUITE);

    @Test
    public void find_a_hotel_by_id() {
        InMemoryHotelRepository hotelRepository = new InMemoryHotelRepository();
        var hotelToSave = new Hotel(HOTEL_ID, HOTEL_NAME, SUPPORTED_ROOM_TYPES);
        hotelRepository.saveHotel(hotelToSave);
        var hotel = hotelRepository.findHotelBy(HOTEL_ID);
        assertEquals(HOTEL_NAME, hotel.name);
        assertEquals(HOTEL_ID, hotel.id);
    }
}
