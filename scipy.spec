#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scipy
Version  : 1.9.3
Release  : 159
URL      : https://github.com/scipy/scipy/releases/download/v1.9.3/scipy-1.9.3.tar.gz
Source0  : https://github.com/scipy/scipy/releases/download/v1.9.3/scipy-1.9.3.tar.gz
Summary  : Fundamental algorithms for scientific computing in Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT Qhull
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : libc-bin
BuildRequires : meson
BuildRequires : meson-python3
BuildRequires : openblas
BuildRequires : pypi(cython)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pyomo)
BuildRequires : pypi(pythran)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : pypi-meson_python
BuildRequires : pypi-pybind11-dev
BuildRequires : pypi-pythran

%description
PROPACK Version 2.1,                              Stanford, April 2005
OVERVIEW
This directory contains a Fortran version of the PROPACK software,
which is designed to efficiently compute the singular values and
singular vectors of a large, sparse and/or structured matrix. The
basic Krylov-subspace algorithm used is Lanczos bidiagonalization,
implemented with partial reorthogonalization. The use of partial
reorthogonalization often improves performance significantly compared
to the classic Lanczos algorithm with full reorthogonalization; the
exact amount of improvement depends on the distribution of the
singular values. Two sets of SVD routines are available, on with and
one without implicit restarting. Implicit restarting allows the
computation of a given number of singular values and corresponding
vectors to be done in a fixed amount of memory. The amount of memory
used by the ordinary version is proportional to the number of
iterations required for the singular values to converge, and this is
generally not known in advance, but since the total number of
matrix-vector multiplications needed is usually lower for the
non-restarted version it still can be the method of choice in many
cases.

%prep
%setup -q -n scipy-1.9.3
cd %{_builddir}/scipy-1.9.3
pushd ..
cp -a scipy-1.9.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666713770
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scipy
cp %{_builddir}/scipy-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/2ec2c7738e484a6277a75c9a9c29e02be515e1d7 || :
cp %{_builddir}/scipy-%{version}/LICENSES_bundled.txt %{buildroot}/usr/share/package-licenses/scipy/e84650e600b1cfd0e3773d90d1ca1162c7daeae2 || :
cp %{_builddir}/scipy-%{version}/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/_uarray/LICENSE %{buildroot}/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/boost/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/highs/LICENSE %{buildroot}/usr/share/package-licenses/scipy/946411ef4b46d0a5e23ec3925b66cd920e60bab7 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/highs/extern/LICENCE_1_0.txt %{buildroot}/usr/share/package-licenses/scipy/3f317fbb3e08fd99169d2e77105d562ea0e482c7 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/highs/extern/filereaderlp/LICENSE %{buildroot}/usr/share/package-licenses/scipy/ee3e4ebdf82451452fe0c5c9466d90d76dec773f || :
cp %{_builddir}/scipy-%{version}/scipy/fft/_pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff || :
cp %{_builddir}/scipy-%{version}/scipy/ndimage/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72 || :
cp %{_builddir}/scipy-%{version}/scipy/optimize/_direct/COPYING %{buildroot}/usr/share/package-licenses/scipy/0c65a98a772b9aa5d3b6bf331102ab6ad8d0f698 || :
cp %{_builddir}/scipy-%{version}/scipy/optimize/tnc/LICENSE %{buildroot}/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_dsolve/SuperLU/License.txt %{buildroot}/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_eigen/arpack/ARPACK/COPYING %{buildroot}/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_propack/PROPACK/license.txt %{buildroot}/usr/share/package-licenses/scipy/6688c21dab3d2394af6a740ae061178e7f0c4f01 || :
cp %{_builddir}/scipy-%{version}/scipy/spatial/qhull_src/COPYING.txt %{buildroot}/usr/share/package-licenses/scipy/5a74d9542429d0f078329ddbd01eb32bf26a88f3 || :
cp %{_builddir}/scipy-%{version}/tools/wheels/LICENSE_linux.txt %{buildroot}/usr/share/package-licenses/scipy/1ebdf28ff73201013bcbe34d7b181aae83c74cd4 || :
cp %{_builddir}/scipy-%{version}/tools/wheels/LICENSE_win32.txt %{buildroot}/usr/share/package-licenses/scipy/8d17aef32ae993da00875f545870929a7e1a6ed4 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
