%global qt_version 5.15.8

Summary: Qt5 - WebView component
Name: opt-qt5-qtwebview
Version: 5.15.8
Release: 3%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

%{?opt_qt5_default_filter}

Requires: opt-qt5-qtwebengine >= %{qt_version}
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtdeclarative-devel >= %{qt_version}
BuildRequires: opt-qt5-qtwebengine-devel
BuildRequires: opt-qt5-qtlocation-devel
BuildRequires: opt-qt5-qtwebchannel-devel

%description
Qt WebView provides a way to display web content in a QML application without necessarily
including a full web browser stack by using native APIs where it makes sense.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel%{?_isa}
Requires: opt-qt5-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.*
%{_opt_qt5_libdir}/libQt5WebView.so.5*
%{_opt_qt5_qmldir}/QtWebView/
%dir %{_opt_qt5_plugindir}/webview/
# consider subpkg with rich/soft dependency -- rex
%{_opt_qt5_plugindir}/webview/libqtwebview_webengine.so

%files devel
%{_opt_qt5_headerdir}/QtWebView/
%{_opt_qt5_libdir}/libQt5WebView.so
%{_opt_qt5_libdir}/libQt5WebView.prl
%{_opt_qt5_libdir}/pkgconfig/Qt5WebView.pc
%{_opt_qt5_libdir}/cmake/Qt5WebView
%{_opt_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_opt_qt5_libdir}/libQt5WebView.la

