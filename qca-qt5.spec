#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xB92A5F04EC949121 (sitter@kde.org)
#
Name     : qca-qt5
Version  : 2.3.10
Release  : 49
URL      : https://download.kde.org/stable/qca/2.3.10/qca-2.3.10.tar.xz
Source0  : https://download.kde.org/stable/qca/2.3.10/qca-2.3.10.tar.xz
Source1  : https://download.kde.org/stable/qca/2.3.10/qca-2.3.10.tar.xz.sig
Source2  : B92A5F04EC949121.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause LGPL-2.1
Requires: qca-qt5-bin = %{version}-%{release}
Requires: qca-qt5-lib = %{version}-%{release}
Requires: qca-qt5-license = %{version}-%{release}
Requires: qca-qt5-man = %{version}-%{release}
BuildRequires : Botan-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : extra-cmake-modules
BuildRequires : gnupg
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(botan-3)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(libsasl2)
BuildRequires : pkgconfig(nss)
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Qt Cryptographic Architecture (QCA)
-----------------------------------
Description
-----------

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) B92A5F04EC949121' gpg.status
%setup -q -n qca-2.3.10
cd %{_builddir}/qca-2.3.10
pushd ..
cp -a qca-2.3.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742416173
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -Dqca_CERTSTORE="/etc/ssl/certs/ca-certificates.crt"  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -Dqca_CERTSTORE="/etc/ssl/certs/ca-certificates.crt"  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../../buildavx2/clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742416173
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qca-qt5
cp %{_builddir}/qca-%{version}/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/caeb68c46fa36651acf592771d09de7937926bb3 || :
cp %{_builddir}/qca-%{version}/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/qca-qt5/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/qca-%{version}/plugins/qca-botan/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-cyrus-sasl/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-gcrypt/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-gnupg/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-logger/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-nss/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-ossl/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-pkcs11/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-softstore/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-wincrypto/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/plugins/qca-wingss/COPYING %{buildroot}/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc || :
cp %{_builddir}/qca-%{version}/src/botantools/botan/license.txt %{buildroot}/usr/share/package-licenses/qca-qt5/902feeccfae30f0eb980e0f50b222cdd2c2df694 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/mkspecs/features/crypto.prf

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mozcerts-qt5
/V3/usr/bin/qcatool-qt5
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
/V3/usr/lib64/libqca-qt5.so.2.3.10
/V3/usr/lib64/qca-qt5/crypto/libqca-botan.so
/V3/usr/lib64/qca-qt5/crypto/libqca-cyrus-sasl.so
/V3/usr/lib64/qca-qt5/crypto/libqca-gcrypt.so
/V3/usr/lib64/qca-qt5/crypto/libqca-gnupg.so
/V3/usr/lib64/qca-qt5/crypto/libqca-logger.so
/V3/usr/lib64/qca-qt5/crypto/libqca-nss.so
/V3/usr/lib64/qca-qt5/crypto/libqca-ossl.so
/V3/usr/lib64/qca-qt5/crypto/libqca-softstore.so
/usr/lib64/libqca-qt5.so.2
/usr/lib64/libqca-qt5.so.2.3.10
/usr/lib64/qca-qt5/crypto/libqca-botan.so
/usr/lib64/qca-qt5/crypto/libqca-cyrus-sasl.so
/usr/lib64/qca-qt5/crypto/libqca-gcrypt.so
/usr/lib64/qca-qt5/crypto/libqca-gnupg.so
/usr/lib64/qca-qt5/crypto/libqca-logger.so
/usr/lib64/qca-qt5/crypto/libqca-nss.so
/usr/lib64/qca-qt5/crypto/libqca-ossl.so
/usr/lib64/qca-qt5/crypto/libqca-softstore.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qca-qt5/902feeccfae30f0eb980e0f50b222cdd2c2df694
/usr/share/package-licenses/qca-qt5/caeb68c46fa36651acf592771d09de7937926bb3
/usr/share/package-licenses/qca-qt5/e60c2e780886f95df9c9ee36992b8edabec00bcc
/usr/share/package-licenses/qca-qt5/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qcatool-qt5.1
