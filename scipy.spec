#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scipy
Version  : 0.18.0
Release  : 56
URL      : http://pypi.debian.net/scipy/scipy-0.18.0.tar.gz
Source0  : http://pypi.debian.net/scipy/scipy-0.18.0.tar.gz
Summary  : SciPy: Scientific Library for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear MIT Qhull
Requires: scipy-python
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Here's what is available (all in double precision):
LSODE
LSODES
LSODA
LSODAR
LSODI
LSOIBT

%package python
Summary: python components for the scipy package.
Group: Default

%description python
python components for the scipy package.


%prep
%setup -q -n scipy-0.18.0

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
python2 setup.py build -b py2 --fcompiler=gnu95
python3 setup.py build -b py3 --fcompiler=gnu95

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
