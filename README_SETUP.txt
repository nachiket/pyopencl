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

  LDFLAGS="-Wl,--no-as-needed" python setup.py build
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
To run example OpenCL kernel, two steps:
   
    aoc -march=emulator -v example.cl -o example.aocx
    CL_CONTEXT_EMULATOR_DEVICE_ALTERA=1  PYOPENCL_CTX='0' python example.py

You do need to modify the example code to load a binary blob.

    dev =cl.get_platforms()[0].get_devices()
    binary = open("example.aocx", "rb").read()
    prg = cl.Program(ctx,dev,[binary])
    prg.build();
    
More instructions/notes at https://paper.dropbox.com/doc/PyOpenCL-with-Altera-FPGAs-8ojfCVUBhiz7UOjRTIaFe
