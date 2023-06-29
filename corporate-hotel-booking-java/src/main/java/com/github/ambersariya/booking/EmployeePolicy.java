package com.github.ambersariya.booking;

import com.github.ambersariya.core.EmployeeId;
import com.github.ambersariya.hotel.RoomType;

import java.util.List;

public record EmployeePolicy(EmployeeId employeeId, List<RoomType> roomTypes)
        implements BookingPolicy {
}
