# FIXME: unbundle QtSystemInfo used by src/version/version.cpp

%define oname Fritzing
%define lname %(echo %oname | tr [:upper:] [:lower:])

Summary:	An Electronic Design Automation software with a low entry barrier
Name:		%{lname}
Version:	0.9.3b	
Release:	1
Group:		Sciences/Other
# LGPLv2+   src/lbb/QtSystemInfo
# CC-BY-SA  docs 
# LGPLv2+   others
License:	GPLv3+ and CC-BY-SA and LGPLv2+
URL:		https://github.com/%{name}/
Source0:	https://github.com/%{name}/%{name}-app/archive/%{version}/%{name}-app-%{version}.tar.gz
Source1:	https://github.com/%{name}/%{name}-parts/archive/%{version}/%{name}-parts-%{version}.tar.gz
Patch0:	%{name}-0.9.3b-disable_auto_update.patch
Patch1:	%{name}-0.9.3b-use_system_font.patch
Patch2:	%{name}-0.9.3b-use_system_libgit2.patch
Patch3:	%{name}-0.9.3b-use_system_libboost.patch

BuildRequires:	desktop-file-utils
BuildRequires:	font(droidsans)
BuildRequires:	font(droidsansmono)
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Gui)
#BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5SerialPort)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	qt5-devel
BuildRequires:	quazip-devel
BuildRequires:	twitter4j

Requires:	%{name}-parts >= %{version}
Requires:	font(droidsans)
Requires:	font(droidsansmono)
Requires:	twitter4j

%description
The Fritzing application is an Electronic Design Automation software with a
low entry barrier, suited for the needs of makers and hobbyists. It offers a
unique real-life "breadboard" view, and a parts library with many commonly
used high-level components. Fritzing makes it very easy to communicate about
circuits, as well as to turn them into PCB layouts ready for production. It
is particularly popular among Arduino and Raspberry Pi users, and is widely
used in education and creative tinkering.

%files -f %{name}.lang
%{_bindir}/%{oname}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/sketches
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/syntax
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{oname}.1*
%doc readme.md
%doc LICENSE.GPL2
%doc LICENSE.GPL3
%doc LICENSE.CC-BY-SA

#----------------------------------------------------------------------------

%package parts
Summary:	Common data for %{oname}
Group:		Development/Other

%description parts
ANN is a library written in the C++ programming language to support both
exact and approximate nearest neighbor searching in spaces of various
dimensions. It was implemented by David M. Mount of the University of
Maryland, and Sunil Arya of the Hong Kong University of Science and
Technology. ANN (pronounced like the name ``Ann'') stands for
Approximate Nearest Neighbors. ANN is also a testbed containing
programs and procedures for generating data sets, collecting and
analyzing statistics on the performance of nearest neighbor algorithms
and data structures, and visualizing the geometric structure of these
data structures.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures. 

%files parts
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bins
%{_datadir}/%{name}/contrib
%{_datadir}/%{name}/core
%{_datadir}/%{name}/obsolete
%{_datadir}/%{name}/svg
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/user
%doc parts/README.md
%doc parts/CONTRIBUTING.md
%doc parts/LICENSE.txt

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-app-%{version} -a1

# fix parts path
mv %{name}-parts-%{version} parts
	
# Apply all patches
%patch0 -p1 -b .disable_autoupdate
#patch1 -p1 -b .font
%patch2 -p1 -b .libgit2
%patch3 -p1 -b .libboost

# Use system libs
rm -f pri/quazip.pri
rm -fr src/lib/quazip

# use system twitter4j
find . -name twitter4j-core-\*jar -exec ln -fs /usr/share/java/twitter4j/twitter4j-core.jar '{}' \;

# Use system fonts
#rm -rf resources/fonts/
ln -fs %{_datadir}/fonts/TTF/droid/DroidSans.ttf resources/fonts
ln -fs %{_datadir}/fonts/TTF/droid/DroidSansMono.ttf resources/fonts
ln -fs %{_datadir}/fonts/TTF/droid/DroidSans-Bold.ttf resources/fonts
# FIXME: OCR-A font has not been packaged yet
ln -fs %{_datadir}/fonts/TTF/droid/DroidSansMono.ttf resources/fonts/OCRA.ttf

# remove duplicated Category entry in .desktop
sed -i -e '/Categories=PCB;/d' %{name}.desktop

# fix .desktop
desktop-file-edit \
	--set-icon="%{name}" \
	--remove-category="EDA" \
	--remove-category="PCB" \
	--add-category="GUIDesigner" \
	--add-category="Engineering" \
	--add-category="Science" \
	--add-category="Education" \
	--remove-key="Version" \
	%{name}.desktop

%build
# FIXME: QMAKE_STRIP option is used to disable strip
#        because qmake strip binaries too early
%{qmake_qt5} \
	DEFINES=QUAZIP_INSTALLED \
	QMAKE_STRIP=echo
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

# icons
rm -fr %{buildroot}/%{_iconsdir}/%{name}.png
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -resize "${d}x${d}" resources/images/%{name}_icon.png \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -resize 32x32 resources/images/%{name}_icon.png \
		%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# parts
cp -far parts/bins %{buildroot}%{_datadir}/%{name}/
cp -far parts/contrib %{buildroot}%{_datadir}/%{name}/
cp -far parts/core %{buildroot}%{_datadir}/%{name}/
cp -far parts/obsolete %{buildroot}%{_datadir}/%{name}/
cp -far parts/svg %{buildroot}%{_datadir}/%{name}/
cp -far parts/scripts %{buildroot}%{_datadir}/%{name}/
cp -far parts/user %{buildroot}%{_datadir}/%{name}/

# locales
%find_lang %{lname} --with-qt
	
%check
# desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

