#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-geepack
Version  : 1.2.1
Release  : 17
URL      : https://cran.r-project.org/src/contrib/geepack_1.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geepack_1.2-1.tar.gz
Summary  : Generalized Estimating Equation Package
Group    : Development/Tools
License  : GPL-3.0
Requires: R-geepack-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
mean, scale, and correlation structures, through mean link,
        scale link, and correlation link. Can also handle clustered
        categorical responses.

%package lib
Summary: lib components for the R-geepack package.
Group: Libraries

%description lib
lib components for the R-geepack package.


%prep
%setup -q -c -n geepack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552922947

%install
export SOURCE_DATE_EPOCH=1552922947
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geepack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geepack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geepack
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  geepack || :


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
/usr/lib64/R/library/geepack/R/geepack
/usr/lib64/R/library/geepack/R/geepack.rdb
/usr/lib64/R/library/geepack/R/geepack.rdx
/usr/lib64/R/library/geepack/data/dietox.txt.gz
/usr/lib64/R/library/geepack/data/koch.txt.gz
/usr/lib64/R/library/geepack/data/ohio.txt.gz
/usr/lib64/R/library/geepack/data/respdis.txt.gz
/usr/lib64/R/library/geepack/data/respiratory.txt.gz
/usr/lib64/R/library/geepack/data/seizure.txt.gz
/usr/lib64/R/library/geepack/data/sitka89.txt.gz
/usr/lib64/R/library/geepack/data/spruce.txt.gz
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
/usr/lib64/R/library/geepack/libs/geepack.so
/usr/lib64/R/library/geepack/libs/geepack.so.avx2
/usr/lib64/R/library/geepack/libs/geepack.so.avx512
