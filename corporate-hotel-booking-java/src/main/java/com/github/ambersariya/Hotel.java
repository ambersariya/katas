package com.github.ambersariya;

import com.github.ambersariya.hotel.Room;

import java.util.ArrayList;

public class Hotel {
    public final int id;
    public final String name;
    private final ArrayList<Room> rooms;

    public Hotel(int id, String name) {
        this.id = id;
        this.name = name;
        rooms = new ArrayList<>();
    }

    public boolean equals(Object other) {
        if (other == null) return false;
        if (other == this) return true;
        if (!(other instanceof Hotel otherHotel)) return false;
        return this.id == otherHotel.id && this.name.equals(otherHotel.name);
    }

    public int hashCode() {
        return id;
    }

    public void setRoom(int roomNumber, RoomType roomType) {
        rooms.add(new Room(roomNumber, roomType));
    }

    public ArrayList<Room> rooms() {
        return rooms;
    }
}
