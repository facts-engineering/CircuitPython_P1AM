from micropython import const

# MDB Constants
DISCRETE_IN = const(0)
ANALOG_IN = const(1)
DISCRETE_OUT = const(2)
ANALOG_OUT = const(3)
STATUS_IN = const(4)
CONFIG_LEN = const(5)
DATA_TYPE = const(6)
P1_NAME = const(7)
DEFAULT_CONFIG = const(8)

# Special Types
TEMP_MODULE = const(32)
PWM_MODULE = const(0xA0)
HSC_MODULE = const(0xC0)

# PWM Constants
PWM_FREQ = const(1)
PWM_DUTY = const(0)
PWM_FREQ_MAX = const(20000)
PWM_DUTY_MAX = 100.0

# P1-04AD Range Constants
AD_RANGES = (
    (0.0, 20.0),
    (0.0, 10.0),
    (0.0, 5.0),
    (0.0, 20.0),
    (0.0, 10.0)
)

# Status Constants
MISSING24V_STATUS = const(3)
BURNOUT_STATUS = const(5)
UNDER_RANGE_STATUS = const(7)
OVER_RANGE_STATUS = const(11)

# Data buffer and word size
analog_word_size = const(4)
data_buf = bytearray(550)

# indexing mode
USE_1_INDEXING = True

# Base Controller pins
CS = None
ACK = None
BC_SPI = None

# fmt: off
# Module info and parameters
mdb = {         #di ai do ao st cf dt
    0x00000000: (0, 0, 0, 0, 0, 0, 0, "Empty"),  # Empty first entry for defaults
    0x04A00081: (1, 0, 0, 0, 0, 0, 1, "P1-08ND3"),
    0x04A00085: (1, 0, 0, 0, 0, 0, 1, "P1-08NA"),
    0x04A00087: (1, 0, 0, 0, 0, 0, 1, "P1-08SIM"),
    0x04A00088: (1, 0, 0, 0, 0, 0, 1, "P1-08NE3"),
    0x04A00042: (1, 0, 0, 0, 0, 0, 1, "P1-08ND-TTL"),
    0x05200082: (2, 0, 0, 0, 0, 0, 1, "P1-16ND3"),
    0x05200089: (2, 0, 0, 0, 0, 0, 1, "P1-16NE3"),
    0x14030050: (0, 0, 1, 0, 0, 0, 1, "P1-04TRS"),
    0x1403F481: (0, 0, 0, 32, 4, 4, PWM_MODULE, "P1-04PWM", (0x02,0x02,0x02,0x02)),
    0x1404008D: (0, 0, 1, 0, 0, 0, 1, "P1-08TA"),
    0x1404008F: (0, 0, 1, 0, 0, 0, 1, "P1-08TRS"),
    0x14040091: (0, 0, 2, 0, 0, 0, 1, "P1-16TR"),
    0x14050081: (0, 0, 1, 0, 0, 0, 1, "P1-08TD1"),
    0x14050082: (0, 0, 1, 0, 0, 0, 1, "P1-08TD2"),
    0x14050046: (0, 0, 1, 0, 0, 0, 1, "P1-08TD-TTL"),
    0x14080085: (0, 0, 2, 0, 0, 0, 1, "P1-15TD1"),
    0x14080086: (0, 0, 2, 0, 0, 0, 1, "P1-15TD2"),
    0x24A50081: (1, 0, 1, 0, 0, 0, 1, "P1-16CDR"),
    0x24A50082: (1, 0, 1, 0, 0, 0, 1, "P1-15CDD1"),
    0x24A50083: (1, 0, 1, 0, 0, 0, 1, "P1-15CDD2"),
    0x34605581: (0, 16,0,  0, 12, 18, 16, "P1-04AD", (0x40,0x03,0x00,0x00,
                                                      0x20,0x03,0x00,0x00,
                                                      0x21,0x03,0x00,0x00,
                                                      0x22,0x03,0x00,0x00,
                                                      0x23,0x03)),
    0x34605588: (0, 16,0,  0, 12, 8, TEMP_MODULE, "P1-04RTD", (0x40,0x03,0x60,0x05,
                                                      0x20,0x01,0x80,0x00)),
    0x34605582: (0, 16,0,  0, 12, 2, 16, "P1-04AD-1", (0x40, 0x03)),
    0x34605583: (0, 16,0,  0, 12, 2, 16, "P1-04AD-2", (0x40, 0x03)),
    0x3460558F: (0, 16,0,  0, 12, 2, 12, "P1-04ADL-1", (0x40, 0x03)),
    0x34605590: (0, 16,0,  0, 12, 2, 12, "P1-04ADL-2", (0x40, 0x03)),
    0x34608C81: (0, 16,0,  0, 12, 20, TEMP_MODULE, "P1-04THM", (0x40,0x03,0x60,0x05,
                                                      0x21,0x00,0x22,0x00,
                                                      0x23,0x00,0x24,0x00,
                                                      0x00,0x00,0x00,0x00,
                                                      0x00,0x00,0x00,0x00)),
    0x34608C8E: (0, 16,0,  0, 12, 8, TEMP_MODULE, "P1-04NTC", (0x40,0x03,0x60,0x05,
                                                      0x20,0x00,0x80,0x02)),
    0x34A0558A: (0, 32,0,  0, 12, 2, 12, "P1-08ADL-1", (0x40, 0x07)),
    0x34A0558B: (0, 32,0,  0, 12, 2, 12, "P1-08ADL-2", (0x40, 0x07)),
    0x34A5A481: (2, 36,0,  36, 4, 12, HSC_MODULE, "P1-02HSC", (0x00,0x00,0x00,0x00,
                                                         0x00,0x00,0x00,0x01,
                                                         0x00,0x00,0x00,0x01)),
    0x44035583: (0, 0, 0, 16, 4, 0, 12, "P1-04DAL-1"),
    0x44035584: (0, 0, 0, 16, 4, 0, 12, "P1-04DAL-2"),
    0x44055588: (0, 0, 0, 32, 4, 0, 12, "P1-08DAL-1"),
    0x44055589: (0, 0, 0, 32, 4, 0, 12, "P1-08DAL-2"),
    0x5461A783: (0, 16,0,  8, 12, 2, 12, "P1-4ADL2DAL-1", (0x40, 0x03)),
    0x5461A784: (0, 16,0,  8, 12, 2, 12, "P1-4ADL2DAL-2", (0x40, 0x03)),
    0xFFFFFFFF: (0, 0, 0, 0, 0, 0, 0, "BAD SLOT"),  # empty or bad
}
# fmt: on

odd_length_modules = (0x14080085, 0x14080086, 0x24A50082, 0x24A50083)