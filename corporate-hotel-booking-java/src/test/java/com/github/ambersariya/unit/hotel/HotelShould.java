package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.Hotel;
import com.github.ambersariya.RoomType;
import com.github.ambersariya.hotel.Room;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HotelShould {
    @Test
    public void be_able_to_return_empty_list_when_there_are_no_rooms() {
        var hotel = new Hotel(1, "premier inn");
        var rooms = new ArrayList<>();
        assertEquals(rooms, hotel.rooms());
    }

    @Test
    public void be_able_to_return_all_of_its_rooms() {
        var hotel = new Hotel(1, "premier inn");
        var rooms = new ArrayList<>();
        rooms.add(new Room(1, RoomType.STANDARD));
        hotel.setRoom(1, RoomType.STANDARD);

        assertEquals(rooms, hotel.rooms());
    }
}
