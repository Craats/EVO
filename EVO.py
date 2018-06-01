from pprint import pprint
from modules import entity
# from modules import world


def main():
    mister = entity.Entity()
    pprint(vars(mister))
    pprint(mister.vitals.vitals)

if __name__ == "__main__":
    main()
