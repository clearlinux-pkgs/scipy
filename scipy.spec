#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scipy
Version  : 1.7.3
Release  : 147
URL      : https://github.com/scipy/scipy/releases/download/v1.7.3/scipy-1.7.3.tar.xz
Source0  : https://github.com/scipy/scipy/releases/download/v1.7.3/scipy-1.7.3.tar.xz
Summary  : SciPy: Scientific Library for Python
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSL-1.0 MIT Qhull
Requires: scipy-license = %{version}-%{release}
Requires: scipy-python = %{version}-%{release}
Requires: scipy-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : libc-bin
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pypi(cython)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pythran)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : pypi-pybind11-dev
BuildRequires : python3-dev
BuildRequires : pythran

%description
This is the ARPACK package from
http://www.caam.rice.edu/software/ARPACK/
Specifically the files are from
http://www.caam.rice.edu/software/ARPACK/SRC/arpack96.tar.gz
with the patch
http://www.caam.rice.edu/software/ARPACK/SRC/patch.tar.gz

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
Provides: pypi(scipy)
Requires: pypi(numpy)

%description python3
python3 components for the scipy package.


%prep
%setup -q -n scipy-1.7.3
cd %{_builddir}/scipy-1.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642367086
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scipy
cp %{_builddir}/scipy-1.7.3/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/scipy-1.7.3/doc/sphinxext/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/df4f727b25238b8a4be050714fe3f1cb06b17f75
cp %{_builddir}/scipy-1.7.3/scipy/_lib/_uarray/LICENSE %{buildroot}/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8
cp %{_builddir}/scipy-1.7.3/scipy/_lib/boost/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/scipy-1.7.3/scipy/fft/_pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff
cp %{_builddir}/scipy-1.7.3/scipy/linalg/src/lapack_deprecations/LICENSE %{buildroot}/usr/share/package-licenses/scipy/f9ccbd191ba31d3f0d69b364758122fc908b546d
cp %{_builddir}/scipy-1.7.3/scipy/ndimage/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72
cp %{_builddir}/scipy-1.7.3/scipy/optimize/_highs/LICENSE %{buildroot}/usr/share/package-licenses/scipy/0fb301a89b68fac0ca71fdfbc2522b7b63576dad
cp %{_builddir}/scipy-1.7.3/scipy/optimize/_highs/external/LICENCE_1_0.txt %{buildroot}/usr/share/package-licenses/scipy/3f317fbb3e08fd99169d2e77105d562ea0e482c7
cp %{_builddir}/scipy-1.7.3/scipy/optimize/_highs/external/filereaderlp/LICENSE %{buildroot}/usr/share/package-licenses/scipy/ee3e4ebdf82451452fe0c5c9466d90d76dec773f
cp %{_builddir}/scipy-1.7.3/scipy/optimize/tnc/LICENSE %{buildroot}/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062
cp %{_builddir}/scipy-1.7.3/scipy/sparse/linalg/dsolve/SuperLU/License.txt %{buildroot}/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532
cp %{_builddir}/scipy-1.7.3/scipy/sparse/linalg/eigen/arpack/ARPACK/COPYING %{buildroot}/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58
cp %{_builddir}/scipy-1.7.3/scipy/spatial/qhull_src/COPYING.txt %{buildroot}/usr/share/package-licenses/scipy/5a74d9542429d0f078329ddbd01eb32bf26a88f3
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scipy/0fb301a89b68fac0ca71fdfbc2522b7b63576dad
/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532
/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/scipy/3f317fbb3e08fd99169d2e77105d562ea0e482c7
/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062
/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72
/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8
/usr/share/package-licenses/scipy/5a74d9542429d0f078329ddbd01eb32bf26a88f3
/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff
/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58
/usr/share/package-licenses/scipy/df4f727b25238b8a4be050714fe3f1cb06b17f75
/usr/share/package-licenses/scipy/ee3e4ebdf82451452fe0c5c9466d90d76dec773f
/usr/share/package-licenses/scipy/f9ccbd191ba31d3f0d69b364758122fc908b546d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
