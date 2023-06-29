package com.github.ambersariya.hotel;

import java.util.List;

public class HotelService {

    private static final List<RoomType> SUPPORTED_ROOM_TYPES = List.of(RoomType.STANDARD, RoomType.MASTER_SUITE);
    private final HotelRepository hotelRepository;

    public HotelService(HotelRepository hotelRepository) {
        this.hotelRepository = hotelRepository;
    }

    public void addHotel(int hotelId, String hotelName) {
        if (hotelRepository.findHotelBy(hotelId) != null) {
            throw new HotelAlreadyExists("Hotel already exists");
        }

        var hotel = new Hotel(hotelId, hotelName, SUPPORTED_ROOM_TYPES);
        hotelRepository.saveHotel(hotel);
    }

    public void setRoom(int hotelId, int roomNumber, RoomType roomType) {
        var hotel = hotelRepository.findHotelBy(hotelId);
        if (hotel == null) {
            throw new HotelNotFound("Hotel does not exist");
        }
        hotel.setRoom(roomNumber, roomType);
        hotelRepository.saveHotel(hotel);
    }

    public Hotel findHotelBy(int hotelId) {
        return hotelRepository.findHotelBy(hotelId);
    }
}
