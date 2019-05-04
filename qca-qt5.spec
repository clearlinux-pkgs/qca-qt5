#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qca-qt5
Version  : 2.2.1
Release  : 5
URL      : https://github.com/KDE/qca/archive/v2.2.1/qca-2.2.1.tar.gz
Source0  : https://github.com/KDE/qca/archive/v2.2.1/qca-2.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause LGPL-2.1
Requires: qca-qt5-bin = %{version}-%{release}
Requires: qca-qt5-lib = %{version}-%{release}
Requires: qca-qt5-license = %{version}-%{release}
Requires: qca-qt5-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : qtbase-dev mesa-dev
Patch1: build.patch

%description
qca-softstore -- Software certificate store Plug-in to QCA
ABOUT
qca-softstore provides simple persistent certificate store for QCA framework.
The plug-in defers the private key access and passphrase prompt to the point
it is actually required, thus enabling the use of files stored on removable media.

%package bin
Summary: bin components for the qca-qt5 package.
Group: Binaries
Requires: qca-qt5-license = %{version}-%{release}

%description bin
bin components for the qca-qt5 package.


%package dev
Summary: dev components for the qca-qt5 package.
Group: Development
Requires: qca-qt5-lib = %{version}-%{release}
Requires: qca-qt5-bin = %{version}-%{release}
Provides: qca-qt5-devel = %{version}-%{release}
Requires: qca-qt5 = %{version}-%{release}

%description dev
dev components for the qca-qt5 package.


%package lib
Summary: lib components for the qca-qt5 package.
Group: Libraries
Requires: qca-qt5-license = %{version}-%{release}

%description lib
lib components for the qca-qt5 package.


%package license
Summary: license components for the qca-qt5 package.
Group: Default

%description license
license components for the qca-qt5 package.


%package man
Summary: man components for the qca-qt5 package.
Group: Default

%description man
man components for the qca-qt5 package.


%prep
%setup -q -n qca-2.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556985477
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1556985477
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qca-qt5
cp COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/COPYING
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/qca-qt5/cmake_modules_COPYING-CMAKE-SCRIPTS
cp plugins/qca-botan/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-botan_COPYING
cp plugins/qca-cyrus-sasl/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-cyrus-sasl_COPYING
cp plugins/qca-gcrypt/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-gcrypt_COPYING
cp plugins/qca-gnupg/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-gnupg_COPYING
cp plugins/qca-logger/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-logger_COPYING
cp plugins/qca-nss/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-nss_COPYING
cp plugins/qca-ossl/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-ossl_COPYING
cp plugins/qca-pkcs11/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-pkcs11_COPYING
cp plugins/qca-softstore/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-softstore_COPYING
cp plugins/qca-wincrypto/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-wincrypto_COPYING
cp plugins/qca-wingss/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/plugins_qca-wingss_COPYING
cp src/botantools/botan/license.txt %{buildroot}/usr/share/package-licenses/qca-qt5/src_botantools_botan_license.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/certs/rootcerts.pem
/usr/mkspecs/features/crypto.prf

%files bin
%defattr(-,root,root,-)
/usr/bin/mozcerts-qt5
/usr/bin/qcatool-qt5

%files dev
%defattr(-,root,root,-)
/usr/include/Qca-qt5/QtCrypto/QtCrypto
/usr/include/Qca-qt5/QtCrypto/qca.h
/usr/include/Qca-qt5/QtCrypto/qca_basic.h
/usr/include/Qca-qt5/QtCrypto/qca_cert.h
/usr/include/Qca-qt5/QtCrypto/qca_core.h
/usr/include/Qca-qt5/QtCrypto/qca_export.h
/usr/include/Qca-qt5/QtCrypto/qca_keystore.h
/usr/include/Qca-qt5/QtCrypto/qca_publickey.h
/usr/include/Qca-qt5/QtCrypto/qca_safetimer.h
/usr/include/Qca-qt5/QtCrypto/qca_securelayer.h
/usr/include/Qca-qt5/QtCrypto/qca_securemessage.h
/usr/include/Qca-qt5/QtCrypto/qca_support.h
/usr/include/Qca-qt5/QtCrypto/qca_textfilter.h
/usr/include/Qca-qt5/QtCrypto/qca_tools.h
/usr/include/Qca-qt5/QtCrypto/qca_version.h
/usr/include/Qca-qt5/QtCrypto/qcaprovider.h
/usr/include/Qca-qt5/QtCrypto/qpipe.h
/usr/lib64/cmake/Qca-qt5/Qca-qt5Config.cmake
/usr/lib64/cmake/Qca-qt5/Qca-qt5ConfigVersion.cmake
/usr/lib64/cmake/Qca-qt5/Qca-qt5Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Qca-qt5/Qca-qt5Targets.cmake
/usr/lib64/libqca-qt5.so
/usr/lib64/pkgconfig/qca2-qt5.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqca-qt5.so.2
/usr/lib64/libqca-qt5.so.2.2.1
/usr/lib64/qca-qt5/crypto/libqca-cyrus-sasl.so
/usr/lib64/qca-qt5/crypto/libqca-gnupg.so
/usr/lib64/qca-qt5/crypto/libqca-logger.so
/usr/lib64/qca-qt5/crypto/libqca-ossl.so
/usr/lib64/qca-qt5/crypto/libqca-softstore.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qca-qt5/COPYING
/usr/share/package-licenses/qca-qt5/cmake_modules_COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/qca-qt5/plugins_qca-botan_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-cyrus-sasl_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-gcrypt_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-gnupg_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-logger_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-nss_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-ossl_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-pkcs11_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-softstore_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-wincrypto_COPYING
/usr/share/package-licenses/qca-qt5/plugins_qca-wingss_COPYING
/usr/share/package-licenses/qca-qt5/src_botantools_botan_license.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qcatool-qt5.1
