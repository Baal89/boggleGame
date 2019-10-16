import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    our test suit for Boggle solver
    """
    
    def test_can_create_an_empty_grif(self):
        """
        test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_is_width_times_height(self):
        """
        test is to ensure that total size of the grid is
        equal to width * height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)