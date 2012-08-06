Summary: Lightweight C++ template library for vector and matrix math
Name: eigen3
Version: 3.1.1
Release: 1
Group: System/Libraries
License: LGPLv3+ or GPLv2+
URL: http://eigen.tuxfamily.org/
Source0: http://bitbucket.org/eigen/eigen/get/%{version}.tar.bz2
BuildRequires: cmake >= 2.6.1
BuildRequires: doxygen
BuildRequires: ghostscript-common
BuildRequires: graphviz
BuildRequires: tetex-dvips
BuildRequires: tetex-latex
BuildRequires: blas-devel
BuildRequires: lapack-devel
BuildRequires: gsl-devel
BuildRequires: qt4-devel
BuildArch: noarch

%description 
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n eigen-eigen-43d9075b23ef

%build
%cmake
%make
make doc

%install
%makeinstall_std -C build

%files
%doc COPYING* build/doc/html/
%dir %{_includedir}/eigen3/
%{_includedir}/eigen3/*
%{_datadir}/pkgconfig/*.pc
