package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.hotel.Hotel;
import com.github.ambersariya.hotel.Room;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HotelShould {
    private static final Hotel hotel = new Hotel(1, "premier inn");
    private static final List<Room> rooms = new ArrayList<Room>();

    @Test
    public void be_able_to_return_empty_list_when_there_are_no_rooms() {
        assertEquals(rooms, hotel.rooms());
    }

    @Test
    public void be_able_to_return_all_of_its_rooms() {
        rooms.add(new Room(1, RoomType.STANDARD));
        hotel.setRoom(1, RoomType.STANDARD);

        assertEquals(rooms, hotel.rooms());
    }

    @Test
    public void find_room_by_room_number() {
        var ROOM = new Room(1, RoomType.STANDARD);
        hotel.setRoom(1, RoomType.STANDARD);
        var room = hotel.findRoomByRoomNumber(1);

        assertEquals(ROOM, room);
    }

    @Test
    public void return_number_of_rooms_in_a_hotel() {
        hotel.setRoom(1, RoomType.STANDARD);
        hotel.setRoom(2, RoomType.STANDARD);
        hotel.setRoom(3, RoomType.STANDARD);

        assertEquals(3, hotel.numberOfRooms());
    }
}
