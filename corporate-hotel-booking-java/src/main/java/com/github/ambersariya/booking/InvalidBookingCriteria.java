package com.github.ambersariya.booking;

public class InvalidBookingCriteria extends RuntimeException {
    public InvalidBookingCriteria(String message) {
        super(message);
    }
}
