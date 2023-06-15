package com.github.ambersariya.booking;

import com.github.ambersariya.hotel.RoomType;

import java.util.List;

public record CompanyPolicy(int companyId, List<RoomType> roomTypes)
        implements BookingPolicy {
}
