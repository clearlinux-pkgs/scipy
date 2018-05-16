#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scipy
Version  : 1.1.0
Release  : 87
URL      : http://pypi.debian.net/scipy/scipy-1.1.0.tar.gz
Source0  : http://pypi.debian.net/scipy/scipy-1.1.0.tar.gz
Summary  : SciPy: Scientific Library for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT Qhull
Requires: scipy-python3
Requires: scipy-python
Requires: Jinja2
Requires: Pillow
Requires: Sphinx
Requires: libc-bin
Requires: matplotlib
Requires: numpy
Requires: pytest-timeout
Requires: pytest-xdist
BuildRequires : Jinja2
BuildRequires : Sphinx
BuildRequires : libc-bin
BuildRequires : numpy
BuildRequires : numpy-legacypython
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
science, and engineering. The SciPy library
        depends on NumPy, which provides convenient and fast N-dimensional
        array manipulation. The SciPy library is built to work with NumPy
        arrays, and provides many user-friendly and efficient numerical
        routines such as routines for numerical integration and optimization.
        Together, they run on all popular operating systems, are quick to
        install, and are free of charge.  NumPy and SciPy are easy to use,
        but powerful enough to be depended upon by some of the world's
        leading scientists and engineers. If you need to manipulate
        numbers on a computer and display or publish the results,
        give SciPy a try!

%package legacypython
Summary: legacypython components for the scipy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the scipy package.


%package python
Summary: python components for the scipy package.
Group: Default
Requires: scipy-python3

%description python
python components for the scipy package.


%package python3
Summary: python3 components for the scipy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scipy package.


%prep
%setup -q -n scipy-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525558826
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
python2 setup.py build -b py2 --fcompiler=gnu95
python3 setup.py build -b py3 --fcompiler=gnu95

%install
export SOURCE_DATE_EPOCH=1525558826
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
