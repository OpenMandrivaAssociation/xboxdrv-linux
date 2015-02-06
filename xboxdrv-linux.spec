Name:		xboxdrv-linux
License:	GPL
Group:		System/Configuration/Hardware 
URL:		http://pingus.seul.org/~grumbel/xboxdrv/
#Autoreqprov:	on
Version:	0.8.5
Release:	2
Summary:	XBox 360 Controller Driver
Source0:	http://pingus.seul.org/~grumbel/xboxdrv/%name-%version.tar.bz2
Source1:	xboxdrv.service
Patch0:		%{name}-Makefile.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(gl)
BuildRequires:	scons
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)

Requires(pre): rpm-helper
Requires(postun): rpm-helper

%description
Userspace Xbox/Xbox360 USB Gamepad Driver for Linux

%prep
%setup -q
# %patch0 -p0

%build
%setup_compile_flags
%scons BUILD=custom \
	CXX="%{__cxx}" \
	CXXFLAGS="-Wall %optflags" \
	LINKFLAGS="%{ldflags}"

%install
install -D xboxdrv %{buildroot}%{_bindir}/xboxdrv
install -D doc/xboxdrv-daemon.1 %{buildroot}%{_mandir}/man1/xboxdrv-daemon.1
install -D doc/xboxdrv.1 %{buildroot}%{_mandir}/man1/xboxdrv.1
install -D -m644 %SOURCE1 %{buildroot}%{_unitdir}/%{name}.service

%post
%_post_service xboxdrv

%preun
%_preun_service xboxdrv

%files
%doc PROTOCOL NEWS AUTHORS COPYING README examples
%{_bindir}/xboxdrv
%{_mandir}/man1/xboxdrv*
%{_unitdir}/%{name}.service
