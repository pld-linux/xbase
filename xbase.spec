Summary:	Xbase DBMS Library
Summary(pl):	Xbase biblioteka dla r�nych baz danych.
Name:		xbase
Version:	1.8.1
Release:	6
Copyright:	LGPL
Group:		Applications/Libraries
Group(pl):	Aplikacje/Biblioteki
Source:		ftp://www.startech.keller.tx.us/pub/xbase/%name-%version.tar.gz
Patch:		xbase-autoconf.patch
URL:		http://www.startech.keller.tx.us/xbase.html
Requires:	libstdc++-devel
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
Bibliotek zawieraj�ca zesp� procerur i funkcji pozwalaj�cych na podstawowe
operacje na na formatacie danych dBASE III i cz�ciowo dBASE IV.

Bazowo projekt powstawa� po Linuxa ale obecnie jest urzywany na wielu
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
Zawiera pliki nag��wkowe potrzebne przy tworzeniu oprogramowania,
oraz modu� dla Turbo Vision.

%prep
%setup -q 
%patch -p1

%build
automake
autoconf
LDFLAGS="-s"
CPPFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-implicit-templates"
export LDFLAGS CPPFLAGS
%configure \
	--enable-nls \
	--with-exceptions \
	--with-index-ndx \
	--with-index-ntx
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog TODO AUTHORS NEWS README

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/{*html,*gif,*jpg}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
