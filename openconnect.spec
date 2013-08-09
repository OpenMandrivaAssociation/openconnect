%define	major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		openconnect
Version:	3.15
Release:	2
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
Url:		http://www.infradead.org/openconnect.html
Source0:	ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Patch0:		%{name}-CVE-2012-3291.patch
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(openssl)

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package -n %{libname}
Summary:	Dynamic libraries for %{name}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc TODO COPYING.LGPL openconnect.html
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libopenconnect.so.%{major}*

%files -n %{devname}
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/%{name}.pc

