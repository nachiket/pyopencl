# source ./compile.sh

python setup.py clean
CFLAGS=-I/home/root/opencl_arm32_rte/host/include/ LDFLAGS="-Wl,--no-as-needed"  python setup.py build
python setup.py install
