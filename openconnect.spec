%define	major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		openconnect
Version:	3.15
Release:	2
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
URL:		http://www.infradead.org/openconnect.html
Source0:	ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	dbus-devel

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package -n %{libname}
Summary:	Dynamic libraries for %{name}

%description -n %{libname}
This package contains libraries for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc TODO COPYING.LGPL openconnect.html
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libopenconnect.so.%{major}*

%files -n %{develname}
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/%{name}.pc

