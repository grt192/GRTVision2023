# Install apriltag
# https://github.com/AprilRobotics/apriltag
wget -c https://github.com/AprilRobotics/apriltag/archive/refs/tags/v3.2.0.tar.gz
tar -xzf v3.2.0.tar.gz
cd apriltag-3.2.0

cmake -B . -DCMAKE_BUILD_TYPE=Release
cmake --build . --target install

# Test apriltag Python module
# python3
# import apriltag


# Fix apriltag Python import error (.so)
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH


# Install pupil-apriltags
# https://github.com/pupil-labs/apriltags
pip3 install --upgrade pip setuptools wheel
pip3 install pupil-apriltags

# Test pupil-apriltags module
# python3
# import pupil_apriltags