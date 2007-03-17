Summary:	A GTK+ tool to configure beryl
Summary(pl.UTF-8):	Narzędzie GTK+ do konfiguracji beryla
Name:		beryl-settings
Version:	0.2.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	cc58ac1aae61bb4dae8e6da693c398a2
Patch0:		%{name}-desktop.patch
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
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	beryl-core >= 1:%{version}
Requires:	beryl-plugins >= 1:%{version}
Requires:	beryl-settings-bindings >= 1:%{version}
Requires:	python-pygtk-gtk >= 2.0
Obsoletes:	compiz-settings-manager
Obsoletes:	csm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure beryl.

%description -l pl.UTF-8
Narzędzie GTK+ do konfiguracji beryla.

%prep
%setup -q
%patch0 -p1
echo '#beryl version header' > VERSION
echo VERSION=%{version} >> VERSION

mv -f po/{hu_HU,hu}.po
mv -f po/{pt_PT,pt}.po
cat > po/LINGUAS <<EOF
ca
es
es_AR
fr
hu
it
ja
ko
nl
pl
pt
zh_CN
zh_HK
zh_TW
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

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/beryl-settings
%{_datadir}/bsm
%{_iconsdir}/hicolor/scalable/apps/beryl-settings.svg
%{_desktopdir}/beryl-settings.desktop
