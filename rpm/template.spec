Name:           ros-jade-heatmap
Version:        0.2.4
Release:        0%{?dist}
Summary:        ROS heatmap package

Group:          Development/Libraries
License:        GPLv3
URL:            https://www.dks.ruhr-uni-bochum.de/en/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-costmap-2d
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-move-base-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospy
Requires:       ros-jade-std-msgs
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-costmap-2d
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-move-base-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-visualization-msgs

%description
The heatmap package allows you to create a WIFI-heatmap

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Aug 26 2015 Adrian Bauer <adrian.bauer@rub.de> - 0.2.4-0
- Autogenerated by Bloom

* Wed Aug 26 2015 Adrian Bauer <adrian.bauer@rub.de> - 0.2.3-1
- Autogenerated by Bloom

* Mon Aug 24 2015 Adrian Bauer <adrian.bauer@rub.de> - 0.2.3-0
- Autogenerated by Bloom

* Sun Jul 19 2015 Adrian Bauer <adrian.bauer@rub.de> - 0.2.2-0
- Autogenerated by Bloom

