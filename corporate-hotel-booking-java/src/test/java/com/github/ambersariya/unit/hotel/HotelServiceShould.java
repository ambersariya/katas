package com.github.ambersariya.unit.hotel;

import com.github.ambersariya.Hotel;
import com.github.ambersariya.HotelRepository;
import com.github.ambersariya.HotelService;
import com.github.ambersariya.RoomType;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class HotelServiceShould {
    private static final String HOTEL_NAME = "premier inn";
    private static final int HOTEL_ID = 2;
    private static final Hotel HOTEL = new Hotel(HOTEL_ID, HOTEL_NAME);
    @InjectMocks
    private HotelService hotelService;
    @Mock
    private HotelRepository hotelRepository;
//    private final Hotel hotel = new Hotel(HOTEL_ID, HOTEL_NAME);

    @BeforeEach
    public void setUp() {
        hotelService = new HotelService(hotelRepository);
    }

    @Test
    public void be_able_to_add_hotel() {
        hotelService.addHotel(HOTEL_ID, HOTEL_NAME);

        verify(hotelRepository).saveHotel(HOTEL);
    }

    @Test
    public void return_a_hotel_by_id() {
        when(hotelRepository.findHotelBy(HOTEL_ID)).thenReturn(HOTEL);
        var hotel = hotelService.findHotelBy(HOTEL_ID);
        assertEquals(HOTEL, hotel);
    }

    @Test
    public void be_able_to_set_room() {
        when(hotelRepository.findHotelBy(HOTEL_ID)).thenReturn(HOTEL);

        hotelService.setRoom(HOTEL_ID, 1, RoomType.STANDARD);

        verify(hotelRepository).saveHotel(HOTEL);
    }
}
