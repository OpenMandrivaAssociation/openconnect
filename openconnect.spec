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
Patch0:		%{name}-CVE-2012-3291.patch
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
%patch0 -p0

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



%changelog
* Sat Feb 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.15-2
+ Revision: 780663
- rebuild

* Sun Nov 27 2011 Andrey Bondrov <abondrov@mandriva.org> 3.15-1
+ Revision: 733696
- Fix file list
- New version 3.15

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.10-1
+ Revision: 688436
- new version

* Thu Apr 21 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-1
+ Revision: 656437
- new version

* Thu Mar 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.01-3
+ Revision: 648312
- patch: fix man page typo

* Tue Mar 15 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 3.01-2
+ Revision: 645097
- install authentication helper library too as subpackage

* Tue Mar 15 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 3.01-1
+ Revision: 644984
- new version
- do not build openconnect-nm-auth-dialog and drop patch for it.
  It is provided by networkmanager-openconnect now

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-5mdv2011.0
+ Revision: 603024
- better name for gui subpackage

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-4mdv2011.0
+ Revision: 603007
- split auth dialog into a subpackage, to avoid X11 dependencies

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-3mdv2011.0
+ Revision: 602078
- don't forget build dependencies to really build networkmanager plugin

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-2mdv2011.0
+ Revision: 601848
- don't remove network-manager plugin (thanks Andrey)

* Fri Sep 24 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-1mdv2011.0
+ Revision: 580910
- update to new version 2.26

* Tue Aug 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.25-1mdv2011.0
+ Revision: 571050
- update to new version 2.25

* Sat Aug 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.24-1mdv2011.0
+ Revision: 567316
- update to new version 2.24

* Tue Apr 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.22-1mdv2010.1
+ Revision: 532349
- update to new version 2.22

* Wed Jan 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.21-1mdv2010.1
+ Revision: 490729
- update to new version 2.21

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 2.20-1mdv2010.1
+ Revision: 486893
- update to new version 2.20

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2010.1
+ Revision: 478981
- update to new version 2.12

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.11-1mdv2010.1
+ Revision: 468645
- update to new version 2.11

* Fri Aug 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-2mdv2010.0
+ Revision: 421873
- drop openssl versionned dependency

* Thu Aug 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2010.0
+ Revision: 421763
- import openconnect


* Thu Aug 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2010.0
- initial mdv package, shamelessly stolen from fedora 
