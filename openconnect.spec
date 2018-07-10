%define major 5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		openconnect
Version:	7.08
Release:	4
Summary:	Open client for Cisco AnyConnect VPN

Group:		Networking/Other
License:	LGPLv2+
Url:		http://www.infradead.org/openconnect.html
Source0:	ftp://ftp.infradead.org:21/pub/openconnect/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnutls)
# our version 1.0.0e of OpenSSL is known to be broken with Cisco DTLS.
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	vpnc

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

%build
%configure --disable-static --with-vpnc-script=/etc/vpnc/vpnc-script \
	--with-openssl --without-openssl-version-check --with-default-gnutls-priority="@SYSTEM" \

%make

%install
%makeinstall_std

%check
%make check

%find_lang %{name}

%files -f %{name}.lang
%doc TODO COPYING.LGPL
%{_sbindir}/%{name}
%{_mandir}/man8/*

%files -n %{libname}
%{_libdir}/libopenconnect.so.%{major}*

%files -n %{devname}
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/%{name}.pc
