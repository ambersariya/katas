package com.github.ambersariya.booking;

import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.core.IdGenerator;
import com.github.ambersariya.hotel.HotelNotFound;
import com.github.ambersariya.hotel.HotelService;
import com.github.ambersariya.hotel.RoomType;

import java.util.Date;

public class BookingService {
    private final BookingPolicyService bookingPolicyService;
    private final IdGenerator idGenerator;
    private final BookingRepository bookingRepository;
    private HotelService hotelService;

    public BookingService(BookingPolicyService bookingPolicyService, IdGenerator idGenerator, BookingRepository bookingRepository, HotelService hotelService) {
        this.bookingPolicyService = bookingPolicyService;
        this.idGenerator = idGenerator;
        this.bookingRepository = bookingRepository;
        this.hotelService = hotelService;
    }

    public Booking book(EmployeeId employeeId, int hotelId, RoomType roomType, Date checkIn, Date checkOut) {
        validateBookingDates(checkIn, checkOut);
        validateHotelExists(hotelId);
        validateRoomTypeIsSupported(hotelId, roomType);

        var isBookingAllowed = this.bookingPolicyService.isBookingAllowed(employeeId, roomType);
        if (!isBookingAllowed) {
            throw new BookingNotAllowedException();
        }
        var booking = new Booking(idGenerator.nextId(), hotelId, employeeId, roomType, checkIn, checkOut);
        this.bookingRepository.saveBooking(booking);

        return booking;
    }

    private void validateRoomTypeIsSupported(int hotelId, RoomType roomType) {
        var hotel = hotelService.findHotelBy(hotelId);
        if (!hotel.supportsRoomType(roomType)) {
            throw new RoomTypeNotSupported("Room type is not supported");
        }
    }

    private void validateHotelExists(int hotelId) {
        if (hotelService.findHotelBy(hotelId) == null) {
            throw new HotelNotFound("Hotel does not exist");
        }
    }

    private void validateBookingDates(Date checkIn, Date checkOut) {
        if (checkIn.after(checkOut) || checkIn.equals(checkOut)) {
            throw new InvalidBookingCriteria("Check-in date cannot be after Check-out date");
        }
    }
}
