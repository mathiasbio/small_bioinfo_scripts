#!/usr/bin/python

import argparse

def calc_cov(covfile, mincov, bedout):
    regiondict = {}
    mincov = int(mincov)
    with open(covfile, "r") as readcovfile:
        for row in readcovfile:
            region = row.strip("\n").split("\t")
            chrom = region[0]
            cov = int(region[2])
            pos = int(region[1])
            
            if chrom not in regiondict:
                regiondict[chrom] = []
            if cov < mincov:
                continue
            regiondict[chrom].append(pos)

    with open(bedout, "w") as bedfile:
        for chrom in regiondict:
            oldpos = regiondict[chrom][0]
            start = regiondict[chrom][0]
            for pos in regiondict[chrom]:
                distance = pos - oldpos
                if distance > 1:
                    if start == oldpos:
                        start -= 1
                    writethis = [str(chrom), str(start), str(oldpos)]
                    bedfile.write("\t".join(writethis) + "\n")
                    start = pos
                oldpos = pos

                    
#    regions = {}
#    for chrom in regiondict:
#        oldpos = 0
#        for pos in regiondict[chrom]:
#            posdiff = oldpos - pos
#            if posdiff > 1:
#                if chrom not in regions:
#                    regions[chrom] = []
#                regions[chrom]
#                start =
#                stop =
#            else:
#               stop = pos
                 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--covfile', nargs='?', help='the mpileup coverage file', required=True)
    parser.add_argument('-m', '--mincov', nargs='?', help='min coverage to merge to consecutive regions', required=True)
    parser.add_argument('-b', '--bedpath', nargs='?', help='path to output bedfile', required=True)
    args = parser.parse_args()
    calc_cov(args.covfile, args.mincov, args.bedpath)
