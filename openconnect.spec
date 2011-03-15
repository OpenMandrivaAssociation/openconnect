Name:		openconnect
Version:	3.01
Release:	%mkrel 1
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

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 openconnect.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO COPYING.LGPL openconnect.html
%{_bindir}/openconnect
%{_mandir}/man8/*
