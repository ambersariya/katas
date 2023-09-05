package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.hotel.Hotel;
import com.github.ambersariya.hotel.Room;
import com.github.ambersariya.hotel.RoomType;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HotelShould {
    private static final List<RoomType> SUPPORTED_ROOM_TYPES = List.of(RoomType.STANDARD, RoomType.MASTER_SUITE);
    private static final Hotel hotel = new Hotel(1, "premier inn", SUPPORTED_ROOM_TYPES);
    private static final List<Room> rooms = new ArrayList<Room>();
    private static final Room STANDARD_ROOM = new Room(1, RoomType.STANDARD);

    @Test
    public void be_able_to_return_empty_list_when_there_are_no_rooms() {
        assertEquals(rooms, hotel.rooms());
    }

    @Test
    public void be_able_to_return_all_of_its_rooms() {
        rooms.add(STANDARD_ROOM);
        hotel.setRoom(1, RoomType.STANDARD);

        assertEquals(rooms, hotel.rooms());
    }

    @Test
    public void find_room_by_room_number() {
        hotel.setRoom(1, RoomType.STANDARD);
        var room = hotel.findRoomByRoomNumber(1);

        assertEquals(STANDARD_ROOM, room);
    }

    @Test
    public void return_number_of_rooms_in_a_hotel() {
        hotel.setRoom(1, RoomType.STANDARD);
        hotel.setRoom(2, RoomType.STANDARD);
        hotel.setRoom(3, RoomType.STANDARD);

        assertEquals(3, hotel.numberOfRooms());
    }
}
