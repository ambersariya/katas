package com.github.ambersariya.hotel;

public class HotelAlreadyExists extends RuntimeException {
    public HotelAlreadyExists(String message) {
        super(message);
    }
}
