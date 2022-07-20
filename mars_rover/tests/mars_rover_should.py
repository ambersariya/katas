import unittest

from mars_rover.mars_rover import MarsRover


class MarsRoverShould(unittest.TestCase):
    def setUp(self) -> None:
        self.rover = MarsRover()

    def test_be_facing_north(self):
        result = self.rover.execute(None)
        self.assertEqual('0:0:N', result)

    def test_face_east_when_turning_right(self):
        result = self.rover.execute('R')
        self.assertEqual('0:0:E', result)

    def test_face_south_when_turning_right(self):
        result = self.rover.execute('RR')
        self.assertEqual('0:0:S', result)

    def test_face_west_when_turning_right(self):
        result = self.rover.execute('RRR')
        self.assertEqual('0:0:W', result)

    def test_move_one_position_when_facing_north(self):
        result = self.rover.execute('M')
        self.assertEqual('0:1:N', result)

    def test_move_two_positions_when_facing_north(self):
        result = self.rover.execute('MM')
        self.assertEqual('0:2:N', result)

    def test_move_three_positions_when_facing_north(self):
        result = self.rover.execute('MMM')
        self.assertEqual('0:3:N', result)

    def test_move_nine_positions_when_facing_north(self):
        result = self.rover.execute('MMMMMMMMM')
        self.assertEqual('0:9:N', result)

    def test_move_one_position_when_facing_east(self):
        result = self.rover.execute('RM')
        self.assertEqual('1:0:E', result)

    def test_move_one_position_when_facing_south(self):
        result = self.rover.execute('MMRRM')
        self.assertEqual('0:1:S', result)

    def test_move_one_position_when_facing_west(self):
        result = self.rover.execute('RMMRRM')
        self.assertEqual('1:0:W', result)

    def test_face_west_when_turning_left_from_north(self):
        result = self.rover.execute('L')
        self.assertEqual('0:0:W', result)

    def test_face_south_when_turning_left_from_west(self):
        result = self.rover.execute('LL')
        self.assertEqual('0:0:S', result)

    def test_face_east_when_turning_left_from_south(self):
        result = self.rover.execute('LLL')
        self.assertEqual('0:0:E', result)

    def test_face_north_when_turning_left_from_east(self):
        result = self.rover.execute('LLLL')
        self.assertEqual('0:0:N', result)

    def test_face_west_when_turning_left_from_north_5_times(self):
        result = self.rover.execute('LLLLL')
        self.assertEqual('0:0:W', result)

    def test_face_west_when_turning_right_from_north_5_times(self):
        result = self.rover.execute('RRRRR')
        self.assertEqual('0:0:E', result)

    def test_be_at_start_position_after_moving_north_10_times(self):
        result = self.rover.execute('MMMMMMMMMM')
        self.assertEqual('0:0:N', result)

    def test_be_at_start_position_after_moving_east_10_times(self):
        result = self.rover.execute('RMMMMMMMMMM')
        self.assertEqual('0:0:E', result)

    def test_be_at_start_position_after_moving_south_10_times(self):
        result = self.rover.execute('RRMMMMMMMMMM')
        self.assertEqual('0:0:S', result)

    def test_be_at_start_position_after_moving_west_10_times(self):
        result = self.rover.execute('LMMMMMMMMMM')
        self.assertEqual('0:0:W', result)

    def test_be_at_2_3_N_with_MMRMMLM(self):
        result = self.rover.execute('MMRMMLM')
        self.assertEqual('2:3:N', result)