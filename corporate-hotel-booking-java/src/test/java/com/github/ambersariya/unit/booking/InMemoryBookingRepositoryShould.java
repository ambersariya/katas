package com.github.ambersariya.unit.booking;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.util.Date;

import org.junit.jupiter.api.Test;

import com.github.ambersariya.booking.Booking;
import com.github.ambersariya.booking.InMemoryBookingRepository;
import com.github.ambersariya.hotel.RoomType;

public class InMemoryBookingRepositoryShould {
    private static final int HOTEL_ID = 1;
    private static final int EMPLOYEE_ID = 1;
    private static final String BOOKING_ID = "afe14de1-71e5-4040-8f5e-aea23c6d5c57";
    private static final RoomType ROOM_TYPE = RoomType.STANDARD;

    @Test
    public void save_a_booking() {
        var repository = new InMemoryBookingRepository();
        var booking = new Booking(BOOKING_ID, HOTEL_ID, EMPLOYEE_ID, ROOM_TYPE, new Date(), new Date());

        repository.saveBooking(booking);
        
        Booking savedBooking = repository.findByBookingId(BOOKING_ID);
        
        assertNotNull(savedBooking);
        assertEquals(booking, savedBooking);
    }
}
