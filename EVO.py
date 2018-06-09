from pprint import pprint
from time import sleep
from modules import entity
from modules import world
from modules import render


def main():
    print("=" * 80)
    print("= Peon test - Generate 1 peon, print vars")
    print("=" * 80)
    peon = entity.Entity()
    pprint(vars(peon))
    pprint(vars(peon.vitals))

    print("=" * 80)
    print("= World generation test - generate a small sample world, print vars")
    print("=" * 80)

    world_map = world.WorldMap(height = 5, width = 3, depth = 4)
    pprint(vars(world_map))
    
    print("=" * 80)
    print("= Render test, single frame")
    print("=" * 80)
    screen = render.Render()
    screen.update_world(world_map.world_composition)
    screen.refresh()
    sleep(2)
    screen.stop()

if __name__ == "__main__":
    main()
