package com.github.ambersariya.unit.booking;

import com.github.ambersariya.booking.*;
import com.github.ambersariya.core.IdGenerator;
import com.github.ambersariya.hotel.Hotel;
import com.github.ambersariya.hotel.HotelNotFound;
import com.github.ambersariya.hotel.HotelService;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Date;
import java.util.List;

import static org.mockito.Mockito.*;

/**
 * Rules
 * <p>
 * Booking should contain a unique ID, employeeId, hotelId, roomType, checkIn and checkOut.
 * Check out date must be at least one day after the check in date.
 * Validate if the hotel exists and room type is provided by the hotel
 * Verify if booking is allowed according to the booking policies defined, if any. See Booking Policy Service for more details.
 * Booking should only be allowed if there is at least one room type available during the whole booking period.
 * Keep track of all bookings. E.g. If hotel has 5 standard rooms, we should have no more than 5 bookings in the same day.
 * Hotel rooms can be booked many times as long as there are no conflicts with the dates.
 * Return booking confirmation to the employee or error otherwise (exceptions can also be used).
 */
@ExtendWith(MockitoExtension.class)
public class BookingServiceShould {
    private static final int HOTEL_ID = 1;
    private static final int EMPLOYEE_ID = 1;
    private static final Date CHECK_IN = new Date(2023, 5, 1);
    private static final Date CHECK_OUT = new Date(2023, 5, 10);
    private static final Date INVALID_CHECK_OUT = new Date(2023, 4, 30);
    private static final String BOOKING_ID = "0d1bfbf4-e7d1-4fa3-b70e-2226b569e033";
    private static final Booking BOOKING_STANDARD_ROOM = new Booking(BOOKING_ID, EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, CHECK_OUT);
    private static final List<RoomType> SUPPORTED_ROOM_TYPES = List.of(RoomType.STANDARD);
    private static final Hotel HOTEL = new Hotel(HOTEL_ID, "Hotel California", SUPPORTED_ROOM_TYPES);
    @Mock
    private BookingPolicyService bookingPolicyService;
    @Mock
    private IdGenerator idGenerator;
    @Mock
    private BookingRepository bookingRepository;
    @Mock
    private HotelService hotelService;
    private BookingService bookingService;

    @BeforeEach
    void setUp() {
        bookingService = new BookingService(bookingPolicyService, idGenerator, bookingRepository, hotelService);
    }

    @Test
    void book_a_room() {
        when(hotelService.findHotelBy(HOTEL_ID)).thenReturn(HOTEL);
        when(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD)).thenReturn(true);
        when(idGenerator.nextId()).thenReturn(BOOKING_ID);
        var booking = bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, CHECK_OUT);

        verify(bookingPolicyService).isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD);
        verify(bookingRepository).saveBooking(BOOKING_STANDARD_ROOM);

        Assertions.assertInstanceOf(Booking.class, booking);
    }

    @Test
    void throw_exception_when_booking_is_not_allowed() {
        when(hotelService.findHotelBy(HOTEL_ID)).thenReturn(HOTEL);
        when(bookingPolicyService.isBookingAllowed(EMPLOYEE_ID, RoomType.STANDARD)).thenReturn(false);
        Assertions.assertThrows(BookingNotAllowedException.class, () -> {
            bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, CHECK_OUT);
        });
        verifyNoInteractions(bookingRepository);
        verifyNoInteractions(idGenerator);
    }

    @Test
    void throw_exception_when_checkout_date_is_before_checkin_date() {
        Assertions.assertThrows(InvalidBookingCriteria.class, () -> {
            bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, INVALID_CHECK_OUT);
        });
    }

    @Test
    void throw_exception_when_checkout_date_is_equal_to_checkin_date() {
        Assertions.assertThrows(InvalidBookingCriteria.class, () -> {
            bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, CHECK_IN);
        });
    }

    @Test
    void throw_exception_when_if_the_hotel_doesnt_exists() {
        when(hotelService.findHotelBy(HOTEL_ID)).thenReturn(null);
        Assertions.assertThrows(HotelNotFound.class, () -> {
            bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.STANDARD, CHECK_IN, CHECK_OUT);
        });

        verifyNoInteractions(bookingRepository);
        verifyNoInteractions(bookingPolicyService);
    }

    @Test
    void throw_exception_when_if_the_hotel_doesnt_support_room_type() {
        when(hotelService.findHotelBy(HOTEL_ID)).thenReturn(HOTEL);
        Assertions.assertThrows(RoomTypeNotSupported.class, () -> {
            bookingService.book(EMPLOYEE_ID, HOTEL_ID, RoomType.JUNIOR_SUITE, CHECK_IN, CHECK_OUT);
        });

        verifyNoInteractions(bookingRepository);
        verifyNoInteractions(bookingPolicyService);
    }
}
