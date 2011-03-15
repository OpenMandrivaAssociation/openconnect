Name:		openconnect
Version:	3.01
Release:	%mkrel 2
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
URL:		http://www.infradead.org/openconnect.html
Source:     ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	dbus-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package static-devel
Summary:	Helper library that implements OpenConnect client authentication
%description
%summary

%prep
%setup -q

%build
# (bor) quick hack so we do not need to patch
sed -i -e 's|/usr/lib|%{_libdir}|g' Makefile
%make

%install
rm -rf %{buildroot}
%makeinstall_std install-lib
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 openconnect.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO COPYING.LGPL openconnect.html
%{_bindir}/openconnect
%{_mandir}/man8/*

%files static-devel
/usr/include/openconnect.h
%{_libdir}/libopenconnect.a
%{_libdir}/pkgconfig/openconnect.pc

