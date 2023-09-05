package com.github.ambersariya.hotel;

public class HotelNotFound extends RuntimeException {
    public HotelNotFound(String message) {
        super(message);
    }
}
