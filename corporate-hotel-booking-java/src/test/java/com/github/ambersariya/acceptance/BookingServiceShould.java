package com.github.ambersariya.acceptance;

import com.github.ambersariya.booking.*;
import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.core.IdGenerator;
import com.github.ambersariya.core.UuidGenerator;
import com.github.ambersariya.employee.InMemoryEmployeeRepository;
import com.github.ambersariya.hotel.HotelService;
import com.github.ambersariya.hotel.InMemoryHotelRepository;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Date;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class BookingServiceShould {
    private static final EmployeeId EMPLOYEE_ID = new EmployeeId("d4bd3200-3d27-4e92-936d-e8f1c47f5f21");
    private static final int HOTEL_ID = 1;
    private static final RoomType ROOM_TYPE = RoomType.STANDARD;
    private static final Date CHECK_IN = new Date(2020, 8, 5);
    private static final Date CHECK_OUT = new Date(2020, 8, 6);
    private static final CompanyId COMPANY_ID = new CompanyId("d4bd3200-3d27-4e92-936d-e8f1c47f5f21");
    private BookingPolicyService bookingPolicyService;
    private IdGenerator idGenerator;
    private InMemoryBookingRepository bookingRepository;
    private HotelService hotelService;

    @BeforeEach
    void setUp() {
        var employeeRepository = new InMemoryEmployeeRepository();
        var bookingPolicyRepository = new InMemoryBookingPolicyRepository();
        bookingRepository = new InMemoryBookingRepository();
        idGenerator = new UuidGenerator();
        var hotelRepository = new InMemoryHotelRepository();
        hotelService = new HotelService(hotelRepository);


        bookingPolicyService = new BookingPolicyService(bookingPolicyRepository, employeeRepository);
        bookingPolicyService.setEmployeePolicy(EMPLOYEE_ID, List.of(RoomType.STANDARD));
        bookingPolicyService.setCompanyPolicy(COMPANY_ID, List.of(RoomType.STANDARD));
    }

    @Test
    void make_a_booking() {
        var bookingService = new BookingService(bookingPolicyService, idGenerator, bookingRepository, hotelService);
        hotelService.addHotel(HOTEL_ID, "Hotel Casablanca");
        hotelService.setRoom(HOTEL_ID, 10, ROOM_TYPE);

        var booking = bookingService.book(EMPLOYEE_ID, HOTEL_ID, ROOM_TYPE, CHECK_IN, CHECK_OUT);

        assertInstanceOf(Booking.class, booking);
        assertNotNull(booking.id());
        assertEquals(EMPLOYEE_ID, booking.employeeId());
        assertEquals(HOTEL_ID, booking.hotelId());
        assertEquals(ROOM_TYPE, booking.roomType());
        assertEquals(CHECK_IN, booking.checkIn());
        assertEquals(CHECK_OUT, booking.checkOut());
    }
}