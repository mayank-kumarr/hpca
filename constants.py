import m5
from m5.objects import *

# Fixed
CPU_MODEL = DerivO3CPU
CLOCK_FREQ = '2GHz'
MEM_MODE = 'timing'
MEM_SIZE = '1GB'
MEM_TYPE = DDR3_1600_8x8
NUM_ROB = 1
L1_TAG_LATENCY = 2
L1_DATA_LATENCY = 2
L1_RESPONSE_LATENCY = 2
L1_MSHRS = 4
L1_TGSTS_PER_MSHR = 20
L2_TAG_LATENCY = 20
L2_DATA_LATENCY = 20
L2_RESPONSE_LATENCY = 20
L2_MSHRS = 20
L2_TGSTS_PER_MSHR = 12
CACHE_LINE = 64
L1_ASSOC = 4
L2_ASSOC = 8

# Variable
LQ_ENTRIES = [32, 64]
SQ_ENTRIES = [32, 64]
L1D_SIZE = ['32kB', '64kB']
L1I_SIZE = ['8kB', '16kB']
L2_SIZE = ['256kB', '512kB']
BP_TYPE = [TournamentBP, BiModeBP]
ROB_ENTRIES = [128, 192]
IQ_ENTRIES = [16, 64]