Summary:	HOME-ETC support programs and libraries
Summary(pl):	Biblioteki i programy zapewniające wsparcie dla HOME-ETC
Name:		home-etc
Version:	1.0.8
Release:	1
Epoch:		1
License:	LGPL
Group:		Base
Requires:	coreutils
Requires:	shadow
Source0:	ftp://ftp.pld-linux.org/people/siefca/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	78b644c45a4808a8be235004b7b0ff86
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
provides support for it.

%description -l pl
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zapewnia wsparcie dla tego
mechanizmu.

%package static
Summary:	Static version of HOME-ETC library
Summary(pl):	Wersja statyczna biblioteki HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains static elements of the library.

%description static -l pl
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera statyczne elementy
biblioteki.

%package devel
Summary:	Header files for HOME-ETC
Summary(pl):	Pliki nagłówkowe dla mechanizmu HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains header files needed to build HOME-ETC-compliant applications.

%description devel -l pl
HOME-ETC jest pomysłem, aby przechowywać pliki konfiguracyjne
w podkatalogu wskazanym przez użytkownika, zamiast bezpośrednio
w jego katalogu domowym. Pakiet ten zawiera pliki nagłówkowe
potrzebne do budowania aplikacji zgodnych z HOME-ETC.

%package examples
Summary:	Example files for HOME-ETC
Summary(pl):	Pliki przykładów dla mechanizmu HOME-ETC
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description examples
HOME-ETC is an idea to keep configuration files in a subdirectory
specified by user, instead of its home directory. This package
contains examples, which explains how to modify existing applications.

%description examples -l pl
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
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man3
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT/etc/profile.d
install -d $RPM_BUILD_ROOT/etc/skel

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README CONTRIBUTORS AUTHORS COPYING doc/HOME-ETC.pl.txt
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /etc/profile.d/home-etc.*sh
/etc/skel/.home_etc

%files devel
%defattr(644,root,root,755)
%doc doc/DEVEL-NOTES AUTHORS CONTRIBUTORS COPYING FILES TODO
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}/*
