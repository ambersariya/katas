package com.github.ambersariya.booking;

import com.github.ambersariya.hotel.RoomType;

import java.util.Date;

public class BookingService {
    private final BookingPolicyService bookingPolicyService;

    public BookingService(BookingPolicyService bookingPolicyService) {
        this.bookingPolicyService = bookingPolicyService;
    }

    public Booking book(int employeeId, int hotelId, RoomType roomType, Date checkIn, Date checkOut) {
        throw new UnsupportedOperationException();
    }
}
