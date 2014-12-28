Summary:	Batalla Naval is a networked multiplayer battleship game
Summary(pl.UTF-8):	Batalla Naval - sieciowa gra wojenna dla wielu graczy
Name:		gbatnav
Version:	1.0.4
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9975f2d4d0c481fd97a910958007b42d
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-po.patch
URL:		http://batnav.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Batalla Naval is a networked naval battleship game.

%description -l pl.UTF-8
Batalla Naval to sieciowa gra wojenna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README README.IPv6 NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
