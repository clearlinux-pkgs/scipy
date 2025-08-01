#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v27
# autospec commit: 65cf152
#
Name     : scipy
Version  : 1.16.0
Release  : 189
URL      : https://github.com/scipy/scipy/releases/download/v1.16.0/scipy-1.16.0.tar.gz
Source0  : https://github.com/scipy/scipy/releases/download/v1.16.0/scipy-1.16.0.tar.gz
Summary  : Fundamental algorithms for scientific computing in Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT
Requires: scipy-license = %{version}-%{release}
Requires: scipy-python = %{version}-%{release}
Requires: scipy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libc-bin
BuildRequires : meson
BuildRequires : meson-python3
BuildRequires : openblas
BuildRequires : pkgconfig(openblas)
BuildRequires : pypi(cython)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pythran)
BuildRequires : pypi-cython
BuildRequires : pypi-meson_python
BuildRequires : pypi-numpy
BuildRequires : pypi-pybind11-dev
BuildRequires : pypi-pythran
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains zstr 1.0.5 form https://github.com/mateidavid/zstr.
The code is licensed under MIT license, see ../../LICENSE.

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
Provides: pypi(scipy)

%description python3
python3 components for the scipy package.


%prep
%setup -q -n scipy-1.16.0
cd %{_builddir}/scipy-1.16.0
pushd ..
cp -a scipy-1.16.0 buildavx2
popd
pushd ..
cp -a scipy-1.16.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750688711
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scipy
cp %{_builddir}/scipy-%{version}/doc/source/_static/scipy-mathjax/LICENSE %{buildroot}/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/scipy-%{version}/scipy/_build_utils/tempita/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/860ce1e3089e4750ef43d9973281f1062f93636b || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/_uarray/LICENSE %{buildroot}/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/array_api_compat/LICENSE %{buildroot}/usr/share/package-licenses/scipy/927759ae3ddc659922e7615a27be84e8579cf180 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/array_api_extra/LICENSE %{buildroot}/usr/share/package-licenses/scipy/7b22805d76eae6b4bc05bfab5932a9f3f7f43df8 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/cobyqa/LICENSE %{buildroot}/usr/share/package-licenses/scipy/fd809a645b70dfce5aee6903b64b015b64e3a127 || :
cp %{_builddir}/scipy-%{version}/scipy/_lib/pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/scipy/b1881ea58a8dacfb4e8965ca56be6cbbe9f53be1 || :
cp %{_builddir}/scipy-%{version}/scipy/fft/_pocketfft/LICENSE.md %{buildroot}/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff || :
cp %{_builddir}/scipy-%{version}/scipy/io/_fast_matrix_market/fast_matrix_market/dependencies/fast_float/LICENSE-MIT %{buildroot}/usr/share/package-licenses/scipy/11e6be99fa6ad788d013a38598c7da3e5d90efbe || :
cp %{_builddir}/scipy-%{version}/scipy/io/_fast_matrix_market/fast_matrix_market/dependencies/ryu/LICENSE-Boost %{buildroot}/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/scipy-%{version}/scipy/ndimage/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72 || :
cp %{_builddir}/scipy-%{version}/scipy/optimize/_direct/COPYING %{buildroot}/usr/share/package-licenses/scipy/0c65a98a772b9aa5d3b6bf331102ab6ad8d0f698 || :
cp %{_builddir}/scipy-%{version}/scipy/optimize/tnc/LICENSE %{buildroot}/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_dsolve/SuperLU/License.txt %{buildroot}/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_eigen/arpack/ARPACK/COPYING %{buildroot}/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58 || :
cp %{_builddir}/scipy-%{version}/scipy/sparse/linalg/_propack/PROPACK/license.txt %{buildroot}/usr/share/package-licenses/scipy/6688c21dab3d2394af6a740ae061178e7f0c4f01 || :
cp %{_builddir}/scipy-%{version}/subprojects/boost_math/math/LICENSE %{buildroot}/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90 || :
cp %{_builddir}/scipy-%{version}/subprojects/highs/LICENSE.txt %{buildroot}/usr/share/package-licenses/scipy/2b805b6f67ce6ac0e3cd11361b4b4a9c03bf80df || :
cp %{_builddir}/scipy-%{version}/subprojects/highs/extern/LICENCE_1_0.txt %{buildroot}/usr/share/package-licenses/scipy/3f317fbb3e08fd99169d2e77105d562ea0e482c7 || :
cp %{_builddir}/scipy-%{version}/subprojects/highs/extern/filereaderlp/LICENSE %{buildroot}/usr/share/package-licenses/scipy/ee3e4ebdf82451452fe0c5c9466d90d76dec773f || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scipy/0c65a98a772b9aa5d3b6bf331102ab6ad8d0f698
/usr/share/package-licenses/scipy/1088e18e7415cdcdfc4b3647a33837cc272b6532
/usr/share/package-licenses/scipy/11e6be99fa6ad788d013a38598c7da3e5d90efbe
/usr/share/package-licenses/scipy/2b805b6f67ce6ac0e3cd11361b4b4a9c03bf80df
/usr/share/package-licenses/scipy/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/scipy/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/scipy/3f317fbb3e08fd99169d2e77105d562ea0e482c7
/usr/share/package-licenses/scipy/41248a200801dfbc906b81e9a00c811474b64062
/usr/share/package-licenses/scipy/58744c28e64b1d647917e9a8490b869221629c72
/usr/share/package-licenses/scipy/589977b80bebdf03e98a6f333b7e0e7a5fd804b8
/usr/share/package-licenses/scipy/612568676ab43b80b877fce96fa4a917137117ff
/usr/share/package-licenses/scipy/6688c21dab3d2394af6a740ae061178e7f0c4f01
/usr/share/package-licenses/scipy/7b22805d76eae6b4bc05bfab5932a9f3f7f43df8
/usr/share/package-licenses/scipy/860ce1e3089e4750ef43d9973281f1062f93636b
/usr/share/package-licenses/scipy/927759ae3ddc659922e7615a27be84e8579cf180
/usr/share/package-licenses/scipy/a8322a2036b23080e6706a894c314b9f477dce58
/usr/share/package-licenses/scipy/b1881ea58a8dacfb4e8965ca56be6cbbe9f53be1
/usr/share/package-licenses/scipy/ee3e4ebdf82451452fe0c5c9466d90d76dec773f
/usr/share/package-licenses/scipy/fd809a645b70dfce5aee6903b64b015b64e3a127

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
