CL_TRACE = False
CL_ENABLE_GL = False
CL_USE_SHIPPED_EXT = True
CL_PRETEND_VERSION = '1.1'
CL_INC_DIR = []
CL_LIB_DIR = [
        '/home/root/opencl_arm32_rte/board/c5soc/arm32/lib', 
        '/home/root/opencl_arm32_rte/host/arm32/lib']
CL_LIBNAME = ['alteracl', 'alterammdpcie', 'elf','stdc++']
#CL_LIBNAME = ['OpenCL', 'alteracl', 'acl_emulator_kernel_rt', 'alterahalmmd',
#                      'alterammdpcie', 'c_accel_runtime', 'elf']
CXXFLAGS = ['-std=c++0x']
LDFLAGS = ['-Wl,--no-as-needed']
