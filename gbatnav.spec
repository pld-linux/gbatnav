%define name	gbatnav
%define ver	0.74.0
%define rel	1
%define prefix  /usr

Summary: Batalla Naval is a networked multiplayer battleship game.
Name:		%name
Version:	%ver
Release:	%rel
Copyright:	GPL
Group:		Amusements/Games
Source:		http://www.pjn.gov.ar/~rquesada/progs/%{name}-%{ver}.tar.gz
URL:		http://www.pjn.gov.ar/~rquesada/batnav.html
Requires:       gtk+ >= 1.2.0
BuildRoot:      /var/tmp/%{name}-%{ver}-root
Docdir:		%{prefix}/doc

%description
Batallla Naval is a networked naval battleship game.

%changelog
* Fri Jun 25 1999 Gregory McLean <gregm@comstar.net>

- Initial spec file written.

%prep
%setup -q

%build
%ifarch alpha
 MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
MYCFLAGS="$RPM_OPT_FLAGS"
CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README README.IPv6 NEWS TODO ChangeLog
%{prefix}/bin/*
%{prefix}/share/pixmaps/*
%{prefix}/share/locale/*/*/*
%{prefix}/share/gnome/apps/Games/*
%{prefix}/share/gnome/help/*/*
