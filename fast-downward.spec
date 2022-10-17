%global debug_package %{nil}

Name: fast-downward
Version: 0.0.0
Release: 1%{?dist}
Summary: Fast Downward is a domain-independent classical planning system.

License: GPLv3
URL: https://github.com/aibasel/downward
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: python3

Requires: python3

%description

%prep
%autosetup

%build
python3 build.py


%install
mkdir -p %{buildroot}/opt/downward
cp fast-downward.py %{buildroot}/opt/downward
cp -r driver %{buildroot}/opt/downward/driver
cp -r builds %{buildroot}/opt/downward/builds

%check


%files
/opt/downward
%license LICENSE.md


%changelog

