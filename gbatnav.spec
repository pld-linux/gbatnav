Summary:	Batalla Naval is a networked multiplayer battleship game
Summary(pl):	Batalla Naval - sieciowa gra wojenna dla wielu graczy
Name:		gbatnav
Version:	1.0.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.sourceforge.net/batnav/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am_fixes.patch
URL:		http://batnav.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Batalla Naval is a networked naval battleship game.

%description -l pl
Batalla Naval to sieciowa gra wojenna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd ggz
	aclocal
	autoconf
cd ..
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games

gzip -9nf AUTHORS README README.IPv6 NEWS TODO ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
