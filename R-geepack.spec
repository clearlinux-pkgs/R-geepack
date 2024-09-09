#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-geepack
Version  : 1.3.11.1
Release  : 55
URL      : https://cran.r-project.org/src/contrib/geepack_1.3.11.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geepack_1.3.11.1.tar.gz
Summary  : Generalized Estimating Equation Package
Group    : Development/Tools
License  : GPL-3.0
Requires: R-geepack-lib = %{version}-%{release}
Requires: R-broom
Requires: R-magrittr
BuildRequires : R-broom
BuildRequires : R-magrittr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
mean, scale, and correlation structures, through mean link,
    scale link, and correlation link. Can also handle clustered
    categorical responses. See e.g. Halekoh and Højsgaard, (2005,

%package lib
Summary: lib components for the R-geepack package.
Group: Libraries

%description lib
lib components for the R-geepack package.


%prep
%setup -q -n geepack
pushd ..
cp -a geepack buildavx2
popd
pushd ..
cp -a geepack buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725891324

%install
export SOURCE_DATE_EPOCH=1725891324
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/geepack/CITATION
/usr/lib64/R/library/geepack/DESCRIPTION
/usr/lib64/R/library/geepack/INDEX
/usr/lib64/R/library/geepack/Meta/Rd.rds
/usr/lib64/R/library/geepack/Meta/data.rds
/usr/lib64/R/library/geepack/Meta/features.rds
/usr/lib64/R/library/geepack/Meta/hsearch.rds
/usr/lib64/R/library/geepack/Meta/links.rds
/usr/lib64/R/library/geepack/Meta/nsInfo.rds
/usr/lib64/R/library/geepack/Meta/package.rds
/usr/lib64/R/library/geepack/Meta/vignette.rds
/usr/lib64/R/library/geepack/NAMESPACE
/usr/lib64/R/library/geepack/NEWS.md
/usr/lib64/R/library/geepack/R/geepack
/usr/lib64/R/library/geepack/R/geepack.rdb
/usr/lib64/R/library/geepack/R/geepack.rdx
/usr/lib64/R/library/geepack/data/Rdata.rdb
/usr/lib64/R/library/geepack/data/Rdata.rds
/usr/lib64/R/library/geepack/data/Rdata.rdx
/usr/lib64/R/library/geepack/doc/geepack-manual.R
/usr/lib64/R/library/geepack/doc/geepack-manual.Rnw
/usr/lib64/R/library/geepack/doc/geepack-manual.pdf
/usr/lib64/R/library/geepack/doc/index.html
/usr/lib64/R/library/geepack/help/AnIndex
/usr/lib64/R/library/geepack/help/aliases.rds
/usr/lib64/R/library/geepack/help/geepack.rdb
/usr/lib64/R/library/geepack/help/geepack.rdx
/usr/lib64/R/library/geepack/help/paths.rds
/usr/lib64/R/library/geepack/html/00Index.html
/usr/lib64/R/library/geepack/html/R.css
/usr/lib64/R/library/geepack/include/famstr.h
/usr/lib64/R/library/geepack/include/gee2.h
/usr/lib64/R/library/geepack/include/geese.h
/usr/lib64/R/library/geepack/include/geesubs.h
/usr/lib64/R/library/geepack/include/inter.h
/usr/lib64/R/library/geepack/include/ordgee.h
/usr/lib64/R/library/geepack/include/param.h
/usr/lib64/R/library/geepack/include/tnt/cholesky.h
/usr/lib64/R/library/geepack/include/tnt/cmat.h
/usr/lib64/R/library/geepack/include/tnt/fcscmat.h
/usr/lib64/R/library/geepack/include/tnt/fmat.h
/usr/lib64/R/library/geepack/include/tnt/fortran.h
/usr/lib64/R/library/geepack/include/tnt/fspvec.h
/usr/lib64/R/library/geepack/include/tnt/index.h
/usr/lib64/R/library/geepack/include/tnt/lapack.h
/usr/lib64/R/library/geepack/include/tnt/lu.h
/usr/lib64/R/library/geepack/include/tnt/qr.h
/usr/lib64/R/library/geepack/include/tnt/region1d.h
/usr/lib64/R/library/geepack/include/tnt/region2d.h
/usr/lib64/R/library/geepack/include/tnt/stopwatch.h
/usr/lib64/R/library/geepack/include/tnt/subscript.h
/usr/lib64/R/library/geepack/include/tnt/tnt.h
/usr/lib64/R/library/geepack/include/tnt/tntmath.h
/usr/lib64/R/library/geepack/include/tnt/tntreqs.h
/usr/lib64/R/library/geepack/include/tnt/transv.h
/usr/lib64/R/library/geepack/include/tnt/triang.h
/usr/lib64/R/library/geepack/include/tnt/trisolve.h
/usr/lib64/R/library/geepack/include/tnt/vec.h
/usr/lib64/R/library/geepack/include/tnt/vecadaptor.h
/usr/lib64/R/library/geepack/include/tnt/version.h
/usr/lib64/R/library/geepack/include/tntsupp.h
/usr/lib64/R/library/geepack/include/utils.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/geepack/libs/geepack.so
/V4/usr/lib64/R/library/geepack/libs/geepack.so
/usr/lib64/R/library/geepack/libs/geepack.so
