from makeup import Makeup
from concealer import Concealer

if __name__ == '__main__':
    # print('new dawn, new day')
    two_faced = Concealer('Too Faced', 'chestnut', 32)
    print(two_faced.apply('eye'))

    assert isinstance(two_faced, Makeup)

    print(two_faced.remove())

    print(two_faced.remove())

