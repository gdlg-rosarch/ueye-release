Name:           ros-indigo-ueye
Version:        0.0.3
Release:        2%{?dist}
Summary:        ROS ueye package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ueye
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-camera-calibration-parsers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs

%description
Driver for IDS Imaging uEye cameras.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Sep 21 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.3-2
- Autogenerated by Bloom

* Thu Sep 18 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.2-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.2-1
- Autogenerated by Bloom

* Sun Sep 21 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.3-1
- Autogenerated by Bloom

* Sun Sep 21 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.3-0
- Autogenerated by Bloom

* Sun Sep 14 2014 Kevin Hallenbeck <kmhallen@oakand.edu> - 0.0.1-0
- Autogenerated by Bloom

