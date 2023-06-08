package com.github.ambersariya.hotel;

public class HotelDoesNotExist extends RuntimeException {
    public HotelDoesNotExist(String message) {
        super(message);
    }
}
