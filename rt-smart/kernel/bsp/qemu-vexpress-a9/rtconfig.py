import os

import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return "#define AUTOMAC".join([str(int(e/2) + 1) + '  0x' + mac[e:e+2] + '\n' for e in range(5,11,2)])

header = '''
#ifndef __MAC_AUTO_GENERATE_H__
#define __MAC_AUTO_GENERATE_H__

/* Automatically generated file; DO NOT EDIT. */
/* mac configure file for RT-Thread qemu */

#define AUTOMAC0  0x52
#define AUTOMAC1  0x54
#define AUTOMAC2  0x00
#define AUTOMAC'''

end = '''
#endif
'''

automac_h_fn = os.path.join(os.path.dirname(__file__), 'drivers', 'automac.h')
with open(automac_h_fn, 'w') as f:
    f.write(header + get_mac_address() + end)

# toolchains options
ARCH        ='arm'
CPU         ='cortex-a'
CROSS_TOOL  = 'gcc'
PLATFORM    = 'gcc'
EXEC_PATH   = os.getenv('RTT_EXEC_PATH') or '/usr/bin'
BUILD       = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX  = os.getenv('RTT_CC_PREFIX') or 'arm-none-eabi-'
    CC      = PREFIX + 'gcc'
    CXX     = PREFIX + 'g++'
    AS      = PREFIX + 'gcc'
    AR      = PREFIX + 'ar'
    LINK    = PREFIX + 'gcc'
    TARGET_EXT = 'elf'
    SIZE    = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY  = PREFIX + 'objcopy'
    STRIP   = PREFIX + 'strip'
    CFPFLAGS = ' -msoft-float'
    AFPFLAGS = ' -mfloat-abi=softfp -mfpu=neon'
    DEVICE   = ' -march=armv7-a -mtune=cortex-a7 -ftree-vectorize -ffast-math -funwind-tables -fno-strict-aliasing'

    CXXFLAGS= DEVICE + CFPFLAGS + ' -Wall'
    CFLAGS  = DEVICE + CFPFLAGS + ' -Wall -std=gnu99'
    AFLAGS  = ' -c' + AFPFLAGS + ' -x assembler-with-cpp'
    LFLAGS  = DEVICE + ' -Wl,--gc-sections,-Map=rtthread.map,-cref,-u,system_vectors -T link.lds' + ' -lsupc++ -lgcc'
    CPATH   = ''
    LPATH   = ''
    
    ##M_CFLAGS - 动态模块编译时用到的 C 代码编译参数，一般此处以 PIC 方式进行编译（即代码地址支持浮动方式执行）；
    ##M_CXXFLAGS - 动态模块编译时用到的 C++ 代码编译参数，参数和上面的 M_CFLAGS 类似；
    ##M_LFLAGS - 动态模块进行链接时的参数。同样是 PIC 方式，并且是按照共享库方式链接（部分链接）；
    ##M_POST_ACTIOn - 动态模块编译完成后要进行的动作，这里会对 elf 文件进行 strip 下，以减少 elf 文件的大小；
    M_CFLAGS = CFLAGS + ' -mlong-calls -fPIC '
    M_CXXFLAGS = CXXFLAGS + ' -mlong-calls -fPIC'
    M_LFLAGS = DEVICE + CXXFLAGS + ' -Wl,--gc-sections,-z,max-page-size=0x4' +\
                                    ' -shared -fPIC -nostartfiles -nostdlib -static-libgcc'
    M_POST_ACTION = STRIP + ' -R .hash $TARGET\n' + SIZE + ' $TARGET \n'
    if BUILD == 'debug':
        CFLAGS   += ' -O0 -gdwarf-2'
        CXXFLAGS += ' -O0 -gdwarf-2'
        AFLAGS   += ' -gdwarf-2'
    else:
        CFLAGS   += ' -Os'
        CXXFLAGS += ' -Os'
    CXXFLAGS += ' -Woverloaded-virtual -fno-exceptions -fno-rtti'

DUMP_ACTION = OBJDUMP + ' -D -S $TARGET > rtt.asm\n'
POST_ACTION = OBJCPY + ' -O binary $TARGET rtthread.bin\n' + SIZE + ' $TARGET \n'
