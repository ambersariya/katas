package com.github.ambersariya;

public class HotelService {

    private final HotelRepository hotelRepository;

    public HotelService(HotelRepository hotelRepository) {
        this.hotelRepository = hotelRepository;
    }

    public void addHotel(int hotelId, String hotelName) {
        var hotel = new Hotel(hotelId, hotelName);
        hotelRepository.saveHotel(hotel);
    }

    public void setRoom(int hotelId, int roomNumber, RoomType roomType) {
        var hotel = hotelRepository.findHotelBy(hotelId);
        hotel.setRoom(roomNumber, roomType);
        hotelRepository.saveHotel(hotel);
    }

    public Hotel findHotelBy(int hotelId) {
        return hotelRepository.findHotelBy(hotelId);
    }
}
