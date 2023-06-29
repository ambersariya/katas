package com.github.ambersariya.booking;

public interface BookingRepository {
    void saveBooking(Booking booking);
    Booking findByBookingId(String bookingId);
}
