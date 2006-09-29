#
Summary:	A GTK+ tool to configure beryl
Summary(pl):	Narzêdzie GTK+ do konfiguracji beryla
Name:		beryl-settings
Version:	0.1.0
Release:	0.1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://distfiles.xgl-coffee.org/beryl-settings/%{name}-%{version}.tar.bz2
# Source0-md5:	acf657ff5cae7c4ec4314fd2eb314839
URL:		http://distfiles.xgl-coffee.org
BuildRequires:	gtk+2-devel >= 2.0
Requires:	beryl-core
Requires:	beryl-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure beryl.

%description -l pl
Narzêdzie GTK+ do konfiguracji beryla.

%prep
%setup -q -n %{name}

%build
autoreconf -v --install
%{__intltoolize}
%{__glib_gettextize} --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/beryl-settings
%{_desktopdir}/beryl-settings.desktop
%{_pixmapsdir}/*.svg
%{_datadir}/beryl/hints
