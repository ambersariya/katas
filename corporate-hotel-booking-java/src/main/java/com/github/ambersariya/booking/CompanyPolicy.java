package com.github.ambersariya.booking;

import com.github.ambersariya.core.CompanyId;
import com.github.ambersariya.hotel.RoomType;

import java.util.List;

public record CompanyPolicy(CompanyId companyId, List<RoomType> roomTypes)
        implements BookingPolicy {
}
