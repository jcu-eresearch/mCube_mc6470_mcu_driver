Import('env')
Import("projenv")

import sys, os
from os.path import join

print(projenv, file=sys.stderr)
env.Append(CFLAGS=[
    "-I{}".format(join(os.getcwd(), "MC7XXX_MCU_1.0.0/sensor/inc")),
    "-I{}".format(join(os.getcwd(), "MC7XXX_MCU_1.0.0/sensor/inc/mag")),
    "-I{}".format(join(os.getcwd(), "MC7XXX_MCU_1.0.0/sensor/inc/accel")),
    "-I{}".format(join(os.getcwd(), "MC7XXX_MCU_1.0.0/platform/bus")),
    "-I{}".format(join(os.getcwd(), "MC7XXX_MCU_1.0.0/platform/console")),
    ])

print()
