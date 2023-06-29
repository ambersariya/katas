package com.github.ambersariya.booking;

import java.util.HashMap;
import java.util.Map;

public class InMemoryBookingRepository implements BookingRepository {
    private final Map<String, Booking> bookings = new HashMap<>();

	@Override
    public void saveBooking(Booking booking) {
        bookings.put(booking.id(), booking);
    }
    
    @Override
	public Booking findByBookingId(String bookingId) {
        return bookings.get(bookingId);
	}
}
