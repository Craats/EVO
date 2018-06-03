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
                single_line.append([0])
                iter_w = iter_w + 1
            single_layer_array.append(single_line)
            iter_h = iter_h + 1

        depth_layers = {}
        while iter_d < self.map_d:
            depth_layers[iter_d] = single_layer_array
            iter_d = iter_d + 1

        # Reminder, coordinates are (Y, X) starting at the top left
        self.world_composition = depth_layers
        self.world_composition[0][1][0] = 1

    def gen_blocks(self):
        """
        Creates individual world blocks from data in
        the world composition array
        """
        pass

class WorldBlock:
    def __init__(self):
        pass
