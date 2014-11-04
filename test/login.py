import os
import sys


p = os.path.join(os.path.dirname(__file__), '..', '..')

sys.path.append(p)

import binaryoptions.marketsworld as mw

m = mw.login('metaperl_rsi')
