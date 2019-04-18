import json, os, sys
import argparse
import numpy as np
import imageio

sequences = ['Basketball', 'Gaslamp', 'Harbor', 'JamSession', 'KiteFlite', 'Stitched_left_Dancing360_8K', 'Stitched_left_Driving360_8K']
schemes = ['S1', 'S2', 'S3', 'S4']

def readingTileInfos(filenameTileJSON):
    
    if (os.path.exists(filenameTileJSON)):
        with open(filenameTileJSON) as f:
            dummyarray4tile = json.load(f)
    else:
        print(filenameTileJSON)
        print('Sorry! there is no json file in the directory!')
        sys.exit()

    return dummyarray4tile

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("t_sch", help="Tiling scheme ")
    parser.add_argument("t_set", help="Tiling set {S_1, S_2, S_3, S_4}")

    args = parser.parse_args()

    # border for the tiles
    pix = 50

    # tiling schemes folder
    json_name = '../tilingSchemes/' + schemes[int(args.t_set) + 1] + '/scheme_' + str(args.t_sch) + '_8192x4096.json'

    srcTiles = readingTileInfos(json_name)

    # empty 8192x4096 resolution frame for visualization 
    vis_frame = np.zeros( (4096,8192) )

    for stile in srcTiles:
        print(stile)

        w = int(stile['orgWidth']) - 2*pix
        h = int(stile['orgHeight']) - 2*pix
        # tile pixel coordinates
        px = int(stile['posX']) + pix
        py = int(stile['posY']) + pix
        # # coded height and width
        # ch = int(srcTiles[caqTile]['codHeight'])
        # cw = int(srcTiles[caqTile]['codWidth'])

        vis_frame[np.round(py):np.round(py + h), np.round(px):np.round(px + w)] = np.ones( (h,w) )* 255

    imageio.imwrite('set_' + schemes[int(args.t_set) + 1] + '_tiling_scheme_' + str(args.t_sch) + '.png', vis_frame)
