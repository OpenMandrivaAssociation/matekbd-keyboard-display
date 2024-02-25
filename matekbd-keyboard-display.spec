Summary:	Preview keyboard layouts on MATE desktop
Name:		matekbd-keyboard-display
Version:	23.11.1
Release:	1
License:	LGPLv3+
Group:		Graphical desktop/Other
URL:		https://github.com/tari01/matekbd-keyboard-display/
Source:		https://github.com/tari01/matekbd-keyboard-display/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	python
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libmatekbd)
BuildRequires:	pkgconfig(libxklavier)

%description
An application that allows you to preview keyboard layouts
on MATE desktop. It uses the libmatekbd library, similarly
to gkbd-keyboard-display and libgnomekbd.

%files
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*svg
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake \
	-GNinja
%ninja_build

%install
%ninja_install -C build 


