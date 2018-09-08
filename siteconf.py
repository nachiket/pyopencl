CL_TRACE = False
CL_ENABLE_GL = False
CL_USE_SHIPPED_EXT = True
CL_PRETEND_VERSION = '1.1'
CL_INC_DIR = []
CL_LIB_DIR = [
        '/opt/altera_pro/16.0/hld/board/de5a_net/linux64/lib', 
        '/opt/altera_pro/16.0/hld/host/linux64/lib', 
        '/opt/altera/16.0/hld/board/de1soc/arm32/lib', 
        '/opt/altera/16.0/hld/board/de5net/linux64/lib', 
        '/opt/altera/16.0/hld/board/s5_ref/linux64/lib', 
        '/opt/altera/16.0/hld/host/linux64/lib']
CL_LIBNAME = ['alteracl', 'alterahalmmd', 'elf','terasic_a10_mmd']
CXXFLAGS = ['-std=c++0x']
LDFLAGS = ['-Wl,--no-as-needed']
