Summary:	Batalla Naval is a networked multiplayer battleship game
Name:		gbatnav
Version:	0.74.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/batnav/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://batnav.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Batallla Naval is a networked naval battleship game.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
alclocal -I macros
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
