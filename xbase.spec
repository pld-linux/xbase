Summary:	Xbase DBMS Library
Summary(pl):	Xbase biblioteka dla ró¿nych baz danych.
Name:		xbase
Version:	1.8.1
Release:	3
Copyright:	LGPL
Group:		Applications/Libraries
Group(pl):	Aplikacje/Biblioteki
Source:		ftp://www.startech.keller.tx.us/pub/xbase/%name-%version.tar.gz
URL:		http://www.startech.keller.tx.us/xbase.html
Buildroot:	/tmp/%{name}-%{version}-root

%description
This product provides C and C++ programmers a class and function library for
manipulating Xbase type datafiles and indices. This project was formerly
known as Xbase for Linux, but as I have recieved input from several people
who are compiling this on platforms other than Linux, I have renamed it to
Xbase DBMS.  The main development of this library however, remains on the
Linux platform utilizing the GCC public domain C/C++ compiler.

XBase DBMS currently includes routines to support multi-user access for .DBF
databases, fields, Dbase III and IV memo fields (variable length fields),
dates, record and file locking and (.NDX) indices.  As of release 1.7.4,
Xbase is compatible with dBASE III data, index and memo fields and also has
support for some dBASE IV features.

%description -l pl
Bibliotek zawieraj±ca zespó³ procerur i funkcji pozwalaj±cych na podstawowe
operacje na na formatacie danych dBASE III i czê¶ciowo dBASE IV.

Bazowo projekt powstawa³ po Linuxa ale obecnie jest urzywany na wielu
platformach.

%package devel
Summary:	Xbase development
Summary(pl):	Xbase delelopment
Group:		Applications/Libraries
Group(pl):	Aplikacje/Biblioteki
Requires:	%{name} = %{version}

%description devel
Include headers and Turbo Vision module in source.

%description devel -l pl
Zawiera pliki nag³ówkowe potrzebne przy tworzeniu oprogramowania,
oraz modu³ dla Turbo Vision.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CPPFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-implicit-templates" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-nls \
	--with-exceptions \
	--with-index-ndx \
	--with-index-ntx
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

install -d $RPM_BUILD_ROOT/usr/doc/%name-%version

gzip -9nf ChangeLog TODO AUTHORS NEWS README

#strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root)%{_bindir}/*
%attr(755,root,root)%{_libdir}/lib*.so*.*

%files devel
%defattr(644,root,root,755)
%doc html/{*html,*gif,*jpg}
%attr(755,root,root)%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/libxbase.la

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.8.1-3]
- more rpm macros.

* Thu Apr 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.8.1-2]
- recompiles on new rpm.

* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.8.1-1]
- added passing $RPM_OPT_FLAGS in CFLAGS and CPPFLAGS; in CPPFLAGS
  added "-fno-rtti -fno-implicit-templates",
- added "-s" to LDFLAGS,
- added stripping shared libraries,
- added URL,
- fixed Copyright (LGPL).

* Wed Apr 14 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate file,
- update to version 1.8.1

* Sat Dec 12 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- building RPM.
