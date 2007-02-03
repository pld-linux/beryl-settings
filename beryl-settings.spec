Summary:	A GTK+ tool to configure beryl
Summary(pl):	Narz�dzie GTK+ do konfiguracji beryla
Name:		beryl-settings
Version:	0.1.9999.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	77d42004275638bbba38dd0abdbb3f95
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	beryl-settings-bindings-devel >= 1:%{version}
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2.0
Requires:	beryl-core >= 1:%{version}
Requires:	beryl-plugins >= 1:%{version}
Requires:	beryl-settings-bindings
Requires:	python-pygtk-gtk >= 2.0
Obsoletes:	compiz-settings-manager
Obsoletes:	csm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure beryl.

%description -l pl
Narz�dzie GTK+ do konfiguracji beryla.

%prep
%setup -q
echo '#beryl version header' > VERSION
echo VERSION=%{version} >> VERSION

mv -f po/{ca_ES,ca}.po
cat > po/LINGUAS <<EOF
ca
es
nl
pl
EOF

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/beryl-settings
%{_datadir}/bsm
%{_iconsdir}/hicolor/scalable/apps/beryl-settings.svg
%{_desktopdir}/*.desktop
