package com.github.ambersariya.booking;

public class RoomTypeNotSupported extends RuntimeException {
    public RoomTypeNotSupported(String message) {
        super(message);
    }
}
