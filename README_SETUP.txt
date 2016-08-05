Hi, welcome.

This Python package uses aksetup for installation, which means that
installation should be easy and quick.

If you don't want to continue reading, just try the regular

  ./configure.py --help
  ./configure.py --some-options
  make
  sudo make install

That should do the trick. (By the way: If a config option says "several ok",
then you may specify several values, separated by commas.)

aksetup also supports regular distutils installation, without using 
configure:

  python setup.py build
  sudo python setup.py install

In this case, configuration is obtained from files in this order:

/etc/aksetup-defaults.py
$HOME/.aksetup-defaults.py
$PACKAGEDIR/siteconf.py

Once you've run configure, you can copy options from your siteconf.py file to
one of these files, and you won't ever have to configure them again manually.
In fact, you may pass the options "--update-user" and "--update-global" to
configure, and it will automatically update these files for you.

This is particularly handy if you want to perform an unattended or automatic
installation via easy_install.

-- Added by Nachiket
To run example OpenCL kernel in emulation mode, three steps:
   
    emconfigutil --xdevice xilinx:adm-pcie-7v3:1ddr:3.0
    xocc --xdevice xilinx:adm-pcie-7v3:1ddr:3.0 -t sw_emu -o example.xclbin example.cl
    XCL_EMULATION_MODE=1 python example.py

You do need to modify the example code to load a binary blob.

    dev =cl.get_platforms()[0].get_devices()
    binary = open("sum.aocx", "rb").read()
    prg = cl.Program(ctx,dev,[binary])
    prg.build();

Furthermore, the direct call to the kernel does not seem to work. Have to use the method indicated on page -- https://documen.tician.de/pyopencl/runtime_program.html 

    sum_knl = prg.sum
    sum_knl.set_args(a_g, b_g, res_g)
    ev = cl.enqueue_nd_range_kernel(queue, sum_knl, a_np.shape, None)


More instructions at https://paper.dropbox.com/doc/PyOpenCL-for-Xilinx-FPGAs-tT2KOlxwe2YGWNBdKNyzx	
