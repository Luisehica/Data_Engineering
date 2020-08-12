import argparse
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd

from article import Articlefrom base import Base, Engine, Session

def

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file ypu want to load into the database',
                        type=str)

    args = parser.parse_args()
    main(args.filename)