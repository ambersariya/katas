package com.github.ambersariya;

import com.github.ambersariya.hotel.Room;

import java.util.HashMap;
import java.util.List;

public class Hotel {
    public final int id;
    public final String name;
    private final HashMap<Integer, Room> rooms;

    public Hotel(int id, String name) {
        this.id = id;
        this.name = name;
        rooms = new HashMap<>();
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
        rooms.put(roomNumber, new Room(roomNumber, roomType));
    }

    public List<Room> rooms() {
        return rooms.values().stream().toList();
    }

    public Room findRoomByRoomNumber(int roomNumber) {
        return rooms.get(roomNumber);
    }

    public int numberOfRooms() {
        return rooms.size();
    }
}
