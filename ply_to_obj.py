'''
Simple script to convert ply to obj models
'''

from argparse import ArgumentParser
from plyfile import PlyData


def main():
    parser = ArgumentParser()
    parser.add_argument('ply_filename')
    parser.add_argument('obj_filename')

    args = parser.parse_args()

    convert(PlyData.read(args.ply_filename), args.obj_filename)

def convert(ply, obj):
    '''
    Convert given ply data
    '''

    with open(obj, 'w') as f:
        f.write("# OBJ file\n")

        verteces = ply['vertex']

        for v in verteces:
            p = [v['x'], v['y'], v['z']]
            c = [ v['red'] / 256 , v['green'] / 256 , v['blue'] / 256 ]
            a = p + c
            f.write("v %.6f %.6f %.6f %.6f %.6f %.6f \n" % tuple(a) )

        for v in verteces:
            n = [0,0,0]#[ v['nx'], v['ny'], v['nz'] ]
            f.write("vn %.6f %.6f %.6f\n" % tuple(n))

        for v in verteces:
            t = [0,0]#[ v['s'], v['t'] ]
            f.write("vt %.6f %.6f\n" % tuple(t))

        if 'face' in ply:
            for i in ply['face']['vertex_indices']:
                f.write("f")
                for j in range(i.size):
                    # ii = [ i[j]+1 ]
                    ii = [ i[j]+1, i[j]+1, i[j]+1 ]
                    # f.write(" %d" % tuple(ii) )
                    f.write(" %d/%d/%d" % tuple(ii) )
                f.write("\n")

main()
