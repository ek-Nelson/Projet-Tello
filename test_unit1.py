# test_drone_controller.py
import unittest
from unittest.mock import MagicMock
from djitellopy import Tello
import time

me = Tello()

class TestDroneController(unittest.TestCase):
    def test_wake_up(self):
        # Création d'un faux objet Tello pour le test
        fake_tello = MagicMock()

        # Appel de la fonction à tester
        me.wake_up(fake_tello)

        # Vérification des appels de méthodes sur l'objet Tello simulé
        fake_tello.takeoff.assert_called_once()
        fake_tello.rotate_clockwise.assert_called_once_with(90)
        fake_tello.move_left.assert_called_once_with(35)
        fake_tello.land.assert_called_once()


    def wake_up(fake_tello):
        fake_tello.takeoff()
        time.sleep(5)
        fake_tello.rotate_clockwise(90)
        time.sleep(3)
        fake_tello.move_left(35)
        time.sleep(3)
        fake_tello.land()

if __name__ == '__main__':
    unittest.main()
