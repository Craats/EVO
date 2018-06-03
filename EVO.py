from pprint import pprint
from modules import entity
from modules import world


def main():
    print("=" * 30)
    print("= Peon test - Generate 1 peon, print vars")
    print("=" * 30)
    peon = entity.Entity()
    pprint(vars(peon))
    pprint(vars(peon.vitals))

    print("=" * 30)
    print("= World generation test - generate a small sample world, print vars")
    print("=" * 30)

    world_map = world.WorldMap(height = 5, width = 3, depth = 4)
    pprint(vars(world_map))

if __name__ == "__main__":
    main()
