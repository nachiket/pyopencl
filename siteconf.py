CL_TRACE = False
CL_ENABLE_GL = False
CL_USE_SHIPPED_EXT = True
CL_PRETEND_VERSION = '1.1'
CL_INC_DIR = []
CL_LIB_DIR = [
        '/opt/altera/16.0/hld/board/terasic/de5net/linux64/lib', 
        '/opt/altera/16.0/hld/board/terasic/s5_ref/linux64/lib', 
        '/opt/altera/16.0/hld/host/linux64/lib']
CL_LIBNAME = ['alteracl', 'alterahalmmd', 'elf']
CXXFLAGS = ['-std=c++0x']
LDFLAGS = ['-Wl,--no-as-needed']
