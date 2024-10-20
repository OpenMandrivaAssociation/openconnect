%define major 5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		openconnect
Version:	9.12
Release:	1
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
Url:		https://www.infradead.org/openconnect.html
# use sailfish branch
# https://git.sailfishos.org/mirror/openconnect/tree/master
Source0:	ftp://ftp.infradead.org/pub/openconnect/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(libpskc)
BuildRequires:	pkgconfig(libp11)
BuildRequires:	pkgconfig(stoken)
BuildRequires:	pkgconfig(tss2-esys)
BuildRequires:	vpnc
Requires:	opensc
Requires:	p11-kit
Requires:	vpnc

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package -n %{libname}
Summary:	Dynamic libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
#./autogen.sh
%configure \
	--disable-static \
	--disable-dsa-tests \
	--with-vpnc-script=/etc/vpnc/vpnc-script \
	--with-openssl \
	--without-openssl-version-check \
	--with-default-gnutls-priority="@SYSTEM"

%make_build

%install
%make_install
rm -f %{buildroot}/usr/libexec/%{name}/hipreport-android.sh

%find_lang %{name}

%check
%make_build check VERBOSE=1 ||:

%files -f %{name}.lang
%doc TODO COPYING.LGPL
%{_sbindir}/%{name}
%{_datadir}/bash-completion/completions/*
%{_mandir}/man8/*
%{_libexecdir}/openconnect/*

%files -n %{libname}
%{_libdir}/libopenconnect.so.%{major}*

%files -n %{devname}
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/doc/%{name}/
