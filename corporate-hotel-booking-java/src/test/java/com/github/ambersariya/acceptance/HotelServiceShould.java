package com.github.ambersariya.acceptance;

import com.github.ambersariya.hotel.*;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;

public class HotelServiceShould {
    private static final int HOTEL_ID = 1;
    private static final String HOTEL_NAME = "premier inn";
    private static final int ROOM_NUMBER = 1;
    private static final RoomType ROOM_TYPE = RoomType.STANDARD;

    @Test
    public void find_a_hotel_by_id() {
        HotelRepository hotelRepository = new InMemoryHotelRepository();
        HotelService hotelService = new HotelService(hotelRepository);
        hotelService.addHotel(HOTEL_ID, HOTEL_NAME);
        hotelService.setRoom(HOTEL_ID, ROOM_NUMBER, ROOM_TYPE);
        var hotel = hotelService.findHotelBy(HOTEL_ID);
        assertInstanceOf(Hotel.class, hotel);
        assertEquals(HOTEL_NAME, hotel.name);
        assertEquals(HOTEL_ID, hotel.id);
        assertInstanceOf(Room.class, hotel.findRoomByRoomNumber(ROOM_NUMBER));
    }
}
