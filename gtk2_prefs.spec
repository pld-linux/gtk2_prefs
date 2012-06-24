Summary:	GTK+ preference utility - theme and font switcher
Summary(pl):	Preferencje GTK+ - zmiana motywu i czcionki
Name:		gtk2_prefs
Version:	0.4.0
Release:	0.2
License:	GPL v2
Group:		X11/Applications
Source0:	http://members.lycos.co.uk/alexv6/pub/gtk/%{name}-%{version}.tar.bz2
# Source0-md5:	95291299651fe34f18017a11fc0ca933
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://members.lycos.co.uk/alexv6/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ version 2 preference utility - theme and font switcher.

%description -l pl
Preferencje GTK+ - zmiana motywu i czcionki.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

#%post
#%%update_desktop_database_post

#%postun
#%%update_desktop_database_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
