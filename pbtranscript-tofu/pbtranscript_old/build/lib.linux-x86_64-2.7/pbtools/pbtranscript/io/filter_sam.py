#!/usr/bin/env python

"""Gmap can occationally produce alignments with bad cigar string.
In order to prevent these alignments from breaking downstream analysis
such as samtools and samtoh5, we need to remove them."""

import sys
import logging
import os.path as op
from pbcore.util.ToolRunner import PBToolRunner
from pbtools.pbtranscript.__init__ import get_version
from pbtools.pbtranscript.Utils import filter_sam

class SAMFilterRunner(PBToolRunner):
    """Gmap filter runner."""
    def __init__(self):
        desc = "Filter gmap sam alignments which have bad cigar strings."
        PBToolRunner.__init__(self, desc)
        self.parser.add_argument("in_sam", type=str, help="Input sam file.")
        self.parser.add_argument("out_sam", type=str, help="Output sam file.")

    def getVersion(self):
        """Get version string."""
        return get_version()

    def run(self):
        """Run"""
        logging.info("Running {f} v{v}.".format(f=op.basename(__file__),
                                                v=self.getVersion()))
        try:
            filter_sam(self.args.in_sam, self.args.out_sam)
        except ValueError as e:
            logging.error(str(e))
            import traceback
            traceback.print_exc()
            return 1
        return 0


def main():
    """Main function"""
    runner = SAMFilterRunner()
    return runner.start()


if __name__ == "__main__":
    sys.exit(main())

