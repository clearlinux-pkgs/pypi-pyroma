#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyroma
Version  : 4.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/6d/03/ec5c0630476fefd9ea76fa71ab9d780133e918c983d22513c3603bd7c93d/pyroma-4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/03/ec5c0630476fefd9ea76fa71ab9d780133e918c983d22513c3603bd7c93d/pyroma-4.1.tar.gz
Summary  : Test your project's packaging friendliness
Group    : Development/Tools
License  : MIT
Requires: pypi-pyroma-bin = %{version}-%{release}
Requires: pypi-pyroma-license = %{version}-%{release}
Requires: pypi-pyroma-python = %{version}-%{release}
Requires: pypi-pyroma-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(build)
BuildRequires : pypi(docutils)
BuildRequires : pypi(flit_core)
BuildRequires : pypi(pep517)
BuildRequires : pypi(pygments)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(trove_classifiers)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zope.event)

%description


%package bin
Summary: bin components for the pypi-pyroma package.
Group: Binaries
Requires: pypi-pyroma-license = %{version}-%{release}

%description bin
bin components for the pypi-pyroma package.


%package license
Summary: license components for the pypi-pyroma package.
Group: Default

%description license
license components for the pypi-pyroma package.


%package python
Summary: python components for the pypi-pyroma package.
Group: Default
Requires: pypi-pyroma-python3 = %{version}-%{release}

%description python
python components for the pypi-pyroma package.


%package python3
Summary: python3 components for the pypi-pyroma package.
Group: Default
Requires: python3-core
Provides: pypi(pyroma)
Requires: pypi(build)
Requires: pypi(docutils)
Requires: pypi(pep517)
Requires: pypi(pygments)
Requires: pypi(requests)
Requires: pypi(setuptools)
Requires: pypi(trove_classifiers)
Requires: pypi(wheel)
Requires: pypi(zope.event)

%description python3
python3 components for the pypi-pyroma package.


%prep
%setup -q -n pyroma-4.1
cd %{_builddir}/pyroma-4.1
pushd ..
cp -a pyroma-4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669824149
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyroma
cp %{_builddir}/pyroma-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pyroma/b0fc0d8365766fe5b3c0ed32016393c8441272d7 || :
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

%files bin
%defattr(-,root,root,-)
/usr/bin/pyroma

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyroma/b0fc0d8365766fe5b3c0ed32016393c8441272d7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
