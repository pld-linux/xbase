Summary:	Xbase DBMS Library
Summary(pl):	Xbase - biblioteka dla ró¿nych baz danych
Name:		xbase
Version:	2.0.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/xdb/%{name}-%{version}.tar.gz
URL:		http://linux.techass.com/projects/xdb/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This product provides C and C++ programmers a class and function
library for manipulating Xbase type datafiles and indices. This
project was formerly known as Xbase for Linux, but as I have recieved
input from several people who are compiling this on platforms other
than Linux, I have renamed it to Xbase DBMS. The main development of
this library however, remains on the Linux platform utilizing the GCC
public domain C/C++ compiler.

XBase DBMS currently includes routines to support multi-user access
for .DBF databases, fields, Dbase III and IV memo fields (variable
length fields), dates, record and file locking and (.NDX) indices. As
of release 1.7.4, Xbase is compatible with dBASE III data, index and
memo fields and also has support for some dBASE IV features.

%description -l pl
Bibliotek zawieraj±ca zespó³ procedur i funkcji pozwalaj±cych na
podstawowe operacje na na formacie danych dBASE III i czê¶ciowo
dBASE IV.

Bazowo projekt powstawa³ pod Linuksa ale obecnie jest u¿ywany na wielu
platformach.

%package devel
Summary:	Xbase development files
Summary(pl):	Xbase dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Xbase development files.

%description devel -l pl
Zawiera pliki nag³ówkowe potrzebne przy tworzeniu oprogramowania
aplikacji u¿ywaj±cych Xbase.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcflags} -fno-rtti -fno-implicit-templates"
export CPPFLAGS
%configure2_13 \
	--enable-nls \
	--with-exceptions \
	--with-index-ndx \
	--with-index-ntx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/[^x]*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/{*.html,*.gif,*.jpg}
%attr(755,root,root) %{_bindir}/xbase-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xbase
