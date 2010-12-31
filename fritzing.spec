%define distsuffix edm

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%define tarname fritzing.2010.10.01.source

Name: fritzing
Version: 0.4.3b
Release: %mkrel 1
Summary: CAD for Arduino
Summary(ru): САПР для Arduino
License: GPLv2/GPLv3
Group: Sciences/Other
Url: http://fritzing.org/
Source: http://fritzing.org/download/%{version}/source-tarball/%{tarname}.tar.bz2
Source1: fritzing.desktop

%description
Fritzing is an open-source initiative to support designers, artists, researchers and hobbyists to work 
creatively with interactive electronics. We are creating a software and website in the spirit of Processing  
and Arduino, developing a tool that allows users to document their prototypes, share them with others, teach electronics 
in a classroom, and to create a pcb layout for professional manufacturing.

%description  -l ru
Fritzing - это Open-Source проект для творческой работы с интерактивной электроникой. 
Ориентирован на  разработчиков, исследователей, творческих людей и просто любителей.
Мы создаём программное обеспечение в духе Processing и Arduino, разрабатываем инструментарий,
позволяющий пользователям документировать их прототипы, делиться прототипами с другими пользователями,
обучать электронике в классе и создавать печатные платы профессионального уровня.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{tarname}

%build
%qmake_qt4 phoenix.pro

%make release

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/bins
install -D -m 755 bins/* %{buildroot}%{_datadir}/%{name}-%{version}/bins/

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/docs/templates/
install -D -m 755 docs/templates/* %{buildroot}%{_datadir}/%{name}-%{version}/docs/templates/

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/contrib/
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/core/
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/obsolete/

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/contrib/breadboard
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/contrib/icon
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/contrib/pcb
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/contrib/schematic

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/breadboard
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/icon
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/pcb
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/schematic

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/breadboard
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/icon
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/pcb
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/schematic


# Может быть, следующие строки лучше потом заменить на линк на каталог пользователя.
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/user/breadboard
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/user/icon
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/user/pcb
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/user/schematic

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/parts/user/

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/sketches/core/

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/translations/syntax/

install -D -m 644 parts/core/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/core/

install -D -m 644 parts/obsolete/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/obsolete/

install -D -m 644 parts/svg/contrib/pcb/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/contrib/pcb/

install -D -m 644 parts/svg/core/breadboard/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/breadboard/
install -D -m 644 parts/svg/core/icon/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/icon/
install -D -m 644 parts/svg/core/pcb/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/pcb/
install -D -m 644 parts/svg/core/schematic/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/core/schematic/

install -D -m 644 parts/svg/obsolete/breadboard/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/breadboard/
install -D -m 644 parts/svg/obsolete/icon/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/icon/
install -D -m 644 parts/svg/obsolete/pcb/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/pcb/
install -D -m 644 parts/svg/obsolete/schematic/* %{buildroot}%{_datadir}/%{name}-%{version}/parts/svg/obsolete/schematic/

install -D -m 644 sketches/core/* %{buildroot}%{_datadir}/%{name}-%{version}/sketches/core/
install -D -m 644 sketches/index.xml %{buildroot}%{_datadir}/%{name}-%{version}/sketches/

install -D -m 644 translations/syntax/* %{buildroot}%{_datadir}/%{name}-%{version}/translations/syntax/
install -D -m 644 translations/*.qm %{buildroot}%{_datadir}/%{name}-%{version}/translations/
install -D -m 644 translations/*.ts %{buildroot}%{_datadir}/%{name}-%{version}/translations/

install -D -m 755 Fritzing %{buildroot}%{_datadir}/%{name}-%{version}/


install -d -m 755 %{buildroot}%{_iconsdir}
install -D -m 644 resources/images/fritzing_icon.png %{buildroot}%{_iconsdir}/

desktop-file-install --vendor mandriva                                    \
                     --dir $RPM_BUILD_ROOT%{_datadir}/applications      \
                                          %{SOURCE1}

%post
if [ $1 = 1 ]; then
    // Do stuff specific to installs
%{__ln_s} %{_datadir}/%{name}-%{version}/Fritzing %{_bindir}/Fritzing
fi
#if [ $1 = 2 ]; then
#    // Do stuff specific to upgrades
#fi

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
    rm -rf %{_bindir}/Fritzing
fi
#if [ $1 = 1 ]; then
#    // Do stuff specific to upgrades
#fi
        

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt LICENSE.GPL2 LICENSE.GPL3
%{_datadir}/%{name}-%{version}
%{_iconsdir}
%{_datadir}/applications/


