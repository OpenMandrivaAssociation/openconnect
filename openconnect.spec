Name:		openconnect
Version:	2.01
Release:	%mkrel 2
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
URL:		http://www.infradead.org/openconnect.html
Source:     ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Patch:      openconnect-2.01-fix-format-errors.patch
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	dbus-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%prep
%setup -q
%patch -p 1

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 openconnect.8 %{buildroot}%{_mandir}/man8

# remove network-manager plugin if build
rm -f %{buildroot}/usr/libexec/nm-openconnect-auth-dialog

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO COPYING.LGPL openconnect.html
%{_bindir}/openconnect
%{_mandir}/man8/*

