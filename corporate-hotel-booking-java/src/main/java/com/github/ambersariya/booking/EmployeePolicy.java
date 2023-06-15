package com.github.ambersariya.booking;

import com.github.ambersariya.hotel.RoomType;

import java.util.List;

public record EmployeePolicy(int employeeId, List<RoomType> roomTypes)
        implements BookingPolicy {
}
