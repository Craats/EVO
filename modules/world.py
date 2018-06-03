import copy
import uuid

class WorldMap:
    """
    This class should contain the world, which is a X * Y rectangle
    Each space in the world should be a seperate class with properties

    First we initialize the whole world, to generate landmass groups
    Then we know which settings each block needs.
    """
    def __init__(self, height: int = 10, width: int = 10, depth: int = 1):
        self.map_h = height
        self.map_w = width
        self.map_d = depth

        # This a dictionary with an entry for each depth level.
        # In this depth level entry is a list of lists 
        # [y1:[x1, x2, x3], y2:[x1, x2, x3]]
        # Where coordinate (0, 0) is top left
        # Each individual node is a dictionary of properties.
        self.world_composition = {"empty": []}

        self.compose_world()
        self.landscape()
        self.gen_blocks()

    def compose_world(self):
        """
        Set the array dimensions correctly.
        """
        iter_d, iter_h, iter_w = 0, 0, 0
        single_layer_array = []
        while iter_h < self.map_h:
            single_line = []
            iter_w = 0
            while iter_w < self.map_w:
                # 0 is appended here as a placeholder. Do not create blocks here
                # Every depth-layer will be the same otherwise.
                single_line.append([0])
                iter_w = iter_w + 1
            single_layer_array.append(single_line)
            iter_h = iter_h + 1

        depth_layers = {}
        while iter_d < self.map_d:
            # Deepcopy here because otherwise every layer is the same
            # referenced list
            depth_layers[iter_d] = copy.deepcopy(single_layer_array)
            iter_d = iter_d + 1

        # Reminder, coordinates are (Y, X) starting at the top left
        self.world_composition = depth_layers

    def landscape(self):
        """
        Make structures in the world
        """
        pass

    def gen_blocks(self):
        """
        Creates individual world blocks from data in
        the world composition array
        """
        for depth_layer_key, depth_layer_value in self.world_composition.items():
            for width_line_key, width_line_value in enumerate(depth_layer_value):
                for height_unit_key, height_unit_value in enumerate(width_line_value):
                    self.world_composition\
                    [depth_layer_key]\
                    [width_line_key]\
                    [height_unit_key] = WorldBlock(type="grassland")

class WorldBlock:
    def __init__(self, type: str = "unset"):
        self.id = uuid.uuid4()
        self.type = type
        self.resources = {"unset": 0}

    def __repr__(self):
        return "{}".format(self.type)

    def set_type(self, newtype: str = "unset"):
        self.type = newtype

    def set_resource(self, res_type: str = "unset", res_amount: int = 0):
        self.resources[res_type] = res_amount
