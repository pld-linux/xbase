Summary: Xbase DBMS Library
Summary(pl): Xbase biblioteka dla ró¿nych baz danych.
Name: xbase
Version: 1.8.1
Release: 1
Copyright: GPL
Group: Applications/Libraries
Group(pl): Aplikacje/Biblioteki
Source: %name-%version.tar.gz
#Source1: %{name}174c-html.tar.gz
Buildroot: /tmp/%{name}-%{version}-root

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
Summary: Xbase development
Summary(pl): Xbase delelopment
Group: Applications/Libraries
Group(pl): Aplikacje/Biblioteki
Requires: xbase = %{version}

%description devel
Include headers and Turbo Vision module in source.

%description devel -l pl
Zawiera pliki nag³ówkowe potrzebne przy tworzeniu oprogramowania,
oraz modu³ dla Turbo Vision.

%prep
%setup -q 

%build
./configure \
	--prefix=/usr \
	--enable-nls \
	--with-exceptions \
	--with-index-ndx \
	--with-index-ntx
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make prefix=$RPM_BUILD_ROOT/usr install

install -d $RPM_BUILD_ROOT/usr/doc/%name-%version

cp ChangeLog TODO AUTHORS NEWS README \
$RPM_BUILD_ROOT/usr/doc/%name-%version/
gzip -9nf $RPM_BUILD_ROOT/usr/doc/%name-%version/*

install -d $RPM_BUILD_ROOT/usr/doc/%name-%version/html
install -d $RPM_BUILD_ROOT/usr/doc/%name-devel-%version/tv

cp -Rdp html/ $RPM_BUILD_ROOT/usr/doc/%name-%version/html
cp -Rdp tv/ $RPM_BUILD_ROOT/usr/doc/%name-devel-%version/tv

strip $RPM_BUILD_ROOT/usr/bin/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root)/usr/bin/*
%attr(755, root, root)/usr/lib/*.so*
/usr/doc/%name-%version/html

%files devel
%defattr(644, root, root, 755)
/usr/include/
%attr(644, root, root)/usr/lib/libxbase.la
/usr/doc/%name-devel-%version/tv

%changelog
* Wed Apr 14 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.8.1-1]
- separate file,
- update to version 1.8.1

* Sat Dec 12 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- building RPM.
