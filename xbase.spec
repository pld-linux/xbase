Summary:	XBase - xbase-compatible C++ class library
Summary(pl):	XBase - kompatybilna z xbase biblioteka klas C++
Name:		xbase
Version:	2.0.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xdb/%{name}-%{version}.tar.gz
# Source0-md5:	9b29362031716a12491beb9f8cc882f2
URL:		http://linux.techass.com/projects/xdb/
BuildRequires:	libstdc++-devel
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
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains XBase development files.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne przy tworzeniu
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/[!x]*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/{*.html,*.gif,*.jpg}
%attr(755,root,root) %{_bindir}/xbase-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xbase
