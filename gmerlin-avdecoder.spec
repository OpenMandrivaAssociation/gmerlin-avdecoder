Name: gmerlin-avdecoder
Summary: A multimedia decoding library
Version: 1.0.0
Release: %mkrel 1
Url: http://gmerlin.sourceforge.net/
License: LGPLv2+
Group: Video
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://downloads.sourceforge.net/gmerlin/%name-%version.tar.gz
Patch0: gmerlin-avdecoder-1.0.0-fix-str-fmt.patch
BuildRequires: gavl-devel >= 1.1.0
BuildRequires: gmerlin-devel >= 0.4.0
BuildRequires: gmerlin >= 0.4.0
BuildRequires: ffmpeg-devel
BuildRequires: oggvorbis-devel
BuildRequires: libmpeg2dec-devel
BuildRequires: libtheora-devel
BuildRequires: a52dec-devel a52dec
BuildRequires: speex-devel
BuildRequires: png-devel
BuildRequires: libmjpegtools-devel
BuildRequires: libflac-devel
BuildRequires: libcdio-devel
BuildRequires: tiff-devel
BuildRequires: libsmbclient-devel
BuildRequires: gettext

%description
This is gmerlin_avdecoder, a multimedia decoding library.
It it primarly a support library for gmerlin, but it can also be
used as a standalone library for getting sophisticated media file
decoding support for your application.

%files -f %name.lang
%defattr(-,root,root)
%_bindir/*
%_libdir/gmerlin/plugins/*.so

#--------------------------------------------------------------------

%define major 1
%define libname %mklibname gmerlin_avdec %major

%package -n %libname
Group: System/Libraries
Summary: Libraries for %name
Requires: %name = %version

%description -n %libname
This package contains shared libraries for %name.

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname -d gmerlin_avdec

%package -n %develname
Group: Development/Other
Summary: Development files for %name
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %develname
This package contains development files for %name.

%files -n %develname
%defattr(-,root,root)
%_includedir/gmerlin/*.h
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --without-doxygen
%make

%install
rm -rf %buildroot
%makeinstall_std

rm -f %buildroot%_libdir/gmerlin/plugins/*.la

%find_lang %name

%clean
rm -rf %buildroot
