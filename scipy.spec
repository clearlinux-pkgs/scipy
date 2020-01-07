#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scipy
Version  : 1.4.1
Release  : 114
URL      : https://github.com/scipy/scipy/releases/download/v1.4.1/scipy-1.4.1.tar.xz
Source0  : https://github.com/scipy/scipy/releases/download/v1.4.1/scipy-1.4.1.tar.xz
Summary  : SciPy: Scientific Library for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT Qhull
Requires: scipy-license = %{version}-%{release}
Requires: scipy-python = %{version}-%{release}
Requires: scipy-python3 = %{version}-%{release}
Requires: Cython
Requires: Jinja2
Requires: Pillow
Requires: matplotlib
Requires: mpmath
Requires: numpy
Requires: pybind11
BuildRequires : Cython
BuildRequires : Jinja2
BuildRequires : Pillow
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : libc-bin
BuildRequires : matplotlib
BuildRequires : mpmath
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pybind11
BuildRequires : pybind11-dev

%description
Author: Enthought, Inc
Austin, TX
enthough-dev@mail.enthought.com
Interpolate is a central package in SciPy, an open-source software package for scientific computing in Python which is maintained by Enthought, Inc.  Interpolate provides functionality for a variety of interpolation techniques, particularly those based on splines.

%package license
Summary: license components for the scipy package.
Group: Default

%description license
license components for the scipy package.


%package python
Summary: python components for the scipy package.
Group: Default
Requires: scipy-python3 = %{version}-%{release}

%description python
python components for the scipy package.


%package python3
Summary: python3 components for the scipy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scipy package.


%prep
%setup -q -n scipy-1.4.1
cd %{_builddir}/scipy-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578418621
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  --fcompiler=gnu95

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scipy
cp %{_builddir}/scipy-1.4.1/doc/scipy-sphinx-theme/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517
cp %{_builddir}/scipy-1.4.1/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/scipy-1.4.1/doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/df4f727b25238b8a4be050714fe3f1cb06b17f75
cp %{_builddir}/scipy-1.4.1/scipy/_lib/_uarray/LICENSE %{buildroot}/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8
cp %{_builddir}/scipy-1.4.1/scipy/fft/_pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff
cp %{_builddir}/scipy-1.4.1/scipy/linalg/src/lapack_deprecations/LICENSE %{buildroot}/usr/share/package-licenses/scipy/f9ccbd191ba31d3f0d69b364758122fc908b546d
cp %{_builddir}/scipy-1.4.1/scipy/ndimage/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72
cp %{_builddir}/scipy-1.4.1/scipy/optimize/tnc/LICENSE %{buildroot}/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062
cp %{_builddir}/scipy-1.4.1/scipy/sparse/linalg/dsolve/SuperLU/License.txt %{buildroot}/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532
cp %{_builddir}/scipy-1.4.1/scipy/sparse/linalg/eigen/arpack/ARPACK/COPYING %{buildroot}/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58
cp %{_builddir}/scipy-1.4.1/scipy/spatial/qhull_src/COPYING.txt %{buildroot}/usr/share/package-licenses/scipy/5a74d9542429d0f078329ddbd01eb32bf26a88f3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532
/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062
/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72
/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8
/usr/share/package-licenses/scipy/5a74d9542429d0f078329ddbd01eb32bf26a88f3
/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff
/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58
/usr/share/package-licenses/scipy/df4f727b25238b8a4be050714fe3f1cb06b17f75
/usr/share/package-licenses/scipy/f9ccbd191ba31d3f0d69b364758122fc908b546d
/usr/share/package-licenses/scipy/fd2e79f66abba5b94347c2df9ca6cf3584b0c517

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
