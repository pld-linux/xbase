Summary:	XBase - xbase-compatible C++ class library
Summary(pl.UTF-8):	XBase - kompatybilna z xbase biblioteka klas C++
Name:		xbase
Version:	2.1.1
Release:	5
License:	LGPL v2.1+ (library), GPL v2+ (programs)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xdb/%{name}-%{version}.tar.gz
# Source0-md5:	f36852f0ba0c4d9e047e84c3269fde37
Patch0:		%{name}-fix.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-am.patch
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

%description -l pl.UTF-8
XBase to kompatybilna z xbase (czyli dBase, FoxPro itp.) biblioteka
klas C++. Jest przydatna do dostępu do danych w plikach starych baz
dBase 3 i 4, a także jako lekki silnik baz danych ogólnego
przeznaczenia. Obsługuje pliki baz DBF (dBase w wersji 3 i 4), indeksy
NDX i NTX oraz DBT (dBase w wersji 3 i 4). Obsługuje blokowanie
plików i rekordów pod systemami uniksowymi.

%package devel
Summary:	XBase development files
Summary(pl.UTF-8):	Pliki dla programistów używających XBase
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains XBase development files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne przy tworzeniu
aplikacji używających Xbase.

%package static
Summary:	Static XBase library
Summary(pl.UTF-8):	Statyczna biblioteka XBase
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XBase library.

%description static -l pl.UTF-8
Statyczna biblioteka XBase.

%package tools
Summary:	XBase utilities for xbase files
Summary(pl.UTF-8):	XBase - narzędzia do plików xbase
License:	GPL v2+
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description tools
XBase utilities for xbase files.

%description tools -l pl.UTF-8
XBase - narzędzia do plików xbase.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
%configure \
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
%attr(755,root,root) %{_libdir}/libxbase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxbase.so.1

%files devel
%defattr(644,root,root,755)
%doc html/{*.html,*.jpg}
%attr(755,root,root) %{_bindir}/xbase-config
%attr(755,root,root) %{_libdir}/libxbase.so
%{_libdir}/libxbase.la
%{_includedir}/xbase

%files static
%defattr(644,root,root,755)
%{_libdir}/libxbase.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkndx
%attr(755,root,root) %{_bindir}/copydbf
%attr(755,root,root) %{_bindir}/dbfutil1
%attr(755,root,root) %{_bindir}/dbfxtrct
%attr(755,root,root) %{_bindir}/deletall
%attr(755,root,root) %{_bindir}/dumphdr
%attr(755,root,root) %{_bindir}/dumprecs
%attr(755,root,root) %{_bindir}/packdbf
%attr(755,root,root) %{_bindir}/reindex
%attr(755,root,root) %{_bindir}/undelall
%attr(755,root,root) %{_bindir}/zap
