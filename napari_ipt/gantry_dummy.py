from typing import List

class GantryDummy():
    def __init__(self, base_url:str=None):
        self._position = [0, 0, 0]

    @property
    def position(self):
        return self._position

    def home(self):
        print("home")

    def enable_drives(self):
        print("enable_drives")

    def disable_drives(self):
        print("disable_drives")

    def move_rel(self, distance: List[float], velocity:float=None, acceleration:float=None, jerk:float=None, deceleration:float=None):
        self._position[0] = self._position[0] + distance[0]
        self._position[1] = self._position[1] + distance[1]
        self._position[2] = self._position[2] + distance[2]
        print('Gantry: move_rel to:' + str(self._position))

    def move_abs(self, position: List[float], velocity:float=None, acceleration:float=None, jerk:float=None, deceleration:float=None):
        self._position = position
        print('Gantry: move_abs to:' + str(self._position))

    def move_abs_u(self, position: List[float], velocity:float=None, acceleration:float=None, jerk:float=None, deceleration:float=None):
        self._position = position
        print('Gantry: move_abs_u to:' + str(self._position))

    def move_to_safe(self, velocity:float=None, acceleration:float=None, jerk:float=None, deceleration:float=None):
        self.position[2] = self.z_safe,
        print('Gantry: move_to_safe to:' + str(self._position))  

    def test_napari(self, name:str=None):
        print(f'Layer selected: {name}')