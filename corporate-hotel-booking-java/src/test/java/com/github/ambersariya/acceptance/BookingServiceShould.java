package com.github.ambersariya.acceptance;

import com.github.ambersariya.booking.Booking;
import com.github.ambersariya.booking.BookingPolicyService;
import com.github.ambersariya.booking.BookingService;
import com.github.ambersariya.booking.InMemoryBookingPolicyRepository;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Date;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;

class BookingServiceShould {
    private static final int EMPLOYEE_ID = 1;
    private static final int HOTEL_ID = 1;
    private static final RoomType ROOM_TYPE = RoomType.STANDARD;
    private static final Date CHECK_IN = new Date(2020, 8, 5);
    private static final Date CHECK_OUT = new Date(2020, 8, 6);
    private static final String BOOKING_ID = "e20a504f-d3a1-48bd-a349-e1cad5158f33";
    private static final int COMPANY_ID = 1;
    private BookingPolicyService bookingPolicyService;

    @BeforeEach
    void setUp() {
        var employeeRepository = new InMemoryEmployeeRepository();
        var bookingPolicyRepository = new InMemoryBookingPolicyRepository();

        bookingPolicyService = new BookingPolicyService(bookingPolicyRepository, employeeRepository);
        bookingPolicyService.setEmployeePolicy(EMPLOYEE_ID, List.of(RoomType.JUNIOR_SUITE));
        bookingPolicyService.setCompanyPolicy(COMPANY_ID, List.of(RoomType.STANDARD));
    }

    @Test
    void make_a_booking() {
        var bookingService = new BookingService(bookingPolicyService);
        var booking = bookingService.book(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECK_IN, CHECK_OUT);

        assertInstanceOf(Booking.class, booking);
        assertEquals(BOOKING_ID, booking.id());
        assertEquals(EMPLOYEE_ID, booking.employeeId());
        assertEquals(HOTEL_ID, booking.hotelId());
        assertEquals(ROOM_TYPE, booking.roomType());
        assertEquals(CHECK_IN, booking.checkIn());
        assertEquals(CHECK_OUT, booking.checkOut());
    }
}