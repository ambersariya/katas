package com.github.ambersariya;

import com.github.ambersariya.hotel.HotelAlreadyExists;
import com.github.ambersariya.hotel.HotelDoesNotExist;

public class HotelService {

    private final HotelRepository hotelRepository;

    public HotelService(HotelRepository hotelRepository) {
        this.hotelRepository = hotelRepository;
    }

    public void addHotel(int hotelId, String hotelName) {
        if (hotelRepository.findHotelBy(hotelId) != null) {
            throw new HotelAlreadyExists("Hotel already exists");
        }

        var hotel = new Hotel(hotelId, hotelName);
        hotelRepository.saveHotel(hotel);
    }

    public void setRoom(int hotelId, int roomNumber, RoomType roomType) {
        var hotel = hotelRepository.findHotelBy(hotelId);
        if (hotel == null) {
            throw new HotelDoesNotExist("Hotel does not exist");
        }
        hotel.setRoom(roomNumber, roomType);
        hotelRepository.saveHotel(hotel);
    }

    public Hotel findHotelBy(int hotelId) {
        return hotelRepository.findHotelBy(hotelId);
    }
}
