from __future__ import print_function

import shapely
import fiona   # do we need this???

from shapely.geometry import Point, asShape




filename = '../cb_2015_us_cd114_500k.shp'
# with fiona.open(filename) as src:
#     pprint.pprint(src[1])


c = fiona.open(filename)

# shapely.geometry.asShape(c[1]['geometry']).contains(Point(-77.16, 39))

# c[1].properies()


# rockhill_sc = Point(34.9249, 81.0251)
# aiken_sc = Point(-81.7196, 33.5604)
#
# shapely.geometry.asShape(c[40]['geometry']).contains(rockhill_sc)
#
# shapely.geometry.asShape(c[40]['geometry']).contains(aiken_sc)
#
#
# shapely.geometry.asShape(c[40]['geometry']).contains(Point(-81.7196, 34.5604))

def found_district(lon, lat, shp, idx):
    res = asShape(shp[idx]['geometry']).contains(Point(lon, lat))
    return res


def get_district(lon, lat, shp):
    n = len(shp)
    state_fips = None
    cd114_fips = None

    for i in range(n):
        if found_district(lon, lat, shp, i):
            state_fips = shp[i]['properties']['STATEFP']
            cd114_fips = shp[i]['properties']['CD114FP']
            break
    return (state_fips, cd114_fips)

print(get_district(-81.7196, 33.5604, c))
print(get_district(-97.0383, 32.5486, c))

