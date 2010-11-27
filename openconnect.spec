Name:		openconnect
Version:	2.26
Release:	%mkrel 3
Summary:	Open client for Cisco AnyConnect VPN
Group:		Networking/Other
License:	LGPLv2+
URL:		http://www.infradead.org/openconnect.html
Source:     ftp://ftp.infradead.org/pub/openconnect/openconnect-%{version}.tar.gz
Patch:      openconnect-2.01-fix-format-errors.patch
BuildRequires:	openssl-devel
BuildRequires:	libxml2-devel
BuildRequires:	gtk2-devel
BuildRequires:	libGConf2-devel
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

# libexecdir is actually libdir on mandriva
install -d -m 755 %{buildroot}%{_libexecdir}
mv %{buildroot}%{_prefix}/libexec/nm-openconnect-auth-dialog \
    %{buildroot}%{_libexecdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc TODO COPYING.LGPL openconnect.html
%{_bindir}/openconnect
%{_mandir}/man8/*
%{_libexecdir}/nm-openconnect-auth-dialog
