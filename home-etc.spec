Summary:	HOME-ETC support programs and scripts
Summary(pl.UTF-8):   Skrypty i programy zapewniające wsparcie dla HOME-ETC
Name:		home-etc
Version:	1.0.9
Release:	4
Epoch:		1
License:	LGPL
Group:		Base
Source0:	ftp://ftp.pld-linux.org/people/siefca/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	628d3acd77458e291f753992d81977c4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	coreutils
Requires:	shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
provides support for it.

%description -l pl.UTF-8
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zapewnia wsparcie dla tego
mechanizmu.

%package lib
Summary:	HOME-ETC Library
Summary(pl.UTF-8):   Biblioteka mechanizmu HOME-ETC
License:	LGPL
Group:		Libraries

%description lib
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains shared HOME-ETC library.

%description lib -l pl.UTF-8
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera bibliotekę dzieloną
HOME-ETC.

%package devel
Summary:	Header files for HOME-ETC
Summary(pl.UTF-8):   Pliki nagłówkowe dla mechanizmu HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description devel
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains header files needed to build HOME-ETC-compliant applications.

%description devel -l pl.UTF-8
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera pliki nagłówkowe
potrzebne do budowania aplikacji zgodnych z HOME-ETC.

%package static
Summary:	Static version of HOME-ETC library
Summary(pl.UTF-8):   Wersja statyczna biblioteki HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains static version of the library.

%description static -l pl.UTF-8
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera statyczną wersję
biblioteki.

%package examples
Summary:	Example files for HOME-ETC
Summary(pl.UTF-8):   Pliki przykładów dla mechanizmu HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains examples, which explains how to modify existing applications.

%description examples -l pl.UTF-8
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera pliki przykładów,
które wyjaśniają w jaki sposób modyfikować istniejące aplikacje.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libexecdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS README doc/HOME-ETC.pl.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /etc/profile.d/home-etc.*sh
/etc/skel/.home_etc

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/DEVEL-NOTES FILES TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
