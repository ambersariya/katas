package com.github.ambersariya.booking;

import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.hotel.RoomType;

import java.util.Date;

public record Booking(
        String id,
        int hotelId,
        EmployeeId employeeId,
        RoomType roomType,
        Date checkIn,
        Date checkOut) {
}
