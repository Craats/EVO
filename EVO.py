from pprint import pprint
from modules import entity
# from modules import world


def main():
    peon = entity.Entity()
    pprint(vars(peon))
    pprint(peon.vitals.vitals)

if __name__ == "__main__":
    main()
