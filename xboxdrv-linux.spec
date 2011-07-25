
Name:		xboxdrv-linux
License:	GPL
Group:		System/Configuration/Hardware 
URL:		http://pingus.seul.org/~grumbel/xboxdrv/
Autoreqprov:	on
Version:	0.8.1
Release:	%mkrel 1
Summary:	XBox 360 Controller Driver
Source:		http://pingus.seul.org/~grumbel/xboxdrv/%name-%version.tar.bz2
Source1:	xboxdrv.init
Patch0:		%name-Makefile.patch
BuildRequires: SDL-devel zlib-devel GL-devel gcc-c++ scons libusb-devel boost-devel udev-devel glib2-devel dbus-glib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Userspace Xbox/Xbox360 USB Gamepad Driver for Linux

%prep
%setup -q
%patch0 -p0

%build
%make PREFIX=/usr

%install
install -D xboxdrv %{buildroot}%{_bindir}/xboxdrv
install -D doc/xboxdrv-daemon.1 %{buildroot}%{_mandir}/man1/xboxdrv-daemon.1
install -D doc/xboxdrv.1 %{buildroot}%{_mandir}/man1/xboxdrv.1
install -c -D -m 0750 %{_sourcedir}/xboxdrv.init %{buildroot}%{_initrddir}/xboxdrv

# rm %{buildroot}/usr/local/bin/xboxdrv
# rm %{buildroot}/usr/local/man/man1/xboxdrv-daemon.1
# rm %{buildroot}/usr/local/man/man1/xboxdrv.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xboxdrv
%{_mandir}/man1/xboxdrv*
%attr(0750,root,admin) %{_initrddir}/xboxdrv