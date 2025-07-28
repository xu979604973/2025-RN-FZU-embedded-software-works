
def GetCPPPATH(BSP_ROOT, RTT_ROOT):
	CPPPATH=[
		RTT_ROOT + "/bsp/qemu-vexpress-a9",
		RTT_ROOT + "/bsp/qemu-vexpress-a9/applications",
		RTT_ROOT + "/bsp/qemu-vexpress-a9/build/kernel/components/lwp/arch/arm/cortex-a",
		RTT_ROOT + "/bsp/qemu-vexpress-a9/drivers",
		RTT_ROOT + "/components/dfs/filesystems/devfs",
		RTT_ROOT + "/components/dfs/filesystems/elmfat",
		RTT_ROOT + "/components/dfs/filesystems/ramfs",
		RTT_ROOT + "/components/dfs/filesystems/romfs",
		RTT_ROOT + "/components/dfs/include",
		RTT_ROOT + "/components/drivers/include",
		RTT_ROOT + "/components/drivers/spi",
		RTT_ROOT + "/components/drivers/spi/sfud/inc",
		RTT_ROOT + "/components/finsh",
		RTT_ROOT + "/components/libc/aio",
		RTT_ROOT + "/components/libc/compilers/musl",
		RTT_ROOT + "/components/libc/compilers/musl/libc/include",
		RTT_ROOT + "/components/libc/compilers/newlib",
		RTT_ROOT + "/components/libc/libdl",
		RTT_ROOT + "/components/libc/mmap",
		RTT_ROOT + "/components/libc/termios",
		RTT_ROOT + "/components/lwp",
		RTT_ROOT + "/components/net/lwip-2.0.2/src",
		RTT_ROOT + "/components/net/lwip-2.0.2/src/arch/include",
		RTT_ROOT + "/components/net/lwip-2.0.2/src/include",
		RTT_ROOT + "/components/net/lwip-2.0.2/src/include/ipv4",
		RTT_ROOT + "/components/net/lwip-2.0.2/src/include/netif",
		RTT_ROOT + "/components/net/netdev/include",
		RTT_ROOT + "/components/net/sal_socket/impl",
		RTT_ROOT + "/components/net/sal_socket/include",
		RTT_ROOT + "/components/net/sal_socket/include/dfs_net",
		RTT_ROOT + "/components/net/sal_socket/include/socket",
		RTT_ROOT + "/components/net/sal_socket/include/socket/sys_socket",
		RTT_ROOT + "/include",
		RTT_ROOT + "/libcpu/arm/common",
		RTT_ROOT + "/libcpu/arm/cortex-a",
	]

	return CPPPATH

def GetCPPDEFINES():
	CPPDEFINES=['_STDC_PREDEF_H', '__STDC_ISO_10646__=201206L']
	return CPPDEFINES

