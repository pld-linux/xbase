Summary:	XBase - xbase-compatible C++ class library
Summary(pl):	XBase - kompatybilna z xbase biblioteka klas C++
Name:		xbase
Version:	2.1.1
Release:	2
License:	LGPL (library), GPL (programs)
Group:		Libraries
Source0:	http://dl.sourceforge.net/xdb/%{name}-%{version}.tar.gz
# Source0-md5:	f36852f0ba0c4d9e047e84c3269fde37
Patch0:		%{name}-fix.patch
URL:		http://linux.techass.com/projects/xdb/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XBase is an xbase (i.e. dBase, FoxPro, etc.) compatible C++ class
library. It's useful for accessing data in legacy dBase 3 and 4
database files as well as a general light-weight database engine. It
includes support for DBF (dBase version 3 and 4) data files, NDX and
NTX indexes, and DBT (dBase version 3 and 4). It supports file and
record locking under *nix OSes.

%description -l pl
XBase to kompatybilna z xbase (czyli dBase, FoxPro itp.) biblioteka
klas C++. Jest przydatna do dostêpu do danych w plikach starych baz
dBase 3 i 4, a tak¿e jako lekki silnik baz danych ogólnego
przeznaczenia. Obs³uguje pliki baz DBF (dBase w wersji 3 i 4), indeksy
NDX i NTX oraz DBT (dBase w wersji 3 i 4). Obs³uguje blokowanie
plików i rekordów pod systemami uniksowymi.

%package devel
Summary:	XBase development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych XBase
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains XBase development files.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne przy tworzeniu
aplikacji u¿ywaj±cych Xbase.

%package static
Summary:	Static XBase library
Summary(pl):	Statyczna biblioteka XBase
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XBase library.

%description static -l pl
Statyczna biblioteka XBase.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
%configure \
	--enable-nls \
	--with-exceptions \
	--with-index-ndx \
	--with-index-ntx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/[!x]*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/{*.html,*.jpg}
%attr(755,root,root) %{_bindir}/xbase-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xbase

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
